from fastapi import HTTPException, status
from router.schemas import ArticleRequestSchema
from sqlalchemy.orm.session import Session
from .articles_feed import articles

from db.models import DbArticle


def db_feed(db: Session):
    new_article_list = [DbArticle(
        title=article["title"],
        sku=article["sku"],
        description=article["description"],
        description_long=article["description_long"],
        owner_id=article["owner_id"]
    ) for article in articles]
    db.query(DbArticle).delete()
    db.commit()
    db.add_all(new_article_list)
    db.commit()
    return db.query(DbArticle).all()


def create(db: Session, request: ArticleRequestSchema) -> DbArticle:
    new_article = DbArticle(
        name=request.name,
        sku=request.sku,
        description=request.description,
        description_long=request.description_long,
        owner_id=request.owner_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_all(db: Session) -> list[DbArticle]:
    return db.query(DbArticle).all()


def get_article_by_id(article_id: int, db: Session) -> DbArticle:
    article = db.query(DbArticle).filter(DbArticle.id == article_id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Article with id = {id} not found')
    return article


def get_article_by_category(category: str, db: Session) -> list[DbArticle]:
    article = db.query(DbArticle).filter(DbArticle.category == category).all()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Article with category = {id} not found')
    return article
