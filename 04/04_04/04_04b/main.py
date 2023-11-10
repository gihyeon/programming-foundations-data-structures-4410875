# frozonset is an immutable and hashable set
primary_colors = frozenset(["Red", "Blue", "Green"])
print(primary_colors)

COLOR = "Blue"

if COLOR in primary_colors:
    print(COLOR + " is primary color.")

# primary_colors.add('Yellow')

yellow = frozenset("Yellow")
print(yellow)

# Hashability
# Hashable frozenset
hashable_frozenset = frozenset({1, 2, 3})
print(hash(hashable_frozenset))

# Unhashable frozenset due to an unhashable element
# unhashable_frozenset = frozenset({1, 2, [3]})  # Lists are unhashable
# This would raise a TypeError because the frozenset is not hashable

# frozenset in set
frznset_in_set = set({1, 2, frozenset({3})})
print(frznset_in_set)

# frozenset in frozenset
frznset_in_frznset = frozenset({1, 2, frozenset({3})})
print(frznset_in_frznset)
print(len(frznset_in_frznset))
