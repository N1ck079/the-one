# Задача-1:
# Примечание: Если уже делали easy задание, то просто перенесите решение сюда.
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.

    Исключения:
        - ValueError: вычисление не возможно.
    """
    if a * b >= 0:
        return (a * b) ** 0.5
    else:
        raise ValueError("Невозможно определить среднее геометрическое "
                         "введенных чисел.")


try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except ValueError as err:
    print("Ошибка:", err, ". Проверьте введенные числа.")
except Exception as err:
    print("Ошибка:", err)

# ПРИМЕЧАНИЕ: Для решения задачи 2-3 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь "меню" выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

from easy import level_up, mk_dir, rem_dir, list_dir, ch_dir
import os
print('Ваша текущая директория {}'.format(os.getcwd()))
menu = 0
try:
    while(menu < 1 or menu > 4):
        menu = int(input('Выберите один из пунктов\n1. Перейти в папку\n2. Просмотреть содержимое текущей папки\n3. Удалить папку\n4. Создать папку\nВаш выбор: '))
        if (menu < 1 or menu > 4):
            print('Попробуйте снова')
    print('Ваша текущая директория {}'.format(os.getcwd()))
    if menu == 1:
        folder = str(input('В какую папку вы хотите перейти: '))
        ch_dir(folder)
    elif menu == 2:
        list_dir()
    elif menu == 3:
        folder = str(input('Какую папку вы хотите удалить: '))
        rem_dir(folder)
    elif menu == 4:
        folder = str(input('Какую папку вы хотите создать: '))
        mk_dir(folder)
except ValueError:
    print('Невозможно создать/удалить/прейти\nValueError')
except FileNotFoundError:
    print('Невозможно создать/удалить/прейти\nFileNotFoundError')
else:
    print('Успешно создано/удалено/перешел')
print('Ваша текущая директория {}'.format(os.getcwd()))