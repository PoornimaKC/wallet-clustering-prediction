from pydantic import BaseModel

class UserInput(BaseModel):
    num_transactions: float
    total_amount: float
    avg_transaction_amount: float
    num_deposits: float
    num_borrows: float
    num_repayments: float
    num_redeems: float
    num_liquidations: float
    active_days: float
    days_between_tx: float
