FROM python:3.10

WORKDIR /app

COPY requirements.txt .

COPY pokemon_api .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "pokemoan_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
