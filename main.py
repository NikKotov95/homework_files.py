def open_file(file='recipes.txt'):
    with open('recipes.txt','r') as file:
        cook_book = {}
        for line in file:
            line = line.strip()
            cook_book.update({line: []})
            k = int(file.readline().strip())
            for _ in range(k):
                lst = file.readline().strip().split(' | ')
                dict = {'ingredient_mane': lst[0], 'quantity': lst[1], 'measure': lst[2]}
                cook_book[line].append(dict)
            file.readline()
        return cook_book
    # print(open_file())

    # noinspection PyUnreachableCode
    def view_cook_book():
        """
        Отображение списка рецептов блюд из файла

        :param c_b:
        :return:
        """


        for key, value in open_file().items():
            print(f'\n {key}')
            for dict in value:
                print(f" {dict['ingredient_name'] +' - '+ dict['quantity'] +' '+ dict ['measure']}")

# view_cook_book(cook_book)

def view_shopping_list(s_l):
    """
    Вывод списка ингредиентов для выбранных блюд с учётом количества человек.
    :param s_l:
    :return:
    """
    print('\nДля приготовления этих блюд нужно:\n')
    index = 1
    for key, values in s_l.items():
        print(f" {index}. {key} {values['quantity']} {values['measure']}")
        index += 1
        print('\n Что-то можно найти н акухне, а остальное прийдётся купить в магазине \n')
def get_shop_list_by_dishes(dishes, person_count):
    """
    Формирование списка необходимых ингредиентов с учётом введёных блюд и количества персон
    :param dishes:
    :param person_count:
    :return:
    """
    shopping_list = ()
    for ingr in dishes:
        for ingred in open_file()[ingred]:
            name_ingr = ingr.pop('ingredient_name')
            ingr['quantity'] = int(ingr['quantity']) * int(person_count)
            if name_ingr in shopping_list:
                ingr['quantity'] += shopping_list[name_ingr]['quantity']
                shopping_list.update({name_ingr: ingr})
                view_shopping_list(shopping_list)

# get_shop_list_by_dishes(['Омлет', 'Запеченный картофель', 'Фахитос', 'Жульен', 'Овощное рагу'], 5)

def input_ingredients(get_shop_list_be_dishes=None):
    """
    Ввод списка желаемых блюд и количество персон
    :return:
    """
    try:
        lst = list(input('Введите через запятую желемые блюда: ').split(', '))
        persons = int(input('Введите количесво персон: '))
        get_shop_list_be_dishes(lst, persons)
    except Exception:
        print('Кажется вы ошиблись с вводом. Проверьте и введите заново без ошибок')

    # input_ingredients()

    def very_main(view_cook_book=None):
        print('\nДобро пожаловать в список рецептов! \n'.upper())
        print('\nВам нужно вести номер действия, чтобы программа выполнила нужное действиу: \n'
              '\n 1. Вывод рецептов. \n'
              '\n 2. Ввод нужных рецептов и количесва человек. Программа вернет список необходимых ингредиентов \n'
              '\n 9. Вывод этой справки \n'
              '\n 0. Выход из программы \n')
        while True:
            prog = str(input('\n Номер действия: \n'.upper()))
            if prog == '1':
                view_cook_book()
            elif prog == '2':
                input_ingredients()
            elif prog == '9':
                print('\nВам нужно вести номер действия, чтобы программа выполнила нужное действиу: \n'
              '\n 1. Вывод рецептов. \n'
              '\n 2. Ввод нужных рецептов и количесва человек. Программа вернет список необходимых ингредиентов \n'
              '\n 9. Вывод этой справки \n'
              '\n 0. Выход из программы \n')
            elif prog == '0':
                print('\n Недеемся вам понравилась наша программа! \n'
                      '\n Досвидания! \n'.upper())
                break
            else:
                print('\nТакой функции пока что ещё нет \n')

                if __name__ == '__main__':
                    very_main()
