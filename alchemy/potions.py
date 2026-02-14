import  alchemy.elements
def healing_potion() -> str:
    return (f"Healing potion brewed with {alchemy.elements.create_fire()}, {alchemy.elements.create_water()}")


def strength_potion() -> str:
    return (f"Strength potion brewed with {alchemy.elements.create_earth()}, {alchemy.elements.create_fire()}")


def invisibility_potion() -> str:
    return (f"Invisibility potion brewed with {alchemy.elements.create_air()}, {alchemy.elements.create_water()}")


def wisdom_potion() -> str:
    return (f"Wisdom potion brewed with all elements: {alchemy.elements.create_fire(), alchemy.elements.create_water(), alchemy.elements.create_earth(), alchemy.elements.create_air()}")