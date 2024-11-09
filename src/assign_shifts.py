# src/assign_shifts.py

import pandas as pd

def assign_shifts():
    # Load data from CSV files
    seniority_df = pd.read_csv("../data/seniority_table.csv")
    choices_df = pd.read_csv("../data/choices_table.csv")
    bid_df = pd.read_csv("../data/bid_table.csv")

    # Implement assignment logic here
    # TODO: Complete shift assignment based on seniority and preferences

if __name__ == "__main__":
    assign_shifts()
