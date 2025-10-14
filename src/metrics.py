#metrics.py = nyckeltals-funktioner
def revenue_by_category(df):
    """
    Beräknar total intäkt per kategori.
    Returnerar ett dictionary med formatet:
    {"Elektronik": 12000, "Kläder": 8000, ...}
    """
    grouped = df.groupby("category")["revenue"].sum()
    return grouped.to_dict()

def top_3_category_by_revenue(df):
    top_3 = df.groupby('category')['revenue'].sum().reset_index().sort_values('revenue', ascending=False).head(3)

    return top_3
