from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from router.schemas import ArticleRequestSchema, ArticleResponseSchema
from db.database import get_db
from db import db_article
from typing import List

router = APIRouter(
    prefix='/api/v1/article',
    tags=['article']
)


@router.post('', response_model=ArticleResponseSchema)
def create(request: ArticleRequestSchema, db: Session = Depends(get_db)):
    return db_article.create(db=db, request=request)


@router.get('/feed', response_model=List[ArticleResponseSchema])
def feed_initial_article(db: Session = Depends(get_db)):
    return db_article.db_feed(db)


@router.get('/all', response_model=List[ArticleResponseSchema])
def get_all_article(db: Session = Depends(get_db)):
    return db_article.get_all(db)


@router.get('/id/{article_id}', response_model=ArticleResponseSchema)
def get_article_by_id(article_id: int, db: Session = Depends(get_db)):
    return db_article.get_article_by_id(article_id=article_id, db=db)


