# Key: State
# Value: Capital

states_to_capitals = {
  "Texas": "Austin",
  "New York": "Albany",
  "California": "Sacramento",
  "Michigan": "Lansing"
}

print(states_to_capitals["Michigan"])
print("---")

for key in states_to_capitals:
    print(key)
print("---")

for key, value in states_to_capitals.items():
    print(key + " | " + value)
