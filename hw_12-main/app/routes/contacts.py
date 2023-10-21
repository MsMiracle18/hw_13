from fastapi import Depends, APIRouter, HTTPException, Request
from fastapi.middleware.throttle import Throttle, SimpleThrottleLimiter
from sqlalchemy.orm import Session
from . import oauth2  
from ..models import User  
from fastapi import HTTPException

router = APIRouter()

@router.get("/get_birthday")
async def get_birthday(today, end_date, db: Session, current_user: User = Depends(oauth2.get_current_user)):
    if current_user.username == user_with_birthday:
        users = db.query(User).all()
        return users
    else:
        raise HTTPException(status_code=403, detail="Access forbidden")

app = FastAPI()

# обмежити кількість запитів до 10 на хвилину на IP-адресу
app.add_middleware(Throttle, throttler=SimpleThrottleLimiter(rate="10/minute"))

@app.get("/contacts/")
async def get_contacts(request: Request):
    return {"message": "Contacts retrieved"}

