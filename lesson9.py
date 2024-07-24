# ####### Дополнительное практическое задание по модулю: Базовые структуры данных
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades[0] = sum(grades[0])/len(grades[0])
grades[1] = sum(grades[1])/len(grades[1])
grades[2] = sum(grades[2])/len(grades[2])
grades[3] = sum(grades[3])/len(grades[3])
grades[4] = sum(grades[4])/len(grades[4])
print('Средняя оценка Аарона:',grades[0])
print('Средняя оценка Бильбо>:',grades[1])
print('Средняя оценка Джонни:',grades[2])
print('Средняя оценка Хендрика:',grades[3])
print('Средняя оценка Стива:',grades[4])
student_list = students
student_list = sorted(student_list)

Sudent_grades_dict = dict()
Sudent_grades_dict.update({
    student_list[0]:grades[0],
    student_list[1]:grades[1],
    student_list[2]:grades[2],
    student_list[3]:grades[3],
    student_list[4]:grades[4]})
print(Sudent_grades_dict)
