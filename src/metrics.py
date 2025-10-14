#metrics.py = nyckeltals-funktioner

def top_3_category_by_revenue(df):
    top_3 = df.groupby('category')['revenue'].sum().reset_index().sort_values('revenue', ascending=False).head(3)

    return top_3
