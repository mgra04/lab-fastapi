from fastapi import FastAPI
from students.router import router

app = FastAPI()

app.include_router(router, prefix="/students")
