from datetime import date, datetime

print('Текущие данные заметки:')
note1 = {'username': 'Имя', 'title': 'Заголовок', 'content': 'Описание', 'status': 'Статус',
         'created_date': 'Дата создания', 'issue_date': 'Дедлайн'}

# выводим данные заметки
for key, value in note1.items():
    print(f'\t{key}: {value}')

# функция выбора внесения изменени в заметку
def update_note():
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
            replace_the_username()
        elif user_ch == '2':
            replace_the_title()
        elif user_ch == '3':
            replase_the_content()
        elif user_ch == '4':
            replase_the_status()
        elif user_ch == '5':
            replase_the_issue_date()
        elif user_ch == '6':
            exit()
            break
        else:
            print('\t Неверное чисто! Введите заново.')
            continue


def replace_the_username():  # функция для внесения изменений в username
    name_1 = input('\t Введите новое значение для username: ')
    note1['username'] = name_1


def replace_the_title():  # функция для внесения изменений в title
    title_1 = input('\t введите новое значение для title: ')
    note1['title'] = title_1


def replase_the_content():  # функция для внесения изменений в content
    content_1 = input('\t Введите новое значение для content: ')
    note1['content'] = content_1


def replase_the_status():  # функция для внесения изменений в status
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
    note1['status'] = status_1


def replase_the_issue_date():  # функция для внесения изменений в issue_date
    while True:  # цикл для проверки правильного формата даты при вводе
        issue_date_1 = input('\t Введите дату дедлайна (в формате день-месяц-год (20-12-2024)): ')
        try:
            date1 = datetime.strptime(issue_date_1, '%d-%m-%Y')  # смена данных на 'datetime.datetime'
            break
        except ValueError:
            print('\t Не правильный формат даты')
    issue_date_1 = date.strftime(date1, '%d-%m-%Y')
    note1['issue_date'] = issue_date_1


def exit():
    print('\t Заметка обновлена:')
    for key, value in note1.items():  # анализируем список и выводим новые данные заметки
        print(f'{key}: {value}')

if __name__ == "__main__":
    update_note()
