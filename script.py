import os
import statistics
from datetime import date
from matplotlib import pyplot as plt
import pandas as pd
from PIL import Image
from paddleocr import PaddleOCR

class DataExtractor:
    def __init__(self, input_folder, threshold=100):
        self.input_folder = input_folder
        self.threshold = threshold
        self.ocr_model = PaddleOCR(lang='en', use_angle_cls=False, show_log=False)

    def list_files(self):
        return [os.path.join(self.input_folder, filename) for filename in os.listdir(self.input_folder)]

    def read(self, file_path):
        result = self.ocr_model.ocr(file_path)
        return [line[1][0] for res in result for line in res]

    def preprocess(self, image_file):
        image = Image.open(image_file).convert("L")
        image = image.point(lambda p: 0 if p > self.threshold else 255)
        return image

    def chop(self, image):
        width, height = image.size
        pixel_values_along_x = [image.getpixel((x, y)) for y in range(height) for x in range(width)]
        standard_dev_y = [statistics.stdev(pixel_values_along_x[y * width: (y + 1) * width]) for y in range(height)]
        low_standard_dev_y = [y for y, stddev in enumerate(standard_dev_y) if stddev < 5]

        y_bounds = [(low_standard_dev_y[i], low_standard_dev_y[i + 1]) for i in range(len(low_standard_dev_y) - 1) if low_standard_dev_y[i + 1] - low_standard_dev_y[i] > 1]

        image_segments = [image.crop((0, y_start - 5, image.width, y_end + 5)) for y_start, y_end in y_bounds]
        return standard_dev_y, image_segments

    def plot_std_dev_along_y(self, standard_dev_y):
        height = len(standard_dev_y)
        i = range(height)
        plt.plot(i, standard_dev_y)
        plt.xlabel('Y-Coordinate')
        plt.ylabel('Std. Dev')
        plt.title('Std. Dev along Y-axis')
        plt.show()

    def read_segments(self):
        results = []
        for i, file in enumerate(self.list_files()):
            preprocessed_image = self.preprocess(file)
            std_dev_y, image_segments = self.chop(preprocessed_image)
            for j, segment in enumerate(image_segments):
                segment.save(f"./temp/{i}_{j}.jpg")
                results.append(self.read(f"./temp/{i}_{j}.jpg"))
            # self.plot_std_dev_along_y(std_dev_y)
        return results

    def process_results(self, results):
        final_results = []
        for result in results:
            scores = result[-3:]
            person = result[:-3]
            name_job_level_title_string = ' '.join(person).replace('.', ' ').replace(')', ' ')
            name_job_level_title_list = name_job_level_title_string.split()

            name = name_job_level_title_list[0]
            level = name_job_level_title_list[-2][-3:]
            culvert = scores[-2]
            flag = scores[-1]

            final_results.append([name, level, culvert, flag])

        df = pd.DataFrame(final_results, columns=['IGN', 'LVL', 'CULVERT', 'FLAG'])
        output_file = f"./{date.today()}.csv"
        df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")

    def clear_temp_folder(self):
        temp_folder = "./temp"
        if os.path.exists(temp_folder):
            files = os.listdir(temp_folder)
            for file in files:
                file_path = os.path.join(temp_folder, file)
                os.remove(file_path)

    def run_extraction(self):
        self.clear_temp_folder()
        results = self.read_segments()
        self.process_results(results)

if __name__ == '__main__':
    input_folder = "./input"
    threshold = 100
    extractor = DataExtractor(input_folder, threshold)
    extractor.run_extraction()
