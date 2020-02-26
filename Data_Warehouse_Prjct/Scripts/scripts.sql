-- create SalesData table:
create table public.SalesData (
  Index int PRIMARY KEY,
	InvoiceNo varchar,
	StockCode varchar,
	Description varchar,
	Quantity int,
	InvoiceDate timestamp,
	UnitPrice float8,
	CustomerID int,
	Country varchar
	);

-- find top 100 customers by amount of orders
select customerid, count(*) as timesOrdered
from public.salesdata
group by customerid
order by timesOrdered desc
limit 100;

-- find top 10 items sold
select stockcode, quantity
from public.salesdata
order by quantity desc
limit 10;

--AWS copy command

copy salesdata
from 's3://salesdata-bucket/Retail_S3.csv'
credentials 'aws_iam_role=arn:aws:iam::873501442911:role/myRedshiftRole_2'
region 'us-east-1'
TIMEFORMAT 'auto'
CSV
IGNOREHEADER 1;
