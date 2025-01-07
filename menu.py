from datetime import date, datetime

notizen = []


def main():
    while True:
        print('Меню действий:\n'
              '\t1. Создать новую заметку\n'
              '\t2. Показать все заметки\n'
              '\t3. Обновить заметку\n'
              '\t4. Удалить заметку\n'
              '\t5. Найти заметки\n'
              '\t6. Выйти из программы')

        user_ch = input('\tВыберите действие указав соответствующий номер: ')
        if user_ch == '1':
            add_a_note(notizen)
        elif user_ch == '2':
            display_notes(notizen)
        elif user_ch == '3':
            note1 = input('\t Введите имя пользователя или заголовок для обновления заметки: ')
            update_note(note1, notizen)
        elif user_ch == '4':
            note2 = input('\t Введите имя пользователя или заголовок для удаления заметки: ')
            delete_note(note2, notizen)
        elif user_ch == '5':
            note3 = input('\t Введите имя пользователя или заголовок для поиска заметки: ')
            search_note(note3, notizen)
        elif user_ch == '6':
            break
        else:
            print('\t Неверный выбор. Пожалуйста, выберите действие из списка.')




def add_a_note(notizen):
    while True:
        username = input('\t Введите имя пользователя: ')  # заполнение данных заметки
        title = input('\t Введите заголовок заметки: ')
        content = input('\t Введите описание заметки: ')
        status = '-'
        while True:  # создаем цикл и условие для татуса

            num_s = input('\t Выберите статус заметки, введя соответствующий номер: \n'
                          '\t1. новая\n'
                          '\t2. в процессе\n'
                          '\t3. выполнено\n ' )
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
        issue_date = date.strftime(date1, '%d-%m-%Y')

        created_date = date.today().strftime('%d-%m-%Y')  # текущая дата

        note1 = {'Имя': username, 'Заголовок': title, 'Описание': content, 'Статус': status,
                 'Дата создания': created_date, 'Дедлайн': issue_date}  # создание словаря

        notizen.append(note1)  # добовляем словарь в список notizen
        note_ = input('\t Хотите добавить ещё одну заметку? (да/нет): ')
        if note_.lower() == 'да':
            continue
        elif note_.lower() == 'нет':  # создаем условие для прекращения цикла
            main()




def display_notes(notizen):
    while True:
        if notizen == []:
            print('\t У вас нет сохранённых заметок.')
            break
        else:
            print('\t Список заметок:')
            for i, note_ in enumerate(notizen):
                print(f'\t______________\n'
                        f'Заметка №', i + 1)
                for j, k in note_.items():
                    print(f'\t{j}: {k}')
        main()




def update_note(note1, notizen):
    for note_1 in notizen:
        if note_1['Username'] == note1 or note_1['Title'] == note1:
            while True:
                print('Какие данные вы хотите обновить?\n'
                      '\t1. Username\n'
                      '\t2. Title\n'
                      '\t3. Content\n'
                      '\t4. Status\n'
                      '\t5. Issue_date\n'
                      '\t6. Выход')
                user_ch = input('Ваш выбор (введите число): ')
                if user_ch == '1':  # условия запуска функций для внесения изменений в заметку
                    replace_the_username(note_1, notizen)
                elif user_ch == '2':
                    replace_the_title(note_1, notizen)
                elif user_ch == '3':
                    replase_the_content(note_1, notizen)
                elif user_ch == '4':
                    replase_the_status(note_1, notizen)
                elif user_ch == '5':
                    replase_the_issue_date(note_1, notizen)
                elif user_ch == '6':
                    exit()
                    break
                else:
                    print('\t Неверное чисто! Введите заново.')
                    continue

def replace_the_username(note_1, notizen):
    for note_1 in notizen:# функция для внесения изменений в username
        name_1 = input('\t Введите новое значение для username: ')
        note_1['username'] = name_1

def replace_the_title(note_1, notizen):  # функция для внесения изменений в title
    title_1 = input('\t введите новое значение для title: ')
    note_1['title'] = title_1

def replase_the_content(note_1, notizen):  # функция для внесения изменений в content
    content_1 = input('\t Введите новое значение для content: ')
    note_1['content'] = content_1

def replase_the_status(note_1, notizen):  # функция для внесения изменений в status
    while True:  # создаем цикл и условие для татуса

        num_s = input('''\t Выберите статус заметки, введя соответствующий номер: 
            1. новая
            2. в процессе
            3. выполнено ''')
        if num_s == '1':  # создаем условие для оператора if
            status_1 = 'новая'
            break
        elif num_s == '2':  # создаем условие для оператора elif
            status_1 = 'в процессе'
            break
        elif num_s == '3':  # создаем условие для оператора elif
            status_1 = 'выполнено'
            break
        else:
            print('Число не подходит!')
    note_1['status'] = status_1

def replase_the_issue_date(note_1, notizen):  # функция для внесения изменений в issue_date
    while True:  # цикл для проверки правильного формата даты при вводе
        issue_date_1 = input('\t Введите дату дедлайна (в формате день-месяц-год): ')
        try:
            date1 = datetime.strptime(issue_date_1, '%d-%m-%Y')  # смена данных на 'datetime.datetime'
            break
        except ValueError:
            print('\t Не правильный формат даты')
    issue_date_1 = date.strftime(date1, '%d-%m-%Y')
    note_1['issue_date'] = issue_date_1




def delete_note(note2, notizen):
    for note_2 in notizen:
        if note_2['Username'] == note2 or note_2['Title'] == note2:
            print(f'Вы хотите удалить заметку {note_2} (да/нет):')
            if input().lower() == 'да':
                if note_2.lower() in notizen:
                    print(f'Вы удалили {notizen.pop(note_2.lower())}')
                else:
                    print('Заметка не найдена!')
            else:
                main()




def search_note(note3, notizen):
    for note_3 in notizen:
        if note_3['Username'] == note3 or note_3['Title'] == note3:
            print('\t Список заметок:')
            for i, note_3 in enumerate(notizen):
                print(f'\t______________\n'
                        f'Заметка №', i + 1)
                for j, k in note_3.items():
                    print(f'\t{j}: {k}')
        main()




if __name__ == '__main__':
    main()