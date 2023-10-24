''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

student_pet_count_list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

NUM_OF_STUDENTS = len(student_pet_count_list)
print("Number of students: ", NUM_OF_STUDENTS)

ITEM_AT_INDEX_THREE = student_pet_count_list[3]
print("Item at index three (4th item): ", ITEM_AT_INDEX_THREE)

ITEM_THREE_FROM_BACK = student_pet_count_list[-3]
print("Item three from back: ", ITEM_THREE_FROM_BACK)

SUM = 0
for individual_pet_count in student_pet_count_list:
    SUM = SUM + individual_pet_count
print("Sum of pet counts: ", SUM)

# average = sum / number of items
AVERAGE = SUM / NUM_OF_STUDENTS
print("Average pet count per student: ", AVERAGE)
