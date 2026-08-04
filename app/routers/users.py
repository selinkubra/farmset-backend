from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from app.database import get_session
from app.models.user import NodeUser

router = APIRouter(prefix="/users", tags=["Users (Kullanıcılar)"])

@router.post("/", response_model=NodeUser)
def create_user(user: NodeUser, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.get("/", response_model=List[NodeUser])
def read_users(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    users = session.exec(select(NodeUser).offset(skip).limit(limit)).all()
    return users
