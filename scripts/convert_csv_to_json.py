import pandas as pd

# Load the CSV file, skipping any header rows if necessary
df = pd.read_csv('sheet.csv', skiprows=4)  # Adjust `skiprows` as needed

# Rename the columns to be shorter and simpler
df.columns = [
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
    "last_price",
]

# Convert to JSON with indentation and save as watches.json
df.to_json('watches.json', orient='records', indent=4)

