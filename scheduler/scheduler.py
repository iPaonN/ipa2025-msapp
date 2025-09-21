import time

from producer import produce

from bson import json_util
from database import get_router_info
import os


def scheduler():

    INTERVAL = 300.0
    next_run = time.monotonic()
    count = 0
    host = os.getenv("RABBITMQ_HOST")

    while True:
        now = time.time()
        now_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
        ms = int((now - int(now)) * 1000)
        now_str_with_ms = f"{now_str}.{ms:03d}"
        print(f"[{now_str_with_ms}] scheduler is running... {count}")

        try:
            for data in get_router_info():
                print("Data:", data)
                body_bytes = json_util.dumps(data).encode("utf-8")
                print("Body bytes:", body_bytes)
                produce("rabbitmq", body_bytes)
        except Exception as e:
            print(e)
            time.sleep(3)
        count += 1
        next_run += INTERVAL
        time.sleep(max(0.0, next_run - time.monotonic()))


if __name__ == "__main__":
    scheduler()
