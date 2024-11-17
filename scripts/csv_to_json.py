import logging
import os
from datetime import datetime

import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Helper functions
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y").strftime("%Y-%m-%d")
    except ValueError:
        return None


def parse_number(value):
    try:
        return float(value.replace(",", "").strip())
    except (ValueError, AttributeError):
        return None


def parse_boolean(value):
    return value.strip().lower() in ["yes", "true", "1"]


def handle_missing(value):
    return value if value and value.strip() else None


COLUMN_MAPPINGS = {
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
        "last_price",
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
        "notes",
    ],
}


def process_csv_to_json(input_file, output_file, mapping_key):
    try:
        logging.info(f"Loading CSV file: {input_file}")
        df = pd.read_csv(input_file)

        # Apply column mapping
        columns = COLUMN_MAPPINGS[mapping_key]
        df = df.iloc[:, : len(columns)]
        df.columns = columns

        # Transform data
        if mapping_key == "watches":
            df["size"] = df["size"].apply(parse_number)
            df["first_year"] = df["first_year"].apply(parse_date)
            df["last_year"] = df["last_year"].apply(parse_date)
            df["first_price"] = df["first_price"].apply(parse_number)
            df["last_price"] = df["last_price"].apply(parse_number)
        elif mapping_key == "movements":
            df["diameter"] = df["diameter"].apply(parse_number)
            df["height"] = df["height"].apply(parse_number)
            df["power_reserve"] = df["power_reserve"].apply(parse_number)
            df["tourbillon"] = df["tourbillon"].apply(parse_boolean)

        # Save to JSON
        output_path = os.path.join("data", output_file)
        logging.info(f"Saving JSON file: {output_path}")
        df.to_json(output_path, orient="records", indent=4)

    except Exception as e:
        logging.error(f"Error processing file {input_file}: {e}")
        raise


if __name__ == "__main__":
    from sys import exit

    exit(0)
    files = [
        {"input": "watches.csv", "output": "watches.json", "key": "watches"},
        {"input": "movements.csv", "output": "movements.json", "key": "movements"},
    ]
    for file_info in files:
        process_csv_to_json(file_info["input"], file_info["output"], file_info["key"])
