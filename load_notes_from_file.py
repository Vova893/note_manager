import yaml

try:
    # Прочитаем файл
    with open('filename.yaml', encoding='utf-8') as file:

        # Десериализуем из формата json в данные Python
        notes = yaml.load(file, Loader=yaml.FullLoader)
        if notes == None:
            print('Файл пустой!')

        print(notes)

# Обработка возможных ошибок
except FileNotFoundError:
    print('\tФайл не найден!')
except UnicodeDecodeError:
    print('\tНе удалось декодировать файл!')
except PermissionError:
    print('\tОшибка доступа к файлу!')
except yaml.parser.ParserError:
    print('Ваш файл не является допустимым YAML')
except:
    print('\tЧто-то случилось при запуске!')
