use zomato_db;
create table Restaurants (
		Id int auto_increment primary key,
		Address varchar(255),
        Name Varchar(100),
        Online_Order enum('Yes','No'),
        Table_booking enum('Yes','No'),
        Rate decimal(2,1),
        Votes int,
        phone varchar(50),
        Location varchar(100),
        Rest_type varchar(100),
        Dish_Liked text,
        Cuisines varchar(200),
        Cost int,
        Menu_Item text,	
        Type varchar(50),
        City varchar(100)
	);
select * from restaurants;

-- KPI Analsis
-- Total Restaurants
select COUNT(*) as Total_Restaurants from restaurants;
-- Average Rating
select round(avg(Rate),2) as Avg_Rating from restaurants;
-- Avg Cost
SELECT ROUND(AVG(Cost),0) AS Avg_cost from restaurants;

-- location based analysis
-- To find the Top Restarants 
select Location, count(*)  as Total_Restaurants
from restaurants
group by Location
order by Total_Restaurants desc
limit 10;
-- Top 10 location based on votes count
select Location, sum(Votes) as Total_Votes
from restaurants
group by Location
order by Total_Votes desc
limit 10;
-- Rest type
-- rest type distibution 
select Rest_type, count(*) as Total_Restaurants 
from restaurants
group by Rest_type
order by Total_Restaurants desc
limit 10;
-- Avg Rating by restauarants 
select Rest_type, round(avg(Rate),2) as Avg_Rating 
from restaurants
group by Rest_type
order by Avg_Rating desc
limit 10;

-- Online Order Vs Rating 
select Online_Order, round(avg(Rate),2) as Avg_Rating
from restaurants 
group by Online_Order;

-- Votes Comparison
select Online_Order, round(avg(Votes),0) as Avg_Rating
from restaurants 
group by Online_Order;

-- Cost vs Rating
select 
	case 
		when Cost < 300 then 'Low_Cost'
		when Cost between 300 and 700 then 'Mid_Cost'
		else 'High_Cost'
	end as Cost_Catogory,
round (avg(Rate),2) as Avg_Rating
from restaurants
group by Cost_Catogory;

-- Table Booking vs Rating 
select Table_booking, round (Avg(Rate),2) as Avg_Rating 
from restaurants
group by Table_booking
order by Avg_Rating desc
limit 10;

-- Popular Cuisines in Bangoluru
select cuisines, count(*) as Total_Cuisines
from restaurants 
group by cuisines
order by Total_Cuisines desc
limit 10;

-- Best Restaurants in bangoluru
select Name,Rate,Votes, Cost 
from restaurants
where Rate >=4.2 and Votes > 500
order by cost;

-- Top cuisines by average rating:
select Cuisines, avg(Rate) AS avg_rate, COUNT(*) AS cnt
from  restaurants
group by Cuisines
having cnt >= 5
order by avg_rate desc;

-- Best Performace Restaurants 
select Name, Location,Rate,Votes 
from restaurants 
order by Rate desc,Votes desc
limit 10;

select Name, Location,Rate,Votes 
from restaurants 
Where Rate < 3.5
order by Votes desc
limit 10;
truncate restaurants ;
select *from restaurants;
