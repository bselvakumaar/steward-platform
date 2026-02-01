
from fastapi import APIRouter

router = APIRouter()

@router.post("/users")
def create_user(email: str, risk_profile: str):
    return {"email": email, "risk_profile": risk_profile}
