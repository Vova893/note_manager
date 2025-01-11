from datetime import date, datetime
import json

with open('filename.txt', encoding='utf-8') as file:
    info = file.read()
    info = info.replace('\n', ';')
    symbols = (',', '\t', '_', 'Список заметок:')
    for sym in symbols:
       info = info.replace(sym, '')
    result = info.split('Заметка №1')
    result.remove(';;')
    for i in result:
        result2 = i.split(';')
    # symbols2 = ('')
    # for k in result2:
    #     result2.remove('')
        print(result2)
    # info = file.readlines()
    # print(info)

    # symbols = ('\t______________\n', '\tСписок заметок:\n', 'Заметка №1\n')
    # for i in symbols:
    #     info.remove(i)
    # for kei in info:
    #     #sym = ('\t', '\n')
    #

    #print(type(kei))

        #for k in sym:
         #   info.remove(k)



    # print(info)
    # print(result)
