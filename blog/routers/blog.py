from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import database, oauth2, schemas
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"],
)

get_db = database.get_db


@router.post("/{id}", status_code=status.HTTP_201_CREATED)
async def create(
    id: int,
    request: schemas.Blog,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.create(id, request, db)


@router.get("/", status_code=200, response_model=list[schemas.ShowBlog])
async def all(
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.get(db)


@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
async def show(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.show(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update(
    id: int,
    request: schemas.Blog,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.update(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def destroy(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.destroy(id, db)
