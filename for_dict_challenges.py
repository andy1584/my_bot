# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
names = {name: 0 for name in sorted(list(set(student['first_name'] for student in students)))} # list для того, чтобы имена выводились в алфавитном порядке.
for i in students:
	names[i['first_name']] += 1
for i, j in names.items():
	print(i, '=', j)
print()

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
names = {name: 0 for name in set(student['first_name'] for student in students)}
for student in students:
	names[student['first_name']] += 1
max_quantity = max(names.values())
for name, quantity in names.items():
    if quantity == max_quantity:
        print('Самое частое имя среди учеников: ', name, '\n')


# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
ind = 1
for cl in school_students:
    names = {name: 0 for name in set(student['first_name'] for student in cl)}
    for student in cl:
    	names[student['first_name']]+=1
    max_quantity = max(names.values())
    for name, quantity in names.items():
        if quantity == max_quantity:
            print(f'Самое частое имя среди учеников в классе {ind}: ', name)
            break
    ind+=1
print()


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for cl in school:
    genders = [0, 0]
    for student in cl['students']:
        if is_male[student['first_name']]:
            genders[0] += 1
        else:
            genders[1] += 1
    print(f'В класе {cl["class"]} {genders[1]} девочки и {genders[0]} мальчика.')
print()


# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля':  False,
  'Олег': True,
  'Миша': True,
}
genders = []
for cl in school:
    cl_gender = {'класс': cl['class'], 'мальчики': 0, 'девочки': 0}
    for student in cl['students']:
        if is_male[student['first_name']]:
            cl_gender['мальчики'] += 1
        else:
            cl_gender['девочки'] += 1
    genders.append(cl_gender)
leaders = {'лидер по мальчикам': None, 'лидер по девочкам': None}
for cl_gender in genders:
    if cl_gender['мальчики'] == max(cl_gender['мальчики'] for cl_gender in genders):
        leaders['лидер по мальчикам'] = cl_gender['класс']
    if cl_gender['девочки'] == max(cl_gender['девочки'] for cl_gender in genders):
        leaders['лидер по девочкам'] = cl_gender['класс']
print(f'Больше всего мальчиков в классе {leaders["лидер по мальчикам"]}.')
print(f'Больше всего девочек в классе {leaders["лидер по девочкам"]}.')


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a