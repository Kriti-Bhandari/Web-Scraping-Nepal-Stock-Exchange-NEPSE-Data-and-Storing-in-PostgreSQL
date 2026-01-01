from sqlalchemy import create_engine, MetaData, Table, Column, Integer, BigInteger, Numeric, String, Text, TIMESTAMP, func


DB_USER = "postgres" 
DB_PASSWORD = "kriti"
HOST = "localhost"
PORT = 5432
DB_NAME = "postgres"
DB_SCHEMA = "public"

CONNECTION_STRING = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

def create_table():
    engine = create_engine(CONNECTION_STRING, echo=False)
    metadata = MetaData()

    today_prices = Table(
        "today_prices",
        metadata,
                Column("id", Integer, primary_key=True, autoincrement=True),
    Column("s_no", Integer, nullable=True),
    Column("symbol", String(32), nullable=False, index=True),
    Column("conf", String(8), nullable=True),
    Column("open", Numeric, nullable=True),
    Column("high", Numeric, nullable=True),
    Column("low", Numeric, nullable=True),
    Column("close", Numeric, nullable=True),
    Column("ltp", Numeric, nullable=True),

    Column("close_ltp", Numeric, nullable=True),
    Column("close_ltp_percent", Numeric, nullable=True),

    Column("vwap", Numeric, nullable=True),
    Column("vol", BigInteger, nullable=True),

    Column("prev_close", Numeric, nullable=True),
    Column("turnover", Numeric, nullable=True),
    Column("trans", Integer, nullable=True),
    Column("diff", Numeric, nullable=True),
    Column("range", Numeric, nullable=True),
    Column("diff_percent", Numeric, nullable=True),
    Column("range_percent", Numeric, nullable=True),
    Column("vwap_percent", Numeric, nullable=True),

    Column("days_120", Numeric, nullable=True),
    Column("days_180", Numeric, nullable=True),
    Column("weeks_52_high", Numeric, nullable=True),
    Column("weeks_52_low", Numeric, nullable=True),
    Column("scraped_at", TIMESTAMP(timezone=True), server_default=func.now(), nullable=False),
)

    metadata.create_all(engine)
    print("Table created sucessfully.")

if __name__ == "__main__":
    create_table()