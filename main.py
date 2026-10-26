from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Krishna Agro Center API", version="1.0.0")


class Student(BaseModel):
    name: str
    age: int
    skills: List[str]


@app.get("/")
def home():
    return {"message": "Welcome to Krishna Agro Center API"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}! Welcome."}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/student")
def create_student(student: Student):
    return {"message": "Student received", "data": student}