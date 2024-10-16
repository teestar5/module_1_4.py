my_string = input("Вывести текст: ")  #Создайте переменную и присвойте ей значение строки с произвольным текстом
print("Результат :", my_string)

my_string = input("Вывести текст : ")  #Вывести количество символов введённого текста
total = 0
for i in range(len(my_string)):
    total = total + 1
print("Количество символов введённого текста = ", total)


my_string = input("Вывести текст: ")      #Выведите строку my_string в верхнем регистре.
print("Результат :", my_string.upper())

my_string = input("Вывести текст: ")      #Выведите строку my_string в нижнем регистре.
print("Результат :", my_string.lower())



my_string = input("Вывести текст: ")      #Пример строки с пробелами"
my_string = my_string.replace(" ", "")
print("Результат :", my_string)

my_string = input("Вывести текст: ")    #Выведите первый символ строки my_string.

print("Результат :", my_string[0])

my_string = input("Вывести текст: ")     #Выведите последний символ строки
print("Результат :", my_string[-1])