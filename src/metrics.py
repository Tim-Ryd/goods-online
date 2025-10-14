#metrics.py = nyckeltals-funktioner
def revenue_by_category(df):
    """
    Beräknar total intäkt per kategori.
    Returnerar ett dictionary med formatet:
    {"Elektronik": 12000, "Kläder": 8000, ...}
    """
    grouped = df.groupby("category")["revenue"].sum()
    return grouped.to_dict()

