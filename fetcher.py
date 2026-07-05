import sqlite3
import yfinance as yf


def fetch_latest():

    ticker = yf.Ticker("^NSEI")

    df = ticker.history(
        period="1d",
        interval="5m"
    )

    if df.empty:
        print("No data found.")
        return

    conn = sqlite3.connect("data/nifty.db")
    cursor = conn.cursor()

    inserted = 0

    for timestamp, row in df.iterrows():

        cursor.execute("""
            INSERT OR IGNORE INTO nifty_5min
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            str(timestamp),
            float(row["Open"]),
            float(row["High"]),
            float(row["Low"]),
            float(row["Close"]),
            int(row["Volume"])
        ))

        # rowcount = 1 means inserted
        if cursor.rowcount == 1:
            inserted += 1

    conn.commit()
    conn.close()

    print(f"Added {inserted} new candle(s).")