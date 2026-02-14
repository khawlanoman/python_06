from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell
print("\n=== Circular Curse Breaking ===\n")
try:
    try:
        print("Testing ingredient validation:")
        value1 = "fire"
        test1 = validate_ingredients(value1)
        print(f'validate_ingredients("{value1}"): {test1}')
        value2 = "dragon scales"
        test2 = validate_ingredients(value2)
        print(f'validate_ingredients("{value2}"):{test2}')
    except Exception:
        print("error")
    try:
        print("\nTesting spell recording with validation:")
        spell = "Fireball"
        ingredient = "fire air"
        value3 = record_spell(spell, ingredient)
        print(f'record_spell("{spell}", "{ingredient}"):{value3}')
        spell1 = "Dark Magic"
        ingredient1 ="shadow"
        value3 = record_spell(spell1, ingredient1)
        print(f'record_spell("{spell1}", "{ingredient1}"):{value3}')  
    except Exception:
        print("error")

    try:
        print("\nTesting late import technique:")
        spell = "Lightning"
        value = "air"
        value3 = record_spell(spell, value)
        print(f'record_spell("{spell}", "{value}"):{value3}')
    except Exception:
        print("ERROR")
except Exception:
    print("error")
        
print("\nCircular dependency curse avoided using late imports!")
print("All spells processed safely!")