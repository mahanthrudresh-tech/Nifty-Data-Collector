import time
from datetime import datetime

from fetcher import fetch_latest

print("NIFTY Collector Started...")

last_minute = -1

while True:

    now = datetime.now()

    # Market timings
    if (
        now.weekday() < 5 and
        (
            (now.hour == 9 and now.minute >= 15)
            or
            (9 < now.hour < 15)
            or
            (now.hour == 15 and now.minute <= 30)
        )
    ):

        # Every 5-minute candle
        if now.minute % 5 == 0 and now.minute != last_minute:

            fetch_latest()

            last_minute = now.minute

    time.sleep(1)