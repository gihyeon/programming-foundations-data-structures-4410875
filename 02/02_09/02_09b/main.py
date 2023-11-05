def find_second_smallest(my_list):
    "Return the second samllest item in a list of integers"
    if len(my_list) > 1:
        my_list_sorted = sorted(my_list)
        return my_list_sorted[1]
    return None

print(find_second_smallest([5, 8, 3, 2, 6]))
