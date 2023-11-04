my_list = [1, 7, 3]
my_list_sorted_asc = sorted(my_list)
my_list_sorted_des = sorted(my_list, reverse=True)

print(my_list_sorted_asc)
print(my_list_sorted_des)

student_grades = [('Sarah', 83), ('Mike', 90), ('Abbie', 78)]
student_grades_sorted_alpha = sorted(student_grades)
student_grades_sorted_score_des = sorted(student_grades, key=lambda x:x[1], reverse=True)

print(student_grades_sorted_alpha)
print(student_grades_sorted_score_des)
