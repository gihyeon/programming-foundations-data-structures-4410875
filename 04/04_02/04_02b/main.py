# Set: a collection of unique items; unordered, no duplicate elements

primary_colors = set(['Red', 'Blue', 'Green'])

print(primary_colors)

color = 'Yellow'

if color in primary_colors:
    print(color + " is a primary color")
else:
    print(color + " is not a primary color")

# Add an element to a set
letters = set(['A', 'B'])
letters.add('C')
letters.add('A')
print(letters)
