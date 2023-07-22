# GMS Guild Contributions Extractor

The following script uses PaddleOCR to extract guild contribution data in GMS. Extracted data is saved as a CSV file in the root folder.

## Requirements
- Python 3.7.9

## How to Use (Windows)

### 1. Clone the Repository
```
bash
git clone https://github.com/hangwl/MaplestoryOCR.git
```

### 2. Setup Necessary Dependencies
```
setup.bat
```

### 3. Run Script 
```
get_contributions.bat
```

The get_contributions script preprocesses and segments screenshots from the ./input folder into the ./temp folder. Data is then extracted from each individual segment, and stored as a CSV file as the final output, with the current date in the filename.