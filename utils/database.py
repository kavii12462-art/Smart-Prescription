import pandas as pd

# Load CSV file
data = pd.read_csv("dataset/medicines.csv")

def get_medicine_info(medicine_name):
    medicine = medicine_name.lower()

    result = data[data["medicine"].str.lower() == medicine]

    if result.empty:
        return None

    return result.iloc[0].to_dict()