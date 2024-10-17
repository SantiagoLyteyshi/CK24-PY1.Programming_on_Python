# TODO Найдите количество книг, которое можно разместить на дискете
obyom_diskety = int(1.44 * 1024 ** 2)

stranic_in_kniga = 100
strok_in_stranica = 50
symbol_in_stroka = 25
odin_symbol = 4

obyom_of_kniga = stranic_in_kniga * strok_in_stranica * symbol_in_stroka * odin_symbol

kolvo_knig = obyom_diskety // obyom_of_kniga

print("Количество книг, помещающихся на дискету:", kolvo_knig)
