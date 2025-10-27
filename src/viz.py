#viz.py = plot-funktioner

import matplotlib.pyplot as plt

def top_3_category_by_revenue_graph(df):
    # Get top 3 categories
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
    top_3 = df.groupby('date')['revenue'].sum().reset_index()
    top_3 = top_3.sort_values('revenue', ascending=False).head(3)
    colors = ["#33FF70", "#E4FF33", "#FF5533"]  
    
    plt.figure(figsize=(5,5))
    plt.bar(top_3['date'], top_3['revenue'], color=colors)
    plt.title('Top 3 Dates by Revenue')
    plt.xlabel('Date')
    plt.ylabel('Revenue')
    plt.show()    



def month_by_month_revenue_graph(df):
    df['month'] = df['date'].str.slice(5,7).astype(int)
    monthly_revenue = df.groupby('month')['revenue'].sum().reset_index().sort_values('month')
    
    plt.figure(figsize=(10,5))
    plt.plot(monthly_revenue['month'], monthly_revenue['revenue'], marker='o', color='#335BFF')
    plt.title('Month by Month Revenue')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.xticks(range(1,7))
    plt.grid()
    plt.show()

    
    