#viz.py = plot-funktioner

import matplotlib.pyplot as plt
import pandas as pd
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



def top_3_date_by_revenue_graph(df):
    # Get top 3 dates
    top_3 = df.groupby('date', as_index=False)['revenue'].sum()
    top_3 = top_3.sort_values('revenue', ascending=False).head(3)
    colors = ['#FF5733', '#33C1FF', '#33FF57']  

    plt.figure(figsize=(8,6))
    plt.bar(top_3['date'].astype(str), top_3['revenue'], color=colors)
    plt.title('Top 3 Dates by Revenue')     
    plt.xlabel('date')
    plt.ylabel('revenue')
    plt.show()



def month_by_month_revenue_graph(df):
    # Extrahera månad från datum
    df['month'] = df['date'].dt.month
    
    # Summera revenue per månad
    monthly_revenue = (
        df.groupby('month', as_index=False)['revenue']
          .sum()
          .sort_values('month')
    )

    # Rita linjediagram
    plt.figure(figsize=(10,5))
    plt.plot(monthly_revenue['month'], monthly_revenue['revenue'],
             marker='o', color='#335BFF')
    plt.title('Month by Month Revenue')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.xticks(monthly_revenue['month'])  # dynamisk x-axel
    plt.grid(True)
    plt.tight_layout()
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
    
