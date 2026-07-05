import sqlite3

conn = sqlite3.connect("data/nifty.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS nifty_5min(

timestamp TEXT PRIMARY KEY,

open REAL,

high REAL,

low REAL,

close REAL,

volume INTEGER

)

""")

conn.commit()

conn.close()