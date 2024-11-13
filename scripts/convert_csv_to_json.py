import pandas as pd

# Load the CSV file, skipping any header rows if necessary
df = pd.read_csv('sheet.csv', skiprows=4)  # Adjust `skiprows` as needed

# Convert to JSON with indentation and save as watches.json
df.to_json('watches.json', orient='records', indent=4)

