from datetime import date, datetime
import json

try:
    with open('filename3.json', 'w', encoding='utf-8') as file:
        notizen = []  # создали пустой список


        def save_notes_to_file(notes, filename):

            while True:  # цикл заполнение данных заметки
                username = input('\tВведите имя пользователя: ')
                title = input('\tВведите заголовок заметки: ')
                content = input('\tВведите описание заметки: ')
                status = '-'

                while True:  # создаем цикл и условие для статуса
                    num_s = input('''\tВыберите статус заметки, введя соответствующий номер: 
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
                    issue_date = input('\tВведите дату дедлайна (в формате день-месяц-год (20-01-2024)): ')
                    try:
                        date1 = datetime.strptime(issue_date, '%d-%m-%Y')  # смена данных на 'datetime.datetime'
                        break
                    except ValueError:
                        print('\tНе правильный формат даты')
                issue_date = date.strftime(date1, '%d-%m-%Y')

                created_date = date.today().strftime('%d-%m-%Y')  # текущая дата

                note1 = {'Имя пользователя': username, 'Заголовок': title, 'Описание': content, 'Статус': status,
                         'Дата создания': created_date, 'Дедлайн': issue_date}  # создание словаря

                notizen.append(note1)  # добовляем словарь в список notizen

                note_ = input('\tХотите добавить ещё одну заметку? (да/нет): ')
                if note_.lower() == 'да':
                    continue
                elif note_.lower() == 'нет':
                    break

            result_ = json.dump(notizen, file, indent=4, ensure_ascii=False)
            print(result_)


        save_notes_to_file(notizen, file)
# Обработка возможных ошибок
except FileNotFoundError:
    print('файл не найден! Создан новый файл.')
except UnicodeDecodeError:
    print('\tНе удалось декодировать файл!')
except PermissionError:
    print('\tОшибка доступа к файлу!')
except:
    print('\tЧто-то случилось при запуске!')
