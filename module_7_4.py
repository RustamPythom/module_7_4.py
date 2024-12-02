team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

str_1 = "В команде Мастера кода участников: %s!" % team1_num
str_2 = "Итого сегодня в командах участников: %s и %s!" % (team1_num,team2_num)

str_3 = "Команда Волшебники данных решила задач:{}!". format(score_2)
str_4 = "Волшебники данных решили задачи за {:.1f} c!".format(team1_time)

str_5 = f"Команды решили {score_1} и {score_2}"
str_6 = f"Результат битвы: {challenge_result}"
str_7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"

print(str_1)
print(str_2)
print(str_3)
print(str_4)
print(str_5)
print(str_6)
print(str_7)


