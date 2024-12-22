from datetime import date, datetime

def create_note():
    notizen = []  # создали пустой список
    while True:
        username = input('\t Введите имя пользователя: ')  # заполнение данных заметки
        title = input('\t Введите заголовок заметки: ')
        content = input('\t Введите описание заметки: ')
        status = '-'
        while True:  # создаем цикл и условие для татуса

            num_s = input('''\t Выберите статус заметки, введя соответствующий номер: 
                1. новая
                2. в процессе
                3. выполнено ''')
            if num_s == '1':  # создаем условие для оператора if
                status = 'новая'
                break
            elif num_s == '2':  # создаем условие для оператора elif
                status = 'в процессе'
                break
            elif num_s == '3':  # создаем условие для оператора elif
                status = 'выполнено'
                break
            else:
                print('Число не подходит!')

        while True:  # цикл для проверки правильного формата даты при вводе
            issue_date = input('\t Введите дату дедлайна (в формате день-месяц-год): ')
            try:
                date1 = datetime.strptime(issue_date, '%d-%m-%Y')  # смена данных на 'datetime.datetime'
                break
            except ValueError:
                print('\t Не правильный формат даты')
        issue_date = date1

        created_date = date.today().strftime('%d-%m-%Y')  # текущая дата
        #created_date = datetime.strptime(created_date, '%d-%m-%Y')  # смена типа данных на 'datetime.datetime'

        note1 = {'Имя': username, 'Заголовок': title, 'Описание': content, 'Статус': status,
                 'Дата создания': created_date, 'Дедлайн': issue_date}  # создание словаря

        notizen.append(note1)  # добовляем словарь в список notizen

        note_ = input('\t Хотите добавить ещё одну заметку? (да/нет): ')
        if note_.lower() == 'да':
            continue
        elif note_.lower() == 'нет':  # создаем условие для прекращения цикла
            break


    for i in notizen:
        for key, value in i.items():  # анализируем список ивыводим список заметок
            print(f'{key}: {value}')

create_note()