#!/.venv/Scripts/python.exe



import numpy as np
import pandas as pd

raw_igns = pd.read_csv('2023-07-21.csv')['IGN']
print(raw_igns)

from fuzzywuzzy import fuzz

string1 = "apple"
string2 = "appel"

similarity_score = fuzz.ratio(string1, string2)
print(similarity_score)  # Output: 91