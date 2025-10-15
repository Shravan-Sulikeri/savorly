from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from src.db.repo import save_recipes


router = APIRouter(prefix="/recipes", tags=["recipes"])

# --- request / response models ---
class GenerateRequest(BaseModel):
    ingredients: List[str]

class Recipe(BaseModel):
    id: int
    title: str
    ingredients: List[str]
    steps_md: str

class GenerateResponse(BaseModel):
    recipes: List[Recipe]

# --- route ---
@router.post("/generate", response_model=GenerateResponse)
async def generate_recipes(req: GenerateRequest):
    styles = ["Bowl", "Stir-Fry", "Casserole"]
    titles_and_steps = [
        (f"{', '.join(req.ingredients)} {style}", "1) Toss everything.\n2) Season.\n3) Serve hot.")
        for style in styles
    ]

    # Save to database
    saved = save_recipes(titles_and_steps, req.ingredients)

    # Convert DB rows back to API models
    out = [
        Recipe(
            id=r.id,
            title=r.title,
            ingredients=r.ingredients_csv.split(","),
            steps_md=r.steps_md,
        )
        for r in saved
    ]
    return GenerateResponse(recipes=out)
