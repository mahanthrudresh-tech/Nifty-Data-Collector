import sqlite3
import pandas as pd

conn = sqlite3.connect("data/nifty.db")

df = pd.read_sql_query("SELECT * FROM nifty_5min", conn)

print(df)

conn.close()