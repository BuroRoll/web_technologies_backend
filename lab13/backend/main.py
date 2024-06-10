from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

import models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Разрешаем CORS запросы отовсюду для всех маршрутов.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/todoitems/", response_model=schemas.ToDoItem)
def create_todo_item(item: schemas.ToDoItemCreate, db: Session = Depends(get_db)):
    db_item = models.ToDoItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/todoitems/", response_model=List[schemas.ToDoItem])
def read_todo_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.ToDoItem).offset(skip).limit(limit).all()


@app.put("/todoitems/{item_id}", response_model=schemas.ToDoItem)
def update_todo_item(item_id: int, item: schemas.ToDoItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(models.ToDoItem).filter(models.ToDoItem.id == item_id).first()

    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.title = item.title
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item


@app.delete("/todoitems/{item_id}", response_model=schemas.ToDoItem)
def delete_todo_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.ToDoItem).filter(models.ToDoItem.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item
