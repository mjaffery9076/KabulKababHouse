import pandas as pd

def load_data(file_path):
    """Loads and cleans the dataset."""
    try:
        df = pd.read_excel(file_path)
        df["Week Starting"] = pd.to_datetime(df["Week Starting"])
        print("Dataset loaded successfully!")
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File not found at {file_path}. Please check the file path.")
