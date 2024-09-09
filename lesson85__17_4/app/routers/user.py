from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import User
from schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify


user_router = APIRouter(prefix='/user', tags=['user'])

@user_router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    return db.scalars(select(User).where(User.id >= 0)).all()

@user_router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    if db.scalars(select(User).where(User.id == user_id)).all() is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f'User ID={user_id} not exist')
    else:
        return db.scalars(select(User).where(User.id == user_id)).all()

    pass
@user_router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], crt_user: CreateUser):
    db.execute(insert(User).values(username=crt_user.username,
                                   firstname=crt_user.firstname,
                                   lastname=crt_user.lastname,
                                   age=crt_user.age,
                                   slug=slugify(crt_user.username)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'User create sucessful'}

@user_router.put('/update')
async def upate_user(db: Annotated[Session, Depends(get_db)], upd_user: UpdateUser, user_id: int):
    if db.scalars(select(User).where(User.id == user_id)).first() is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f'User ID={user_id} not exist')
    else:
        db.execute(update(User).where(User.id == user_id).values(firstname=upd_user.firstname,
                                                                 lastname=upd_user.lastname,
                                                                 age=upd_user.age))
        db.commit()
        return {'status_code': status.HTTP_200_OK,
                'transaction': 'User update successful!'}
    pass
@user_router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    if db.scalars(select(User).where(User.id == user_id)).first() is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f'User ID={user_id} not exist')
    else:
        db.execute(delete(User).where(User.id == user_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK,
                'transaction': 'User delete successful!'}
    pass
