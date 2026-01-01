import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, MetaData, Table
from decimal import Decimal

DB_USER = "postgres" 
DB_PASSWORD = "kriti"
HOST = "localhost"
PORT = 5432
DB_NAME = "postgres"
DB_SCHEMA = "public"

CONNECTION_STRING = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

SHARE_SANSAR_URL = "https://www.sharesansar.com/today-share-price"

def fetch_page(): 
    response = requests.get(SHARE_SANSAR_URL)  #(Use of Request for Web Scraping)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")#(Use of Beautiful Soup for Web Scraping)

def extract_eachtable_rows(soup):
    table = soup.find("table", {"id": "headFixed"})#(extracting table with id called headfixed)
    tbody = table.find("tbody")
    rows = tbody.find_all("tr")
    return rows 

def parse_eachTable_rows(rows):
    data = []
    for row in rows:
        cols = [cell.text.strip() for cell in row.find_all("td")]#(Extracting td values and removing extrav spaces using strip method.)
        # (Skipping empty rows)
        if len(cols) < 24: 
            continue
        data.append(cols)
    return data
  
def clean_number(value):
    if value is None:
        return None
    value = value.replace(",", "")  #(Removing commas in the data)
    if value == "" or value == "-": #(if theres empty value or '-', replacing it with None)
        return None
    try:            #(Exception handling using Try-catch )
        return float(value)
    except:
        return None
 

def convert_list_to_dict(records):
    columns = [
        "s_no", "symbol", "conf", "open", "high", "low", "close", "ltp",
        "close_ltp", "close_ltp_percent", "vwap", "vol", "prev_close",
        "turnover", "trans", "diff", "range", "diff_percent", "range_percent",
        "vwap_percent", "days_120", "days_180", "weeks_52_high", "weeks_52_low"
    ]
    numeric_columns = {
        "s_no", "open", "high", "low", "close", "ltp",
        "close_ltp", "close_ltp_percent", "vwap", "vol",
        "prev_close", "turnover", "trans", "diff",
        "range", "diff_percent", "range_percent", "vwap_percent",
        "days_120", "days_180", "weeks_52_high", "weeks_52_low"
    }
    final_data = []
    for row in records:
        r = dict(zip(columns, row))
        # (Cleaning the numeric values with the method and saving it back into the dictionary. )
        for col in numeric_columns:
            r[col] = clean_number(r[col])
        final_data.append(r)
    return final_data


def save_to_databaseTable(parsed_data):

    engine = create_engine(CONNECTION_STRING)
    metadata = MetaData()
    metadata.reflect(bind=engine)  

    today_prices = metadata.tables["today_prices"]

    try:       #(Exception handling using Try-catch )
        with engine.begin() as conn:
            conn.execute(today_prices.insert(), parsed_data)
            print("Data inserted into today_prices table.")
    except Exception as e:
        print("Database error:", e)


def show_first_10_records():
    
    engine = create_engine(CONNECTION_STRING)
    metadata = MetaData(schema=DB_SCHEMA)
    metadata.reflect(bind=engine)

    today_prices = metadata.tables[f"{DB_SCHEMA}.today_prices"]

    with engine.connect() as conn:
        result = conn.execute(today_prices.select().limit(10)) #(Fetching data from the database table)
        rows = list(result)

    if not rows:
    
      print("\nNo records found!")
    else:
      columns = today_prices.columns.keys()
      print("\nFirst 10 Records:\n")
    
      for index, row in enumerate(rows, start=1):
        row_dict = {col: float(val) if isinstance(val, Decimal) else val #(Using Dictionary comprehension to display records.)
                    for col, val in zip(columns, row)}
        print(f"Record {index}: {row_dict}\n{'-'*50}")



if __name__ == "__main__":          #(Function calls.)

    print("\nFetching page...")
    soup = fetch_page()

    print("Extracting rows...")
    rows = extract_eachtable_rows(soup)

    print(" Parsing rows...")
    parsed_list = parse_eachTable_rows(rows)

    print(" Converting to dictionary format...")
    final_data = convert_list_to_dict(parsed_list)

    print(" Saving into database...")
    save_to_databaseTable(final_data)

    print(" Showing first 10 inserted records:")
    show_first_10_records()

    print("\n Scraping completed successfully!\n")

