username = input('Введите имя пользователя: ')
title = input('Введите заголовок заметки: ')
content = input('Введите описание заметки: ')
status = input('Укажите статус заметки: ')
created_date = input('Укажите дату создания заметки в формате "день-месяц-год", пример "10-11-2024": ')
issue_date = input('Укажите дату истечения заметки (дедлайн) в формате "день-месяц-год", пример "10-12-2024": ')


dictionary = {1: username, 2: title, 3: content, 4: status, 5: created_date, 6: issue_date,}
print(dictionary)

