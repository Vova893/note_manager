notizen = []
note1 = {'Имя': 'Светлана' , 'Заголовок': 'Книги', 'Описание': 'Темы реферата', 'Статус': 'в работе',
            'Дата создания': '12-12-2024', 'Дедлайн': '25-04-2025'}
note2 = {'Имя': 'Андрей', 'Заголовок': 'Учеба', 'Описание': 'Расписание занятий', 'Статус': 'Новая',
            'Дата создания': '17-12-2024', 'Дедлайн': '30-12-2024'}
notizen.append(note1)
notizen.append(note2)
print('\fТекущие заметки:')

for i, note_ in enumerate(notizen):  # выводим информацию о текущих заметках
    print(f'\t______________\n'
          f'Заметка №', i + 1)
    for j, k in note_.items():
        print(f'\t{j}: {k}')

delete_note = input('\fВведите имя пользователя или заголовок для удаления заметки: ')

for delete_dictionary in notizen:
    if delete_dictionary['Имя'] == delete_note or delete_dictionary['Заголовок'] == delete_note:
        print(f'\fВы хотите удалить заметку {delete_note} (да/нет):')
        if input().lower() == 'да':
            if delete_dictionary in notizen:
                notizen.remove(delete_dictionary)
                print(f'\fЗаметка {delete_note} успешно удалена. Остались следующие заметки: ')
                break
    else:
        print('\fЗаметок с таким именем пользователя или заголовком не найдено!')
        break

for i, note_ in enumerate(notizen):
    print(f'\t______________\n'
          f'Заметка №', i + 1)
    for j, k in note_.items():
        print(f'\t{j}: {k}')  # анализируем и выводим список с оставшимися заметками
