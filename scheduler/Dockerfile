FROM python

WORKDIR /sample_app
COPY . /sample_app/

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./database.py .
COPY ./producer.py .
COPY  ./scheduler.py .

CMD ["python3", "-u", "scheduler.py"]
