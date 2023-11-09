# Set: a collection of unique items; unordered, no duplicate elements

primary_colors = set(["Red", "Blue", "Green"])

print(primary_colors)

COLOR = "Yellow"

if COLOR in primary_colors:
    print(COLOR + " is a primary color")
else:
    print(COLOR + " is not a primary color")

# Add an element to a set
letters = set(["A", "B"])
letters.add("C")
letters.add("A")
print(letters)
