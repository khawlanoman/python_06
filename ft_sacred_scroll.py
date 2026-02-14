import alchemy
from alchemy import elements, __author__, __version__


print("=== Sacred Scroll Mastery ===\n")
print("Testing direct module access:")

try:
    test1 = elements.create_fire()
    test2 = elements.create_water()
    test3 = elements.create_earth()
    test4 = elements.create_air()
    print(f"alchemy.elements.create_fire():{test1}")
    print(f"alchemy.elements.create_water():{test2}")
    print(f"alchemy.elements.create_earth():{test3}")
    print(f"alchemy.elements.create_air():{test4}")
except Exception as e:
    print(f"error:{e}")


print("\nTesting package-level access (controlled by __init__.py):")
try:
    test1 = alchemy.create_fire()
    test2 = alchemy.create_water()
    print(f"alchemy.elements.create_fire():{test1}")
    print(f"alchemy.elements.create_water():{test2}")
    try:
        test3 = alchemy.create_earth()
        print(f"alchemy.elements.create_earth(): {test3}")
    except AttributeError:
        print("alchemy.elements.create_earth(): AttributeError - not exposed")
    try:
        test4 = alchemy.create_air()
        print(f"alchemy.elements.create_air():{test4}")
    except AttributeError:
        print("alchemy.elements.create_air(): AttributeError - not exposed")
except Exception as e:
    print(f"error:{e}")

print("\nPackage metadata:")
print(f"Version : {__version__}")
print(f"Author : {__author__}")
