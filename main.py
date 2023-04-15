from fastapi import FastAPI

# start api: uvicorn main:app --reload 

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}