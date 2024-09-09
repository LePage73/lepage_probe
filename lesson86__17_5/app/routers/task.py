from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import Task, User
from schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify


router = APIRouter(prefix='/task', tags=['task'])

@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    return db.scalars((select(Task).where(Task.id >= 0))).all()
    pass
@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    if db.scalars(select(Task).where(Task.id == task_id)).all() is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f'Task ID={task_id} not exist')
    else:
        return db.scalars(select(Task).where(Task.id == task_id)).all()
    pass
@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], crt_task: CreateTask, user_id: int):
    if db.scalars(select(User).where(User.id == user_id)).first() is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f'User ID={user_id} not exist')

    db.execute(insert(Task).values(title=crt_task.title,
                                   content=crt_task.content,
                                   priority=crt_task.priority,
                                   user_id=user_id,
                                   slug=slugify(crt_task.title)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Task create successful!'}

    pass
@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], upd_task: UpdateTask, task_id: int):
    if db.scalars(select(Task).where(Task.id == task_id)).all() is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f'Task ID={task_id} not exist')
    db.execute(update(Task).where(Task.id == task_id).values(title=upd_task.title,
                                                             content=upd_task.content,
                                                             priority=upd_task.priority))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Task update successful!'}
    pass
@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    if db.scalars(select(Task).where(Task.id == task_id)).all() is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f'Task ID={task_id} not exist')
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_200_OK,
            'transaction': 'Task delete successful!'}

    pass
