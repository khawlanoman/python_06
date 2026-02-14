from .validator import validate_ingredients

def record_spell(spell_name: str, ingredients: str) -> str:
    if (validate_ingredients(ingredients) == f"{ingredients} - VALID"):
        return (f"Spell recorded: {spell_name} ({ingredients} - VALID)")
    elif (validate_ingredients(ingredients) == f"{ingredients} - INVALID"):
        return (f"Spell recorded: {spell_name} ({ingredients} - INVALID)")