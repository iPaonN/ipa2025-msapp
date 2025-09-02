import time, pika

from producer import product

def scheduler():
    count = 0
    while True:
        now = time.time()
        now_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
        print(f"[{now_str}] scheduler is running... {count}")

        try:
            product("localhost", "192.168.1.44")
        except Exception as e:
            print(e)
            time.sleep(3)
        count += 1
        time.sleep(10)

if __name__ == "__main__":
    scheduler()

