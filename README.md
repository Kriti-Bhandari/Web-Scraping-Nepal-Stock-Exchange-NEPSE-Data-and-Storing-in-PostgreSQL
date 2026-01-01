📈 Web Scraping Nepal Stock Exchange (NEPSE) Data and Storing in PostgreSQL

Instructor: Pujan Dahal

Project Overview: 

This project automates the process of collecting daily stock price data from Nepal Stock Exchange (NEPSE) by scraping the Share Sansar website and storing the data in a PostgreSQL database for further analysis and reporting.

The goal of this project is to demonstrate skills in:

-Web scraping

-Data extraction

-Database handling

-Python automation

Such systems are commonly used by financial companies to maintain historical stock data for analytics and decision making.

Data is scraped from:

🔗 https://www.sharesansar.com/today-share-price

The website provides daily trading information for all NEPSE-listed companies.

Tools & Technologies Used :

Programming Language :	Python

Web Scraping :	requests, BeautifulSoup

Database :	PostgreSQL

Database Connector : psycopg2

ORM	: SQLAlchemy

 Project Files :
 
table_creation.py	Creates the PostgreSQL table

nepse_scraper.py	Scrapes data and inserts into database

README.md	Project documentation

Methodology :

-Send Request to Website
The script uses requests to fetch the HTML of the Share Sansar NEPSE page.

-Parse HTML Content
BeautifulSoup is used to locate the stock price table.

-Extract Data
Each row is read and converted into structured fields such as symbol, price, volume, etc.

-Create Database Table
A PostgreSQL table called today_prices is created using SQLAlchemy.

-Insert Data
All scraped records are inserted into the PostgreSQL database.

-Verification
The first 10 rows are fetched and printed to verify successful insertion.

 How to Run the Project
Step 1 – Install required libraries
pip install requests beautifulsoup4 psycopg2 sqlalchemy

Step 2 – Create the table
python table_creation.py

Step 3 – Run the scraper
python nepse_scraper.py

Step 4 – Verify

The script will print the first 10 records from the database after insertion.

Result : 

The PostgreSQL database will contain a full snapshot of the current NEPSE trading day data, making it ready for:

-Trend analysis

-Stock prediction models

-Business intelligence dashboards

-Learning Outcomes

-Through this project, I learned:

-How to scrape live financial data

-How to clean and structure raw web data

-How to store and retrieve data from PostgreSQL

-How to automate real-world data pipelines

Author:

Kriti Bhandari

Bachelor’s in Computer Science

Tribhuvan University (TU), Nepal
