# ДДомашнее задание по теме "Форматирование строк"

# Входные данные
team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'

team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# use %s
print('В команде "%s" - %s участников'  % (team1_name, team1_num))
print('В команде "%s" - %s участников'  % (team2_name, team2_num))
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))

#use format()
print('Команда "{}" решила задач: {}'.format(team1_name,score1))
print('Команда "{}" решила задач: {}'.format(team2_name,score2))
print('"{}" решили задачи за {}'.format(team1_name,team1_time))
print('"{}" решили задачи за {}'.format(team2_name,team2_time))

# use f string
print(f'Команды решили {score1} и {score2} задачи')
if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = f'Победа команды "{team1_name}"'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = f'Победа команды "{team2_name}"'
else:
    result = 'Ничья!'
print(f'Результат: {result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем {(team1_time+team2_time) / tasks_total} секунды на задачу!.')
