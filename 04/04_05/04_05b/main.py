"""Problem: create a program that determines whether a piece of text has only unique characters"""

def has_unique_characters(data):
    unique_data = set(data)
    return len(unique_data) == len(data)

print(has_unique_characters("sample"))
print(has_unique_characters("hello world"))
print(has_unique_characters("linkedin"))
print(has_unique_characters("python"))
