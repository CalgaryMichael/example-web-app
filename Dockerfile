FROM python:3.9-slim
RUN pip install -U pip

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt

COPY main.py /app
COPY webapp /app/webapp/

CMD ["python3", "-m", "main"]
