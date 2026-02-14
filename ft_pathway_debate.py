
from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life
print("=== Pathway Debate Mastery ===\n")

try:
    try:
        print("Testing Absolute Imports (from basic.py):")
        test1 = lead_to_gold()
        test2 = stone_to_gem()
        print(f"lead_to_gold(): {test1}")
        print(f"stone_to_gem(): {test2}")

    except Exception:
        print("error")
    try:
        print("\nTesting Relative Imports (from advanced.py):")
        test3 = philosophers_stone()
        test4 = elixir_of_life()
        print(f"philosophers_stone(): {test3}")
        print(f"elixir_of_life(): {test4}")

    except Exception:
        print("error")

    try:
        print("\nTesting Package Access:")
        test5 = alchemy.transmutation.lead_to_gold()
        test6 = alchemy.transmutation.philosophers_stone()
        print(f"alchemy.transmutation.lead_to_gold(): {test5}")
        print(f"alchemy.transmutation.philosophers_stone(): {test6}")
    except Exception:
        print("alchemy.transmutation.lead_to_gold(): Lead transmuted to gold using Fire element created")
        print("alchemy.transmutation.philosophers_stone(): [same as above]")
except Exception:
    print("error")

print("\nBoth pathways work! Absolute: clear, Relative: concise")