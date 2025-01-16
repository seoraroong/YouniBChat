from fastapi import FastAPI
from backend.app.routers import users  # users 모듈을 가져오기

app = FastAPI()

app.include_router(users.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Hello, YouniBChat!"}