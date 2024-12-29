from datetime import date, datetime

current_date = date.today().strftime('%d-%m-%Y')  # текущая дата
print('Текущая дата:', current_date)
current_date = datetime.strptime(current_date, '%d-%m-%Y')  # смена типа данных на 'datetime.datetime'
print(type(current_date))
while True:
    issue_date = input('Введите дату дедлайна (в формате день-месяц-год): ')
    try:
        date1 = datetime.strptime(issue_date, '%d-%m-%Y')  # смена данных на 'datetime.datetime'
        break
    except ValueError:
        print('Не правильный формат даты')
issue_date = date1
# issue_date = datetime.strptime(issue_date, '%d-%m-%Y')
if current_date < issue_date:  # создаем условие для получения дедлайна
    date_deadline = issue_date - current_date  # получаем остаток днкй до дедлайна
    print('До дедлайна осталось', date_deadline.days, 'дня.')
elif current_date > issue_date:  # создаем второе условие для получения дедлайна
    date_deadline2 = current_date - issue_date  # получем дни после истечения дедлайна
    print('Внимане! Дедлайн истек', date_deadline2.days, 'дней назад.')
