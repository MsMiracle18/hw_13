from fastapi import Depends, APIRouter
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
