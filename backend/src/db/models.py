from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    pass_hash: str

    favorites: List["Favorite"] = Relationship(back_populates="user")

class Recipe(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    slug: str = Field(index=True)  # simple identifier like "rec_1_2025"
    title: str
    ingredients_csv: str
    steps_md: str

    favorites: List["Favorite"] = Relationship(back_populates="recipe")

class Favorite(SQLModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    recipe_id: int = Field(foreign_key="recipe.id", primary_key=True)

    user: User = Relationship(back_populates="favorites")
    recipe: Recipe = Relationship(back_populates="favorites")
