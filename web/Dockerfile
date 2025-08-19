FROM python
RUN pip install flask
RUN pip install pymongo
COPY  ./static ./static
COPY  ./templates ./templates/
COPY  sample_app.py .

EXPOSE 8080

CMD python ./sample_app.py
