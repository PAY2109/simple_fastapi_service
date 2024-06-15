from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from utils import validate_payload
from deposit_service import calculate_deposit


app = FastAPI()


class DepositInfo(BaseModel):
    date: str
    periods: int
    amount: int
    rate: float


@app.post("/deposit/calculate/")
async def get_deposit_info(deposit_info: DepositInfo):
    deposit_info_dict = deposit_info.dict()
    # print(deposit_info_dict)
    if validate_payload(payload=deposit_info_dict):
        deposit = calculate_deposit(payload=deposit_info_dict)
        return deposit
    else:
        raise HTTPException(
            status_code=400,
            detail={"error": "Invalid input"}
        )
