# Tuples are immutable array-like structures

point = (2, 5)

x = point[0]
y = point[1]

print(x, y)

def cal_square_properties(length):
    area = length * length
    perimeter = length * 4
    return (area, perimeter)

result = cal_square_properties(2)
print("Area:", result[0])
print("Perimeter:", result[1])
