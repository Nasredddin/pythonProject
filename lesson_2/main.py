print('Здравствуйте, как вас зовут?')
a = input()
print('Добро пожаловать,' + a)
print('Как твои дела?')
a = input()
if 'хорошо' in a or 'нормально' in a:
    print('молодцом, так держать')
elif 'плохо' in a or 'ужасно' in a:
    print('жаль тебя, все будет ок')
else:
    print('ERROR')