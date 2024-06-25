"""  Написати функцію, яка обчислює суму двох чисел.
"""
def number_addition(a,b):
    return a + b


"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(s):
    return s[::-1]


"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word(words):
    if not words:
        return ""

    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


"""Создайте функцию, которая будет округлять четырехзначные числа, заменяя все цифры, стоящие справа от разряда числа, 
буквой «К». Число менее тысячи будет выводиться без изменений.
"""

def views_func(views):
    if views < 1000:
        print(views)
        return
    hundreds = views / 1000
    print((round(hundreds * 10.0) / 10.0), "K")


"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
        index = str1.find(str2)
        return index

