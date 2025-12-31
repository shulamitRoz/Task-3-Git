from fastapi import FastAPI
import json
import uuid

from pydantic import BaseModel

class Animal(BaseModel):
    name: str
    species: str
    age: int
    color: str

app = FastAPI()
FILE = "data.json"



@app.post("/add")
def add_payload(payload: dict):
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    payload["id"] = str(uuid.uuid4())

    data.append(payload)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
    
    return {
        "message": "Payload saved",
        "id": payload["id"]
    }

@app.get("/")
def get_last_payloads():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    return data[-10:]