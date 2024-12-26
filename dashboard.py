from data_loader import load_data
from analysis import get_weekly_sales, get_top_selling_items, get_summary_statistics
from visualizations import (
    plot_sales_trend,
    plot_top_items,
    plot_sales_with_predictions,
)
from predictions import predict_next_week_sales
from predictions import predict_sales_for_each_week
from visualizations import plot_actual_vs_predicted

# Step 1: Load the dataset
FILE_PATH = "data/Kabul_Kabab_Sales.xlsx"
data = load_data(FILE_PATH)

# Step 2: Analyze the data
weekly_sales = get_weekly_sales(data)
top_items = get_top_selling_items(data)
summary_stats = get_summary_statistics(data)

# Step 3: Visualize the results
plot_sales_trend(weekly_sales)
plot_top_items(top_items)

# Step 4: Predict next week's sales
predictions = predict_next_week_sales(data)

# Step 5: Visualize predictions alongside actual sales
plot_sales_with_predictions(weekly_sales, predictions)

# Predict sales for each week
data_with_predictions = predict_sales_for_each_week(data)
print(data_with_predictions[["Week Starting", "Total Sales", "Predicted Sales"]])

plot_actual_vs_predicted(data_with_predictions)

