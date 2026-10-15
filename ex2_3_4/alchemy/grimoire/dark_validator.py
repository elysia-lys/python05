from .dark_spellbook import dark_spell_allowed_ingredients  # noqa: F401


def dark_validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()

    for i in allowed:
        if i in ingredients.lower():
            return (f"{ingredients} - VALID ")
    return (f"{ingredients} - INVALID")
