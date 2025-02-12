import yaml

try:
    # Прочитаем файл
    with open('filename.yaml', encoding='utf-8') as file:
        
        def load_notes_from_file(filename):
            # Десериализуем из формата json в данные Python
            notes = yaml.load(file, Loader=yaml.FullLoader)
            if notes == None:
                print('Файл пустой!')

            print(notes)
        
        load_notes_from_file(file)
        
# Обработка возможных ошибок
except FileNotFoundError:
    file = open('../filename.yaml', 'w', encoding='utf-8')
    print('\tФайл не найден! Создан новый файл')
except UnicodeDecodeError:
    print('\tНе удалось декодировать файл!')
except PermissionError:
    print('\tОшибка доступа к файлу!')
except yaml.parser.ParserError:
    print('Ваш файл не является допустимым YAML')
except:
    print('\tЧто-то случилось при запуске!')
