FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

COPY table.py .

COPY constants.py .

COPY pokemon-info.csv .

CMD ["python", "main.py"]