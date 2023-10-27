seating_chart = [
    ["Sarah", "Claire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

# Access to Lauren
# print(seating_chart[2][1])

# Display low and column no. for each students
for i, element in enumerate(seating_chart):
    for j, ele_val_inner_list in enumerate(element):
        print(f"{ele_val_inner_list} is in row {i+1}, col {j+1}")
