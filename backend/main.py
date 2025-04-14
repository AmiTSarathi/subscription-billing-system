
from fastapi import FastAPI
from billing_engine import generate_user_bill
from mock_db import USERS
from datetime import datetime

app = FastAPI()

@app.get("/bill/{user_id}")
def get_user_bill(user_id: str):
    today = datetime.today()
    user = next((u for u in USERS if u["user_id"] == user_id), None)
    if not user:
        return {"error": "User not found"}
    bill = generate_user_bill(user, today)
    return bill
