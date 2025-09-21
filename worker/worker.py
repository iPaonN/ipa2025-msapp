from consumer import consume
from os

def worker():
    consume(os.getenv("RABBITMQ_HOST"))


if __name__ == "__main__":
    worker()
