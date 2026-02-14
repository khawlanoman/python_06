
def validate_ingredients(ingredients: str) -> str:
    list = ["fire", "water", "earth", "air"]
    string = ingredients.split()
    for l in string:
        if l not in list:
            return (f"{ingredients} - INVALID")

    return (f"{ingredients} - VALID")
