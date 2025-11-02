#viz.py = plot-funktioner

import matplotlib.pyplot as plt
from . import metrics

def top_3_category_by_revenue_graph(df):
    """
    Ger tillbaka ett stapeldiagram som visualiserar top 3 kategorier utifrån intäkt.
    """
    top_3 = df.groupby('category')['revenue'].sum().reset_index()
    top_3 = top_3.sort_values('revenue', ascending=False).head(3)
    colors = ['#FF5733', '#33C1FF', '#33FF57']  
    
    plt.figure(figsize=(5,5))
    plt.bar(top_3['category'], top_3['revenue'], color=colors)
    plt.title('Top 3 Categories by Revenue')
    plt.xlabel('Category')
    plt.ylabel('Revenue')
    plt.show()

def revenue_per_city(df):
    city_data = metrics.summary_city(df)
    plt.figure(figsize=(8,5))
    plt.bar(city_data["city"], city_data["total_revenue"], color="pink")
    plt.title("Intäkt per stad")
    plt.xlabel("Stad")
    plt.ylabel("Total intäkt (kr)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()