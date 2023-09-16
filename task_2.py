'''
✔ Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
'''
import os

def get_absolute_path(file):
    return os.path.abspath(file), os.path.basename(file), os.path.splitext(file)[1]


file = input('Введите абсолютный путь файла: ')

absolute_path = get_absolute_path(file)

print(absolute_path)