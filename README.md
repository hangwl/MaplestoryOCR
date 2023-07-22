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
run_scripts.bat
```

The get_contributions script preprocesses and segments screenshots from the ./data/input folder into the ./data/temp folder. Data is then extracted from each individual segment, and stored as a raw CSV file as the output in the ./data/output folder, with the current date in the filename.

The fuzz_igns script uses thefuzz library to implement the fuzzy string matching algorithm on raw ign strings and takes the ./data/guild_assets/igns.csv file as an input for ign choices. The final output is stored as a CSV file as the final output in the ./data/output folder, with the current date in the filename.