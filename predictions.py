import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

def train_sales_model(df):
    """Trains a model to predict next week's sales."""
    df["Week Number"] = (df["Week Starting"] - df["Week Starting"].min()).dt.days // 7
    X = df[["Week Number"]]
    y = df["Total Sales"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, "models/sales_model.pkl")
    print("Sales prediction model trained and saved!")

import pandas as pd
import joblib

def predict_next_week_sales(df):
    """Predicts total sales for the next week."""
    # Load the trained model
    try:
        model = joblib.load("models/sales_model.pkl")
    except FileNotFoundError:
        raise FileNotFoundError("The sales prediction model is missing. Please train the model first.")

    # Prepare the input for the next week's prediction
    last_week = df["Week Starting"].max()
    next_week = last_week + pd.Timedelta(days=7)
    week_number = (next_week - df["Week Starting"].min()).days // 7

    # Ensure the input has the same structure as training data
    prediction_input = pd.DataFrame({"Week Number": [week_number]})

    # Make the prediction
    predicted_sales = model.predict(prediction_input)
    return pd.Series([predicted_sales[0]], index=[next_week])

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def predict_sales_for_each_week(df):
    """
    Predicts sales for each week using only data from prior weeks.
    Args:
    - df: DataFrame containing sales data with 'Week Starting' and 'Total Sales'.
    
    Returns:
    - pd.DataFrame: Original DataFrame with an added 'Predicted Sales' column.
    """
    # Ensure the dataframe is sorted by 'Week Starting'
    df = df.sort_values("Week Starting").reset_index(drop=True)
    
    # Add a 'Week Number' column
    df["Week Number"] = (df["Week Starting"] - df["Week Starting"].min()).dt.days // 7
    
    # Create a column to store predictions
    df["Predicted Sales"] = None

    # Iterate through each week, training on prior weeks and predicting the current week
    for i in range(1, len(df)):
        # Training data includes all weeks up to the previous week
        train_data = df.iloc[:i]
        X_train = train_data[["Week Number"]]
        y_train = train_data["Total Sales"]

        # Train the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predict sales for the current week
        current_week = df.iloc[i]["Week Number"]
        df.at[i, "Predicted Sales"] = model.predict([[current_week]])[0]

    return df

