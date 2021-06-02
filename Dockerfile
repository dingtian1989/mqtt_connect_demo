FROM python:latest

ENV PATH /usr/local/bin:$PATH

ADD ./app /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

CMD ["python", "/usr/src/app/mqtt_listner.py"]