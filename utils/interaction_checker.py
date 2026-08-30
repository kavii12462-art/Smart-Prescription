import pandas as pd

# Load interaction dataset
data = pd.read_csv("dataset/interactions.csv")

# Clean data
data["medicine1"] = data["medicine1"].astype(str).str.strip().str.lower()
data["medicine2"] = data["medicine2"].astype(str).str.strip().str.lower()
data["interaction"] = data["interaction"].astype(str).str.strip()


def check_interaction(med1, med2):
    med1 = med1.strip().lower()
    med2 = med2.strip().lower()

    # Same medicine
    if med1 == med2:
        return "✅ No known interaction found."

    # Search both combinations
    result = data[
        (
            (data["medicine1"] == med1) &
            (data["medicine2"] == med2)
        ) |
        (
            (data["medicine1"] == med2) &
            (data["medicine2"] == med1)
        )
    ]

    if result.empty:
        return "✅ No known interaction found."

    return "⚠️ " + result.iloc[0]["interaction"]