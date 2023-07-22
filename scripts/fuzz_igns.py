from datetime import date
import pandas as pd
from thefuzz import fuzz, process

def process_raw_ign(raw_ign, choices, threshold):
    matched_ign, score = process.extractOne(raw_ign, choices, scorer=fuzz.token_sort_ratio)
    if score < threshold:
        return (f"{raw_ign}[?]", score)
    return (matched_ign, score)

df =  pd.read_csv(f"./data/output/{date.today()}_raw.csv")

raw_igns = df['IGN'].tolist()
choices = pd.read_csv("./data/guild_assets/igns.csv")['IGN'].tolist()

# use extractOne method to set scorer threshold
threshold = 80
matched_igns = [process_raw_ign(raw_ign, choices, threshold)[0] for raw_ign in raw_igns]

new_df = pd.DataFrame({'IGN': matched_igns})
df = pd.concat([new_df, df.drop('IGN', axis=1)], axis=1)
output_file = f"./data/output/{date.today()}.csv"
df.to_csv(output_file, index=False)
print(f"Matched IGN data saved to {output_file}")