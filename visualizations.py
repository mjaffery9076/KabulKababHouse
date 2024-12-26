import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

def plot_sales_trend(weekly_sales):
    """Plots the weekly sales trend."""
    plt.figure(figsize=(14, 7))
    sns.lineplot(x=weekly_sales.index, y=weekly_sales.values, marker='o', color='blue')
    plt.title("Weekly Sales Trend", fontsize=16, fontweight='bold')
    plt.xlabel("Week Starting", fontsize=14)
    plt.ylabel("Total Sales ($)", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(visible=True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

def plot_top_items(top_items):
    """Plots the top-selling products excluding 'Gross Sales'."""
    # Remove 'Gross Sales' if it exists
    if 'Gross Sales' in top_items.index:
        top_items = top_items.drop('Gross Sales')

    # Create the bar chart
    plt.figure(figsize=(10, 6))
    sns.barplot(y=top_items.index, x=top_items.values, hue=top_items.index, palette="coolwarm", dodge=False)
    plt.title("Top-Selling Products", fontsize=16, fontweight='bold')
    plt.xlabel("Quantity Sold", fontsize=14)
    plt.ylabel("Menu Items", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    
    # Add value labels
    for index, value in enumerate(top_items.values):
        plt.text(value + 10, index, f"{value}", fontsize=10, va='center')

    plt.legend([], [], frameon=False)  # Hide the legend
    plt.tight_layout()
    plt.show()


def plot_sales_with_predictions(weekly_sales, predictions):
    """Plots actual sales vs. predicted sales in an interactive dashboard."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=weekly_sales.index, y=weekly_sales.values,
        mode="lines+markers", name="Actual Sales",
        line=dict(color="blue", width=2), marker=dict(size=6)
    ))
    fig.add_trace(go.Scatter(
        x=predictions.index, y=predictions.values,
        mode="lines+markers", name="Predicted Sales",
        line=dict(dash="dot", color="red", width=2), marker=dict(size=6)
    ))
    fig.update_layout(
        title="Weekly Sales Trend with Predictions",
        xaxis_title="Week Starting", yaxis_title="Sales ($)",
        template="plotly_white", hovermode="x"
    )
    fig.show()

import matplotlib.pyplot as plt

def plot_actual_vs_predicted(df):
    """Plots actual sales vs. predicted sales."""
    plt.figure(figsize=(12, 6))
    plt.plot(df["Week Starting"], df["Total Sales"], label="Actual Sales", marker='o', color="blue")
    plt.plot(df["Week Starting"], df["Predicted Sales"], label="Predicted Sales", linestyle="--", color="red")
    plt.title("Actual vs Predicted Sales", fontsize=16, fontweight="bold")
    plt.xlabel("Week Starting", fontsize=14)
    plt.ylabel("Sales ($)", fontsize=14)
    plt.legend()
    plt.grid(visible=True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()
