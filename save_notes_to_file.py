from datetime import date, datetime
import yaml


try:
    with open('filename.yaml', 'w', encoding='utf-8') as file:
        def save_notes_to_file():
            notizen = []  # создали пустой список

            while True:
                username = input('\tВведите имя пользователя: ')  # заполнение данных заметки
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
                    issue_date = input('\tВведите дату дедлайна (в формате день-месяц-год (20-12-2025)): ')
                    try:
                        date1 = datetime.strptime(issue_date, '%d-%m-%Y')  # смена данных на 'datetime.datetime'
                        break
                    except ValueError:
                        print('\tНе правильный формат даты')
                issue_date = date.strftime(date1, '%d-%m-%Y')

                created_date = date.today().strftime('%d-%m-%Y')  # текущая дата

                note1 = {'Имя пользователя': username, 'Заголовок': title, 'Описание': content, 'Статус': status,
                         'Дата создания': created_date, 'Дедлайн': issue_date}  # создание словаря

                notizen.append(note1)  # добавляем словарь в список notizen

                note_ = input('\tХотите добавить ещё одну заметку? (да/нет): ')
                if note_.lower() == 'да':
                    continue
                elif note_.lower() == 'нет':  # создаем условие для прекращения цикла
                    break
                else:
                    print('Число не подходит!')

            # сериализация данных списка заметок в формат yaml
            yaml.dump(notizen, file, sort_keys=False, indent=4, default_flow_style=False, allow_unicode=True)


        save_notes_to_file()

# Обработка возможных ошибок
except FileNotFoundError:
    print('\tФайл filename.yaml не найден! Создан новый файл.')
except UnicodeDecodeError:
    print('\tНе удалось декодировать файл filename.yaml!')
except PermissionError:
    print('\tОшибка доступа к файлу filename.yaml!')
except:
    print('\tЧто-то случилось при запуске!')
