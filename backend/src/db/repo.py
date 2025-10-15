from typing import Iterable, List
from sqlmodel import select
from src.db.session import get_session
from src.db.models import Recipe

def save_recipes(titles_and_steps: Iterable[tuple[str, str]], ingredients: list[str]) -> List[Recipe]:
    """Persist a list of recipes, return saved rows."""
    ing_csv = ",".join(ingredients)
    saved: List[Recipe] = []
    with get_session() as session:
        for idx, (title, steps_md) in enumerate(titles_and_steps, start=1):
            rec = Recipe(
                slug=f"gen_{idx}",
                title=title,
                ingredients_csv=ing_csv,
                steps_md=steps_md,
            )
            session.add(rec)
            saved.append(rec)
        session.commit()
        for rec in saved:
            session.refresh(rec)
    return saved

def list_recipes(limit: int = 20) -> List[Recipe]:
    with get_session() as session:
        stmt = select(Recipe).order_by(Recipe.id.desc()).limit(limit)
        return list(session.exec(stmt))
