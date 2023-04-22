FROM python:3.10

WORKDIR /app

COPY api/requirements.txt .

COPY api/pokemon_api .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "pokemon_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
