import pandas as pd
import json


# Load the CSV files, skipping any header rows if necessary
watches_df = pd.read_csv('watches.csv', skiprows=4)  # Adjust `skiprows` as needed
movements_df = pd.read_csv('movements.csv', skiprows=4)  # Adjust `skiprows` as needed

# Define the simplified column names for the expected columns
new_column_names = {
    "watches": [
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
    ],
    "movements": [
        "calibre",
        "typical_model",
        "years_sold",
        "winding_type",
        "diameter",
        "height",
        "parts",
        "rubies",
        "diamonds",
        "chatons",
        "power_reserve",
        "frequency",
        "balance_adjust",
        "balance_spring",
        "barrels",
        "tourbillon",
        "fusee_chain",
        "acoustics",
        "seconds_mechanism",
        "column_wheel",
        "power_reserve_display",
        "hours_minutes",
        "seconds",
        "date",
        "day",
        "week",
        "month",
        "leap_year",
        "time_zone",
        "day_night",
        "moonphase",
        "chronograph",
        "flyback",
        "split",
        "notes"
    ],
}

# Rename only the columns we care about, ignoring any extra columns
watches_df = watches_df.iloc[:, :len(new_column_names)]  # Select only the first 15 columns
watches_df.columns = new_column_names["watches"]

movements_df.columns = new_column_names["movements"]

# Convert DataFrame to JSON format and write to files without escaping "/"
with open('watches.json', 'w') as json_file:
    json.dump(json.loads(watches_df.to_json(orient='records')), json_file, indent=4, ensure_ascii=False)

with open("movements.json", "w") as json_file:
    json.dump(json.loads(movements_df.to_json(orient='records')), json_file, indent=4, ensure_ascii=False)

