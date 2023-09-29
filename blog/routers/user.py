from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import database, oauth2, schemas
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"],
)

get_db = database.get_db


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
async def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get("/{id}", status_code=200, response_model=schemas.ShowUser)
async def show_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return user.show_user(id, db)
