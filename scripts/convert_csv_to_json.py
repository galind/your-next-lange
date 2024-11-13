import pandas as pd
import json


# Load the CSV file, skipping any header rows if necessary
df = pd.read_csv('sheet.csv', skiprows=4)  # Adjust `skiprows` as needed

# Define the simplified column names for the first 15 expected columns
new_column_names = [
    "ref_no",
    "model",
    "case",
    "dial",
    "hands",
    "strap",
    "lug_width",
    "size",
    "movement",
    "limited",
    "notes",
    "first_year",
    "last_year",
    "first_price",
    "last_price"
]

# Rename only the columns we care about, ignoring any extra columns
df = df.iloc[:, :len(new_column_names)]  # Select only the first 15 columns
df.columns = new_column_names

# Convert DataFrame to JSON format and write to file without escaping "/"
with open('watches.json', 'w') as json_file:
    json.dump(json.loads(df.to_json(orient='records')), json_file, indent=4, ensure_ascii=False)

