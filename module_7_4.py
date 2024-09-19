
team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 7
team2_num = 5
score1 = 44
score2 = 42
team1_time = 24
team2_time = 26


print('В команде %s участников: %s !' % (team1, team1_num))
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

print('Команда {} решила задач: {}!'.format(team2, score2))
print('{} решили задачи за {} мин.!'.format(team1, team1_time))

tasks_total = score1 + score2
time_avg = (score1 + score2)/(team1_time + team2_time)
time_avg = round(time_avg, 2)
print(f'Команды решили {score1} и {score2} задач')
if score1 > score2 or score1 == score2 and team1_time > team2_time:
    print(f'Результат битвы: победа команды {team1} !')
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    print(f'Результат битвы: победа команды {team2} !')
else:
    print(f'Боевая ничья!')

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} минуты на задачу')






