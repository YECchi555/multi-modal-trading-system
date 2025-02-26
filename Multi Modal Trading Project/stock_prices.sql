CREATE TABLE IF NOT EXISTS stock_prices (
    ticker TEXT,
    date TEXT,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume INTEGER,
    PRIMARY KEY(ticker, date)
);

import sqlite3
import pandas as pd

conn = sqlite3.connect('market_data.db')
query = "SELECT * FROM stock_prices WHERE ticker='AAPL'"
df = pd.read_sql(query, conn)
print(df.head())pad