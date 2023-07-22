import os
import pandas as pd
from datetime import date
from thefuzz import fuzz, process

class IGNMatcher:
    def __init__(self, input_file, choices_file, min_score_threshold=80):
        self.input_file = input_file
        self.choices_file = choices_file
        self.min_score_threshold = min_score_threshold

    def process_raw_ign(self, raw_ign, choices):
        matched_ign, score = process.extractOne(raw_ign, choices, scorer=fuzz.token_sort_ratio)
        if score < self.min_score_threshold:
            return (f"{raw_ign}[?]", score)
        return (matched_ign, score)

    def match_igns(self):
        df = pd.read_csv(self.input_file)
        raw_igns = df['IGN'].tolist()

        choices = pd.read_csv(self.choices_file)['IGN'].tolist()

        matched_igns = [self.process_raw_ign(raw_ign, choices)[0] for raw_ign in raw_igns]

        new_df = pd.DataFrame({'IGN': matched_igns})
        df = pd.concat([new_df, df.drop('IGN', axis=1)], axis=1)

        output_file = f"./data/output/{date.today()}.csv"
        df.to_csv(output_file, index=False)
        print(f"Matched IGN data saved to {output_file}")

def main():
    input_file = f"./data/output/{date.today()}_raw.csv"
    choices_file = "./data/guild_assets/igns.csv"
    ign_matcher = IGNMatcher(input_file, choices_file)
    ign_matcher.match_igns()

if __name__ == "__main__":
    main()
