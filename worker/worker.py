from consumer import consume

def worker():
    consume("rabbitmq")

if __name__ == "__main__":
    worker()
