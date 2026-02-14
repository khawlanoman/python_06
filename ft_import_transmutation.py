import alchemy.elements
from alchemy.elements import create_fire
from alchemy.potions import healing_potion as heal
from alchemy.potions import strength_potion
from alchemy.elements import create_fire, create_water
print("\n=== Import Transmutation Mastery ===\n")

try:
    try:
        print("Method 1 - Full module import:")
        test1 = create_fire()
        print(f"alchemy.elements.create_fire(): {test1}")
    except:
        print("error")
    try:
        print("\nMethod 2 - Specific function import:")
        test2 = create_water()
        print(f"create_water(): {test2}")
    except:
        print("error")
    try:
       print("\nMethod 3 - Aliased import:") 
       method3 = heal()
       print(f"heal(): {method3}")
    except:
        print("ERROR") 

    try:
        print("\nMethod 4 - Multiple imports:")
        method4_1 = alchemy.elements.create_earth()
        method4_2 = alchemy.elements.create_air()
        print(f"create_earth(): {method4_1}")
        print(f"create_air(): {method4_2}")
        print(f"strength_potion(): {strength_potion()}")
    except Exception:
        print("error")
except Exception as e:
    print(f"error:{e}")


print("\nAll import transmutation methods mastered!")
  
    
   
   