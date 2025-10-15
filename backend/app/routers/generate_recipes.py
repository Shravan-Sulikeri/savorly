from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import List

router = APIRouter(prefix="/api", tags=["recipes"])

class GenerateRequest(BaseModel):
    pantry_items: List[str] = Field(
        default_factory=list,
        description="List of items, e.g. ['eggs','spinach']"
    )

class Recipe(BaseModel):
    title: str
    ingredients: List[str]
    steps_md: str

class GenerateResponse(BaseModel):
    recipes: List[Recipe]

@router.post("/generate_recipes", response_model=GenerateResponse)
def generate_recipes(req: GenerateRequest):
    items = [i.strip() for i in req.pantry_items if i.strip()]
    base = ", ".join(items) if items else "your pantry"
    fake = [
        Recipe(
            title=f"Quick {base} Bowl",
            ingredients=items or ["(add items)"],
            steps_md="1) Toss everything in a pan.\n2) Season to taste.\n3) Serve warm."
        ),
        Recipe(
            title=f"Cozy {base} Stir-Fry",
            ingredients=items or ["(add items)"],
            steps_md="1) Sauté base.\n2) Add sauce.\n3) Enjoy."
        ),
        Recipe(
            title=f"Baked {base} Casserole",
            ingredients=items or ["(add items)"],
            steps_md="1) Layer in dish.\n2) Bake 15–20 min.\n3) Rest and serve."
        ),
    ]
    return GenerateResponse(recipes=fake)

