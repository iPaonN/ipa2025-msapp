FROM python

WORKDIR /sample_app
COPY . /sample_app/

RUN pip install -r /sample_app/requirements.txt

COPY . .

CMD ["python3", "-u" ,"worker.py"]
