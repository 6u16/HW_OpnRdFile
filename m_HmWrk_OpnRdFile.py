# <<Домашнее задание «Открытие и чтение файла, запись в файл>>
## Task №1,2,3

import os
 
# Task №1,2:

class Cook_book:
    def __init__(self, cook_book_name):
        self.cook_book_name = cook_book_name
        self.cook_book = {}

    def add_bludo(self,bludo):
        self.bludo = bludo
        self.cook_book.update(self.bludo)
        #print(self.cook_book)

    def get_ingr_cnt(self,i_name):
        for i,j in enumerate(self.cook_book.get(i_name),start=1):
            pass
        return i

    def person_calc(self, private_Person): # Расчёт на количество Персон
        self.value_of_ingrdnts = {}
        self.private_Person = private_Person  ### - Сказал Графт, Графта нельзя запрограммировать так чтобы он не называл его рядовой Персон. Отметка Калта "991202"
        for self.ingrdnts in self.cook_book.values(): # Идём к списку ингредиентов всех блюд
            for ingrdnt in self.ingrdnts: 
                self.all_value = {}
                self.all_value.update(ingrdnt)
                del self.all_value['ingredient_name'] # Оставляем только объём и еи
                self.all_value['quantity'] *= private_Person
                if ingrdnt.get('ingredient_name') in self.value_of_ingrdnts: # если ингредиент уже есть то прибавляем массу/объём
                    temp_1 = self.value_of_ingrdnts.get(ingrdnt.get('ingredient_name'))
                    self.all_value['quantity'] = temp_1.get('quantity') + self.all_value.get('quantity') # Суммируем одинаковые компоненты
                    self.value_of_ingrdnts[ingrdnt.get('ingredient_name')] = self.all_value
                else:
                    self.value_of_ingrdnts.setdefault(ingrdnt.get('ingredient_name'),self.all_value)

class Bludo:
    def __init__(self, bludo_name):
        self.bludo_name = bludo_name
        self.bludo_reciept = {}
        self.ingredients = []

    def add_ingredient(self,ingredient):
        self.ingredient = ingredient
        self.ingredients.append(ingredient)
        self.bludo_reciept.setdefault(self.bludo_name, self.ingredients)

    def get_ingr_cnt(self):
        for i in self.bludo_reciept.values():
            pass
        return len(i)

class Ingredient:
    def __init__(self, ingredient_name, quantity, measure):
        self.ingredient_dict = {}
        self.ingredient_name = ingredient_name
        self.quantity = quantity
        self.measure = measure
        self.ingredient_dict.setdefault('ingredient_name', self.ingredient_name)
        self.ingredient_dict.setdefault('quantity', self.quantity)
        self.ingredient_dict.setdefault('measure', self.measure)


bludo1 = Bludo('Омлет')
ingredient1 = Ingredient('Яйцо',2,'шт')
ingredient2 = Ingredient('Молоко',100,'мл')
ingredient3 = Ingredient('Помидор',2,'шт')

bludo2 = Bludo('Утка по Пекински')
ingredient4 = Ingredient('Утка',1,'шт')
ingredient5 = Ingredient('Вода',2,'л')
ingredient6 = Ingredient('Мёд',3,'ст.л')
ingredient7 = Ingredient('Соевый соус',60,'мл')

bludo3 = Bludo('Запечёный картофель')
ingredient8 = Ingredient('Картофель',1,'шт')
ingredient9 = Ingredient('Чеснок',3,'зубч')
ingredient10 = Ingredient('Сыр гауда',100,'г')

# Добавляем ингредиенты в блюда
bludo1.add_ingredient(ingredient1.ingredient_dict)
bludo1.add_ingredient(ingredient2.ingredient_dict)
bludo1.add_ingredient(ingredient3.ingredient_dict)
bludo1.add_ingredient(ingredient10.ingredient_dict) # Проверка на повторение названия ингредиента

bludo2.add_ingredient(ingredient4.ingredient_dict)
bludo2.add_ingredient(ingredient5.ingredient_dict)
bludo2.add_ingredient(ingredient6.ingredient_dict)
bludo2.add_ingredient(ingredient7.ingredient_dict)

bludo3.add_ingredient(ingredient8.ingredient_dict)
bludo3.add_ingredient(ingredient9.ingredient_dict)
bludo3.add_ingredient(ingredient10.ingredient_dict)

# Добавляем блюда в книгу
cook_book1 = Cook_book('Книга блюд №1')
cook_book1.add_bludo(bludo1.bludo_reciept)
cook_book1.add_bludo(bludo2.bludo_reciept)
cook_book1.add_bludo(bludo3.bludo_reciept)

# Смотрим на книгу в словаре
print(cook_book1.cook_book_name,'\n')
for i in cook_book1.cook_book.items():
    print(i)
print('\n')

# Расчёт блюд на кол. Персон
cook_book1.person_calc(6)
print(f'На {cook_book1.private_Person} Персон\n')
for i in cook_book1.value_of_ingrdnts.items():
    print(i)
print('\n')

# Запись Книги блюд в txt
file_path_01 = os.path.join(os.getcwd(), 'Txt_files\\m_HmWrk_OpnRdFile_CookBook_01.txt')  ## строительство путик нашему файлу

f_01 = open(file_path_01)
with open(file_path_01, 'w', encoding='utf-8') as f_01:
    f_01.write(f'{cook_book1.cook_book_name}\n\n')
    for bl_name in cook_book1.cook_book.keys():
        f_01.write(f'{bl_name}\n')
        f_01.write(f'{cook_book1.get_ingr_cnt(bl_name)}\n')
        for ingrdnts in cook_book1.cook_book.get(bl_name):
            n1 = ingrdnts.get('ingredient_name')
            n2 = ingrdnts.get('quantity')
            n3 = ingrdnts.get('measure')
            f_01.write(f'{n1} | {n2} | {n3}\n')
        f_01.write('\n')


## Task №3:
# Файлы для чтения [f_02,f_03,f_04] в кодировке 'ANSI'
# Файл для записи 'f_output' будет в кодировке 'UTF-8'
file_path_02 = os.path.join(os.getcwd(), 'Txt_files\\m_HmWrk_OpnRdFile_f_01.txt')  ## строительство путик нашему файлу
file_path_03 = os.path.join(os.getcwd(), 'Txt_files\\m_HmWrk_OpnRdFile_f_02.txt')  
file_path_04 = os.path.join(os.getcwd(), 'Txt_files\\m_HmWrk_OpnRdFile_f_03.txt')
file_path_output = os.path.join(os.getcwd(), 'Txt_files\\m_HmWrk_OpnRdFile_f_output.txt')

f_02 = open(file_path_02)
f_03 = open(file_path_03)
f_04 = open(file_path_04)
f_out = open(file_path_output)

# Функция сортировки текстовых файлов по кол. строк
def sort_txt_str_quantity():
    file_list = [f_02,f_03,f_04]
    file_path_list = [file_path_02,file_path_03,file_path_04]
    txt_list = []
    txt_dict = {}
    key_list =[]

    # Пишем в словарь текст из файлов с ключами равными кол.строк в них
    for i_01, element_file_list in enumerate(file_list): # element_file_list - очередной файл из списка
        with open(file_path_list[i_01]) as element_file_list: # Читаем файл по пути списка file_path_list в итерации списка файлов file_list
            for i_02, element_str in enumerate(element_file_list,start=1):
                txt_list.append(element_str)
            txt_dict.setdefault(i_02,txt_list) # Словарь из ключей = кол.строк и списком строк из файла
            txt_list = []

    for i in txt_dict.keys(): # Получим ключи и сортируем их
        key_list.append(i)
    key_list.sort()

    with open(file_path_output,'w',encoding='utf-8') as f_out: # Пишем в m_HmWrk_OpnRdFile_f_output.txt сортированную последовательность
        for key in key_list:
            for str_element in txt_dict.get(key):
                f_out.write(str_element)
            f_out.write('\n')
        
sort_txt_str_quantity()