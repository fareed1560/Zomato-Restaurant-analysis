import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("D:\DA-SQL\Final Project on - DA\Restaurants_data\zomato.ne.csv",encoding='iso-8859-1',low_memory = False)
#print (df.info())
df.rename(columns = {'approx_cost(for two people)':'Cost',
                     'listed_in(type)':'Type',
                     'listed_in(city)':'City',
                     'rate':'Rate',
                     'votes':'Votes',
                     'cuisines':'Cuisines',
                     'book_table':'Table_booking',
                     'online_order':'Online_Order',
                     'name':'Name',
                     'address':'Address',
                     'location':'Location',
                     'rest_type':'Rest_type',
                     'menu_item':'Menu_Item',
                     'dish_liked':'Dish_Liked'},
          inplace = True)
# Split 'rate' column in-place: keep only numeric part, discard text
df['Rate'] = df['Rate'].str.extract(r'(\d+\.\d+|\d+)')
df['Rate'] = pd.to_numeric(df['Rate'], errors='coerce').fillna(0)
# Clean 'approx_cost' column: remove commas, convert to float
df['Cost'] = df['Cost'].str.replace(',', '', regex=False)
df['Cost'] = pd.to_numeric(df['Cost'], errors='coerce').fillna(0)
#Fill missing values: numeric with 0, text with 'NA'
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].fillna('NA')
    else:
        df[col] = df[col].fillna(0)
#print (df.info())
# to find the Correlation between columns
def encode (df):
    for column in df.columns[~df.columns.isin(['Rate','Cost','Votes'])]:
        df[column] = df[column].factorize()[0]
        return df
df_en = encode(df.copy())
#print (df_en)
#print (df.columns)

# find correlation between the columns

df_en['Online_Order'] = (
    df_en['Online_Order']
    .astype(str)
    .str.strip()
    .str.lower()
    .map({'yes':1, 'no':0, 'true':1, 'false':0})
)
df_en['Table_booking'] = (
    df_en['Table_booking']
    .astype(str)
    .str.strip()
    .str.lower()
    .map({'yes':1, 'no':0, 'true':1, 'false':0})
)
useful_cols = ['Rate','Cost','Votes','Online_Order','Table_booking']
corr_df = df_en[useful_cols].apply(pd.to_numeric, errors='coerce')
corr = corr_df.corr(method='spearman')
plt.figure(figsize=(8,6))
sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm',
    fmt=".2f",
    square=True
)
#plt.title("Spearman Correlation Matrix")
#plt.show()
# To save the file
df.to_csv("D:\DA-SQL\Final Project on - DA\Restaurants_data\zomato.cleaned.csv",encoding='iso-8859-1')

#1.What are the top 10 location based on restaurant count?
Top_10_location_count=df['Location'].value_counts().head(10).rename_axis('Location').reset_index(name='Restaurent_Count')
print (Top_10_location_count)

plt.figure(figsize=(10, 8))
bars = plt.bar(range(len(Top_10_location_count)), Top_10_location_count['Restaurent_Count'], 
               color='skyblue', edgecolor='navy', linewidth=1.0)
plt.title('Top 10 Locations by Restaurant Count in Bangalore', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Location', fontsize=12, fontweight='bold')
plt.ylabel('Number of Restaurants', fontsize=12, fontweight='bold')
plt.xticks(range(len(Top_10_location_count)), Top_10_location_count['Location'], rotation=45, ha='right')
# Add value labels on bars
for i, bar in enumerate(bars):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 10,
             f'{int(height)}', ha='center', va='bottom', fontweight='bold')

plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('top_10_locations_matplotlib.png', dpi=300, bbox_inches='tight')
plt.show()

#2.Top 10 location based on votes count?

Top_location_votes = df.groupby('Location')['Votes'].sum().reset_index().sort_values('Votes',ascending = False).head(10)
Top_location_votes.columns = ['Location','Total_Votes']
print (Top_location_votes)

#Creating the Visualisation
plt.figure(figsize=(10,5))
bars = plt.bar(Top_location_votes['Location'], Top_location_votes['Total_Votes'])
# Add value labels above bars
for bar, val in zip(bars, Top_location_votes['Total_Votes']):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height(),
             str(val),
             ha='center', va='bottom', fontsize=9)
plt.title('Top 10 Locations by Total Votes')
plt.xlabel('Location')
plt.ylabel('Total Votes')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
#3.Top 10 location based on Average cost?
Top_location_cost = df.groupby('Location')['Cost'].mean().reset_index().sort_values('Cost',ascending = False).head(10)
Top_location_cost.columns= ['Location','Cost']
print (Top_location_cost)

plt.figure(figsize=(10, 6))
plt.bar(Top_location_cost['Location'], Top_location_cost['Cost'])

plt.title('Top 10 Locations by Average Cost for Two')
plt.xlabel('Location')
plt.ylabel('Average Cost for Two')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
#4.Is online delivery service available?
online_counts = df['Online_Order'].value_counts()
print (online_counts)
plt.figure(figsize=(6, 6))
plt.pie(
    online_counts,
    labels=online_counts.index,
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Online Delivery Availability")
plt.axis('equal')
plt.show()
#5.Is Table Booking service available?
df['Table_booking'] = (
    df['Table_booking']
    .astype(str)
    .str.strip()
    .str.lower()
    .map({
        'yes': 'Yes',
        'no': 'No',
        'true': 'Yes',
        'false': 'No',
        '1': 'Yes',
        '0': 'No'
    })
)
df = df[df['Table_booking'].isin(['Yes', 'No'])]
print(df['Table_booking'].value_counts())

counts = df['Table_booking'].value_counts()
wedges, texts, autotexts = plt.pie(
    counts,
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Table Booking Availability")
plt.legend(
    wedges,
    counts.index,
    title="Table Booking",
    loc="center left",
    bbox_to_anchor=(1, 0.5)
)
plt.ylabel("")
plt.show()
#6 Is there any difference b/w rate of restaurants accepting and not accepting online orders?
orders_deffernce = df.groupby('Online_Order')['Rate'].agg(['count','mean','median']).reset_index().sort_values('mean',ascending=False)
orders_deffernce['percentage'] = (orders_deffernce['count']/len(df)*100).round(1).astype(str)+'%'
print (orders_deffernce)
# Visualization
plt.figure(figsize=(7,5))
bars = plt.bar(orders_deffernce['Online_Order'], orders_deffernce['mean'])
# Add percentage labels above bars
for bar, pct in zip(bars, orders_deffernce['percentage']):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height(),
             pct,
             ha='center', va='bottom', fontsize=10)
plt.title('Average Rating by Online Order Availability')
plt.xlabel('Online Order (Yes / No)')
plt.ylabel('Average Rating')
plt.tight_layout()
plt.show()

#7.Difference b/w rate of restaurants providing table booking service and not providing table booking service
Table_defference =df.groupby('Table_booking')['Rate'].agg(['count','mean','median']).reset_index().sort_values('mean',ascending=False)
Table_defference['percentage']= (Table_defference['count']/ len(df)*100).round(1).astype(str)+'%'
print (Table_defference)
#visualization 
plt.figure(figsize=(6,4))
bars = plt.bar(Table_defference['Table_booking'], Table_defference['mean'])
# Add percentage labels above bars
for bar, pct in zip(bars, Table_defference['percentage']):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height(),
             pct,
             ha='center', va='bottom', fontsize=10)
plt.title('Mean Rating by Table Booking Option')
plt.xlabel('Book Table')
plt.ylabel('Mean Rating')
plt.tight_layout()
plt.show()

#8.Rating distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Rate'], bins=20, kde=True)
plt.title("Rating Distribution")
plt.show()

#9.Location wise rating?
top_locations= df['Location'].value_counts().head(15).index.tolist()
Loc_Rating= df [df['Location'].isin(top_locations)].groupby('Location')['Rate'].mean().reset_index().sort_values('Rate',ascending=False).round(2)
print(Loc_Rating)
#Visualization
plt.figure(figsize=(10,5))
bars = plt.bar(Loc_Rating['Location'], Loc_Rating['Rate'])
# Add rating labels above bars
for bar, rating in zip(bars, Loc_Rating['Rate']):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height(),
             round(rating, 2),
             ha='center', va='bottom', fontsize=9)
plt.title('Average Rating of Top 15 Locations')
plt.xlabel('Location')
plt.ylabel('Average Rating')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#10.Which are the most common restaurant type in Bangalore?
rest_type_counts= df['Rest_type'].value_counts().head(15)
rest_type_common = ((rest_type_counts)/len(df)*100).round(1)
rest_type_sum=pd.DataFrame({'Restaurent_type': rest_type_counts.index,
                            'count':rest_type_counts.values,
                            'percentage':rest_type_common.values
                            }).reset_index(drop=True)
print ("\n Top Most common Restarents Types")
print (rest_type_sum)
plt.figure(figsize=(12,6))
bars = plt.bar(rest_type_sum['Restaurent_type'], rest_type_sum['count'])
# Add percentage labels above bars
for bar, pct in zip(bars, rest_type_sum['percentage']):
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height(),
             f"{pct}%",
             ha='center', va='bottom', fontsize=9)
plt.title('Top 15 Restaurant Types')
plt.xlabel('Restaurant Type')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#11.Average of rating based of different restaurant type.
rating_by_type = df.groupby('Rest_type').agg({'Rate':['count','mean','median'],'Name':'count'}).round(3)
rating_by_type.columns = ['Rating_Count','Avg_Rating','Medina_Rating','Total_Restaurents']
rating_by_type = rating_by_type.sort_values('Avg_Rating',ascending=True).head(30)
print(rating_by_type)
# Visualization
plt.figure(figsize=(10,8))
bars = plt.barh(rating_by_type.index, rating_by_type['Avg_Rating'])
for bar, rating in zip(bars, rating_by_type['Avg_Rating']):
    plt.text(bar.get_width(),
             bar.get_y() + bar.get_height()/2,
             round(rating, 2),
             va='center', ha='left', fontsize=9)
plt.title('Average Rating by Restaurant Type')
plt.xlabel('Average Rating')
plt.ylabel('Restaurant Type')
plt.tight_layout()
plt.show()

#12.What are the different type of services restaurant provide?
service_col = None
for c in df.columns:
    if 'listed' in c.lower() or 'service' in c.lower() or c.lower() in ['type','Rest_type', 'Type']:
        service_col = c
        break
if service_col:
    srv = df[service_col].fillna('Unknown').astype(str)
    srv_counts = srv.value_counts().reset_index()#.rename(columns={'index':'service','%s'%service_col:'Service_type'})
    srv_counts.columns = ['service', 'Service_type']
    print (srv_counts)
plt.figure(figsize=(10,5))
bars = plt.bar(srv_counts['service'], srv_counts['Service_type'])
# Add count labels above bars
for bar, val in zip(bars, srv_counts['Service_type']):
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        str(val),
        ha='center', va='bottom', fontsize=9
    )
plt.title('Service / Listed Type Distribution')
plt.xlabel('Service Type')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
service_df = df.groupby(['Online_Order','Table_booking']).size()

#13.Relation between types of services and their rating
print("\n STATISTICAL COMPARISONS:")
service_col = None
for c in df.columns:
    if 'listed' in c.lower() or 'service' in c.lower() or c.lower() in ['type','Rest_type','Type']:
        service_col = c
        break
if service_col:
    srv = df[service_col].fillna('Unknown').astype(str)
    # Create dataframe with rating statistics
    service_rating = df.groupby(srv).agg({
        'Rate': ['count','mean','median']
    }).reset_index()
    # Flatten columns
    service_rating.columns = ['service', 'count', 'avg_rating', 'median_rating']
    # Sort by avg_rating descending
    service_rating = service_rating.sort_values('avg_rating', ascending=False).head(20)
    print (service_rating)

plt.figure(figsize=(10,6))
plt.scatter(service_rating['count'], service_rating['avg_rating'], color='green', s=80)
for i, txt in enumerate(service_rating['service']):
    plt.annotate(txt, (service_rating['count'].iloc[i], service_rating['avg_rating'].iloc[i]),
                 rotation=45, ha='right', fontsize=8)
plt.title('Relation Between Service Type Count and Average Rating')
plt.xlabel('Number of Restaurants')
plt.ylabel('Average Rating')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
service_rating = df.pivot_table(
    values='Rate',
    index='Online_Order',
    columns='Table_booking',
    aggfunc='mean'
)
sns.heatmap(service_rating, annot=True)
plt.title("Service Combination vs Avg Rating")
plt.show()

#14.Cost distribution
price_bins= [0,400,600,1000,float('inf')]
price_labels=['Budget (<400)','Affordable(400-600)','Mid-Range(600-800)','Premium(>1000)']
df['price_segment']=pd.cut(df['Cost'],bins = price_bins,
                           labels=price_labels,right=False)
price_dist = df['price_segment'].value_counts(sort=True)
price_dist_p = (price_dist/len(df)*100).round(1)
print ("\n Price Segment Distributions:")
price_summary = pd.DataFrame({
    'segment': price_dist.index,
    'count': price_dist.index,
    'Percentage':price_dist_p.values,
    'Avg_cost': df.groupby('price_segment')['Cost'].mean().round(0).values
    })
print (price_summary)                     
fig=plt.figure(figsize=(20,16))
plt.hist(df['Cost'],bins=50)
plt.title("Cost Distribution Histogram",fontsize=16,fontweight = 'bold')
plt.xlabel('Cost for Two')
plt.ylabel('Frequence')
plt.legend()
plt.grid(alpha=0.3)
plt.show()

#15.Cost vs rating
if not df['Cost'].isnull().all():
    clean_costs = df['Cost'].dropna()
    cap = clean_costs.quantile(0.95)
sub = df[['Cost','Rate']].dropna()
sub_plot = sub[sub['Cost']<=cap]
plt.figure(figsize=(7,5))
plt.scatter(sub_plot['Cost'], sub_plot['Rate'], alpha=0.4, s=10)
plt.xlabel("Cost for two")
plt.ylabel("Rating")
plt.title("Cost vs Rating (capped at 95th percentile)")
try:
    z = np.polyfit(sub_plot['cost_for_two'], sub_plot['Rate'], 1)
    p = np.poly1d(z)
    xs = np.linspace(sub_plot['cost_for_two'].min(), sub_plot['cost_for_two'].max(), 100)
    plt.plot(xs, p(xs))
except Exception as e:
    pass
    plt.tight_layout()
    plt.grid(True)
    plt.show()
#16.Which are the most popular casual dining restaurant chains?
casual_df = df[df['Rest_type'].str.contains("Casual Dining", case=False, na=False)]
# Count restaurant chains
casual_chain_counts = (
    casual_df['Name']
    .value_counts()
    .head(10)     # Top 10
    .rename_axis('Restaurant_Chain')
    .reset_index(name='Count')
)
print("\nTop 10 Casual Dining Restaurant Chains in Bangalore:")
print(casual_chain_counts)
#Visualization
plt.figure(figsize=(12,6))
bars = plt.bar(casual_chain_counts['Restaurant_Chain'], casual_chain_counts['Count'])
plt.xlabel("Restaurant Chain", fontsize=12, fontweight='bold')
plt.ylabel("Number of Outlets", fontsize=12, fontweight='bold')
plt.title("Top 10 Casual Dining Restaurant Chains in Bangalore", fontsize=14, fontweight='bold')
# Add labels on bars
for bar in bars:
    h = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        h + max(casual_chain_counts['Count']) * 0.02,
        str(h),
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
#17.Most popular Quick bites restaurant chains
quick_bites_df = df[df['Rest_type'].str.contains("Quick Bites", case=False, na=False)]
# Count restaurant chains
quick_bites_chain_counts = (
    quick_bites_df['Name']
    .value_counts()
    .head(10)   # Top 10
    .rename_axis('Restaurant_Chain')
    .reset_index(name='Count')
)
print("\nTop 10 Quick Bites Restaurant Chains in Bangalore:")
print(quick_bites_chain_counts)
plt.figure(figsize=(12,6))
bars = plt.bar(quick_bites_chain_counts['Restaurant_Chain'],
                quick_bites_chain_counts['Count'])
plt.xlabel("Restaurant Chain", fontsize=12, fontweight='bold')
plt.ylabel("Number of Outlets", fontsize=12, fontweight='bold')
plt.title("Top 10 Quick Bites Restaurant Chains in Bangalore",
          fontsize=14, fontweight='bold')
# Add data labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + max(quick_bites_chain_counts['Count']) * 0.02,
        str(height),
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
#18.Most popular cafes of Bangalore
cafe_df = df[df['Rest_type'].str.contains("Cafe", case=False, na=False)]
# Count popular cafe chains
popular_cafes = (
    cafe_df['Name']
    .value_counts()
    .head(10)    # Top 10
    .rename_axis('Cafe_Name')
    .reset_index(name='Count')
)
print("\nTop 10 Most Popular Cafes in Bangalore:")
print(popular_cafes)
plt.figure(figsize=(12,6))
bars = plt.bar(popular_cafes['Cafe_Name'], popular_cafes['Count'])
plt.xlabel("Cafe Name", fontsize=12, fontweight='bold')
plt.ylabel("Number of Outlets", fontsize=12, fontweight='bold')
plt.title("Top 10 Most Popular Cafes in Bangalore", fontsize=14, fontweight='bold')
# Add labels above each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + max(popular_cafes['Count']) * 0.02,
        str(height),
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
#19.Finding the best restaurants in each category - cheapest, highly rated and reliable(large number of votes)
#1. CHEAPEST RESTAURANTS (Low cost + High rating + Reliable)
print("\n TOP 10 CHEAPEST HIGHLY-RATED RELIABLE RESTAURANTS")
cheapest_top = df[(df['Rate'] >= 4.0) & 
                  (df['Votes'] >= 100)].nlargest(10, 'Rate')
cheapest_top = cheapest_top.sort_values(['Cost', 'Rate', 'Votes'], ascending=[True, False, False])
print(cheapest_top[['Name', 'Location', 'Rate', 'Votes', 'Cost','Cost']].round(2).head(10))

# 2. HIGHEST RATED RESTAURANTS (Rating >= 4.5 + Reliable)
print("\n TOP 10 HIGHEST RATED RELIABLE RESTAURANTS")
highest_rated = df[(df['Rate'] >= 4.5) & 
                   (df['Votes'] >= 500)].nlargest(10, 'Rate')
highest_rated = highest_rated.sort_values(['Rate', 'Votes'], ascending=[False, False])
print(highest_rated[['Name', 'Location', 'Rate', 'Votes', 'Cost']].head(10))

# 3. MOST RELIABLE (High votes + Good rating)
print("\n TOP 10 MOST RELIABLE (High Votes + Good Rating)")
reliable = df[(df['Rate'] >= 4.0) & 
              (df['Votes'] >= 1000)].nlargest(10, 'Votes')
reliable = reliable.sort_values(['Votes', 'Rate'], ascending=[False, False])
print(reliable[['Name', 'Location', 'Rate', 'Votes', 'Cost']].head(10))
# Create summary DataFrame
summary = pd.DataFrame({
    'Category': ['Cheapest Top Rated', 'Highest Rated', 'Most Reliable'],
    'Restaurants': [len(cheapest_top), len(highest_rated), len(reliable)],
    'Avg_Rating': [cheapest_top['Rate'].mean(), highest_rated['Rate'].mean(), reliable['Rate'].mean()],
    'Avg_Cost': [cheapest_top['Cost'].mean(), highest_rated['Cost'].mean(), reliable['Cost'].mean()],
    'Total_Votes': [cheapest_top['Votes'].sum(), highest_rated['Votes'].sum(), reliable['Votes'].sum()]
})
print("\n CATEGORY SUMMARY:")
print(summary.round(1))
#20.Which are the most popular cuisines of Bangalore?
df["Cuisines"] = df['Cuisines'].astype(str)
cuisines_expanded = df.assign(cuisine=df["Cuisines"].str.split(',').explode("Cuisine"))
cuisines_expanded = cuisines_expanded[cuisines_expanded["Cuisines"]!=""]
popular_cuisines = (cuisines_expanded.groupby("Cuisines").agg
                    (Restuarent_Count=("Name","count"),
                     Total_Votes=("Votes","sum"),
                     Avg_Rating=("Rate","mean")
                     ).round(2).sort_values(["Restuarent_Count","Total_Votes"],ascending = False).reset_index().head(10))
print (popular_cuisines)
# Visualization 
plt.figure(figsize=(12,6))
plt.barh(popular_cuisines['Cuisines'], popular_cuisines['Restuarent_Count'])
plt.xlabel("Number of Restaurants")
plt.ylabel("Cuisine")
plt.title("Top 10 Most Popular Cuisines in Bangalore")
plt.gca().invert_yaxis()  # Highest at top
plt.tight_layout()
plt.show()
#21.Which are the top restaurant chains in Bangalore?
Restaurentcounts = df['Name'].value_counts().reset_index().rename(columns={'index':'Name','name':'Restaurants'}).head(10)
print(Restaurentcounts)
# Remove duplicates based on restaurant name + address
df["unique_id"] = df["Name"].astype(str).str.strip() + " | " + df["Address"].astype(str).str.strip()
df = df.drop_duplicates(subset=["unique_id"])
# Group by restaurant name to find chain counts
chains = (
    df.groupby("Name")
    .agg(
        Outlet_Count=("Address", "count"),
        Total_Votes=("Votes", "sum"),
        Avg_Rating=("Rate", "mean")
    )
    .sort_values(["Outlet_Count", "Total_Votes"], ascending=False)
    .reset_index()
).round(2).head(10)
# Filter only restaurant chains with at least 3 outlets
top_chains = chains[chains["Outlet_Count"] >= 3]
print (top_chains)
df['Name'].value_counts().head(10).plot(kind='bar')
plt.title("Top Restaurant Chains")
plt.show()
























