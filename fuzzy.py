from thefuzz import fuzz

a = "Assassin's Creed III"
b = "Assassins Creed III"

print(f"Ratio: {fuzz.ratio(a, b)}")
print(f"Partial Ratio: {fuzz.partial_ratio(a, b)}")