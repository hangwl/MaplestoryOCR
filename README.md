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

## Scripts

```get_contributions.py``` 
preprocesses and segments screenshots from the ./data/input folder into the ./data/temp folder. 

```fuzz_igns.py``` 
uses thefuzz library to implement the fuzzy string matching algorithm on raw IGN strings and takes the ./data/guild_assets/igns.csv file as an input for IGN choices. The final output is saved in the ./data/output folder, with the current date in the filename.