from pydantic import BaseModel
from typing import List


class ArticleRequestSchema(BaseModel):
    title: str
    sku: str
    description: str
    description_long: str
    owner_id: int


class UserRequestSchema(BaseModel):
    username: str
    email: str
    password: str
    is_admin: bool


class ArticleResponseSchema(ArticleRequestSchema):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserResponseSchema(UserRequestSchema):
    id: int
    created_article: List[ArticleResponseSchema] = []

    class Config:
        orm_mode = True
