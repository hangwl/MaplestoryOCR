# GMS Guild Contributions Extractor

The following script uses PaddleOCR to extract guild contribution data in GMS. Extracted data is saved as a CSV file in the root folder.

## Requirements

- Python 3.7.9

## Installation and Setup

Follow these steps to set up the environment and run the script:

### 1. Clone the Repository
```
bash
git clone https://github.com/hangwl/MaplestoryOCR.git
```

### 2. Set Up a Virtual Environment
```
python3.7
python -m venv .venv # Create the virtual environment
source .venv/bin/activate # Activate the virtual environment
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run the Script
```
python script.py
```

The script will preprocess and segment screenshots from the ./input folder into the ./temp folder. Data is then extracted from each individual segment, and stored as a CSV file as the final output, with the current date in the filename.