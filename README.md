# Zomato-Restaurant-analysis

Executive Summary:
This report presents a comprehensive analysis of restaurant data obtained from the Zomato platform with the objective of understanding restaurant distribution, customer preferences, pricing trends, and service performance. The analysis was conducted using Python, SQL, Excel, and Power BI to ensure accurate data cleaning, in-depth exploration, and interactive visualization.

Business Objectives:

The primary objective of this analysis is to derive actionable business insights from Zomato restaurant data that can support strategic decision-making for restaurant owners, investors, and food service platforms. The specific business objectives of this study are outlined below:

    1.	Analyse Restaurant Distribution by Location. To identify areas with high and low restaurant density in order to understand market competition and potential opportunities for expansion.
    2.	Evaluate Customer Ratings and Engagement. To assess rating patterns and vote counts across restaurants and determine the factors that influence customer satisfaction and engagement.
    3.	Assess the Impact of Online Ordering Services. To examine whether restaurants offering online ordering receive higher ratings and greater customer interaction compared to those that do not.
    4.	Analyse the Effect of Table Booking Availability. To understand how table booking services impact customer preferences, ratings, and overall restaurant performance.
    5.	Examine Pricing Trends and Performance. To evaluate the relationship between average cost for two and restaurant ratings in order to identify optimal pricing ranges.
    6.	Identify Popular Cuisines and Service Combinations. To determine the most preferred cuisines and analyse how different service combinations (online order and table booking) influence performance.
    7.	Support Data-Driven Business Decisions. To provide insights that can help stakeholders optimize service offerings, improve customer experience, and plan future growth strategies.

Data Cleaning Process:

Before performing analysis and building dashboards, the raw Zomato dataset was thoroughly cleaned and prepared to ensure accuracy, consistency, and reliability of the results. Since real-world data often contains inconsistencies and missing values, a structured data-cleaning approach was followed using Python, SQL, and Excel.

1. Handling Missing and Null Values:

        The dataset was examined for missing and null values across all columns. Records with critical missing information such as ratings or location were removed, while non-critical missing values were handled appropriately to avoid distortion in the analysis.

2. Removing Duplicate Records:

        Duplicate restaurant entries were identified based on restaurant name and location. These duplicate records were removed to ensure that each restaurant was represented only once in the dataset, preventing overcounting and biased results.

3. Standardizing Data Formats:
  
        Several columns contained inconsistent formatting. Customer ratings were converted into a uniform numerical format, and categorical variables such as online ordering and table booking were standardized to consistent values (e.g., Yes/No). Text fields were cleaned to remove extra spaces and inconsistencies.

4. Cleaning and Validating Categorical Data:

        Invalid or irrelevant values in categorical columns were filtered out. This ensured that categories such as location, cuisine, and service availability were accurate and suitable for grouping and comparison during analysis.

5. Outlier Detection and Filtering:

        Extreme or unrealistic values in numerical fields such as average cost were reviewed and filtered where necessary to maintain realistic and meaningful analysis results.
6. Column Selection and Optimization:

        Irrelevant or unused columns were removed to streamline the dataset and improve analysis efficiency. Only business-relevant fields were retained for exploratory analysis and dashboard development.

Dashboard Explanation:

To present the analysis in an interactive and user-friendly manner, dashboards were developed using Microsoft Excel and Power BI. These dashboards allow stakeholders to explore restaurant performance dynamically and gain quick insights without needing technical knowledge.

1. Excel Dashboard Overview:

        The Excel dashboard was designed to provide a high-level overview of restaurant performance using PivotTables, Pivot Charts, and slicers. It includes key visualizations such as restaurant count by location, average ratings by service type, cost distribution, and cuisine analysis. Slicers enable users to filter data by location, online ordering availability, and table booking options, allowing for flexible and customized analysis.
2. Power BI Dashboard Overview:

        The Power BI dashboard offers a more advanced and visually rich analysis experience. It includes key performance indicator (KPI) cards displaying total restaurants, average rating, total votes, and average cost. Interactive charts and graphs provide insights into location-wise performance, service impact, pricing trends, and customer engagement.

3. Interactivity and User Controls:

        Both dashboards are equipped with filters and slicers that allow users to:
        •	Analyse restaurant performance by location
        •	Compare online ordering versus non-online ordering restaurants
        •	Evaluate the impact of table booking services
        •	Examine pricing segments and rating trends

4. Business Value of the Dashboards:

        The dashboards transform complex datasets into clear visual stories. They enable stakeholders to quickly identify high-performing locations, understand customer preferences, and evaluate service effectiveness. By providing real-time, interactive insights, the dashboards support data-driven decisions that can improve customer experience, optimize pricing strategies, and guide business expansion plans.
Key Insights:

1.	High Restaurant Concentration in Central Locations:

        The analysis shows that central and high-traffic locations have the highest number of restaurants. While these areas offer strong customer demand, they also experience intense competition. Restaurants operating in such locations need differentiated offerings to stand out.
2.	Positive Impact of Online Ordering Services:

        Restaurants that provide online ordering consistently demonstrate higher average ratings and increased customer engagement compared to those that do not. This indicates that convenience and accessibility play a significant role in improving customer satisfaction.
3.	Table Booking Enhances Customer Engagement:

        Restaurants offering table booking services tend to receive more votes and better ratings, especially in premium and busy locations. This suggests that advance reservation options improve the overall dining experience and customer trust.
4.	Mid-Range Pricing Performs Best:

        The relationship between average cost and ratings reveals that mid-range priced restaurants generally receive higher ratings than both low-cost and high-cost establishments. Customers appear to value a balance between price and quality.

Business Recommendations:

    Based on the key insights and findings from the analysis, the following business recommendations are proposed to help improve restaurant performance, enhance customer satisfaction, and support data-driven decision-making.

1.	Expand and Strengthen Online Ordering Services.
2.	Promote Table Booking in High-Traffic Locations.
3.	Focus on Optimal Pricing Strategies.
4.	Target Expansion in Low-Competition Locations.
5.	Leverage Popular Cuisines for Market Growth.
Conclusion:

        While the analysis provides valuable insights into restaurant performance and customer behaviour, it is important to consider certain limitations associated with the dataset and the analytical approach.
1.	Data Scope and Coverage:

        The dataset represents a limited snapshot of restaurants available on the Zomato platform and may not include all restaurants across every location. As a result, findings may not fully reflect the entire restaurant market.
2.	Time Dependency of Data:
   
        The data does not capture changes over time such as seasonal trends, recent restaurant openings, or updated customer ratings. Business dynamics may have evolved since the data was collected.
        The analysis is based solely on Zomato data. Customer behaviour and performance trends may vary across other food delivery or restaurant discovery platforms.
