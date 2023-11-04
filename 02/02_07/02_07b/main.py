# Linear Search

my_list = [5, 6, 2, 4, 6, 0, 1]
ITEM = 2

def linear_search(item, listy):
    for index, value in enumerate(listy):
        if value == item:
            print(f"Index number: {index}")
            return True
    return False

print(linear_search(ITEM, my_list))

ITEM_INDEX = my_list.index(ITEM)
print(ITEM_INDEX)
