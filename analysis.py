def get_weekly_sales(df):
    """Aggregates weekly sales for trend analysis."""
    return df.groupby("Week Starting")["Total Sales"].sum()

def get_top_selling_items(df):
    """Identifies top-selling products."""
    return df.iloc[:, 5:].sum().sort_values(ascending=False)

def get_summary_statistics(df):
    """Calculates summary statistics for total sales."""
    stats = df["Total Sales"].describe()
    print("\nSummary Statistics for Total Sales:")
    print(stats)
    return stats
