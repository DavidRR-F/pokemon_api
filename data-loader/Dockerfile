FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY main.py .

COPY table.py .

COPY constants.py .

COPY pokemon-data .

CMD ["python", "main.py"]