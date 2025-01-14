# функция должна принимать столько
# аргументов, сколько последовательностей
# передается в функцию map()
def plus(a, b, c):
  return a + b +c
  total = 0 == a,b,c
# функция 'plus' применяется к элементам 
# из всех последовательностей параллельно
x = map(plus, [1, 2], [3, 4], [5, 6])
list(x)
# [9, 12]


def create_tuple(a, b):
    
    return a, b

# функция `map()` останавливается, когда 
# заканчивается самая короткая последовательность
x = map(create_tuple, ['a', 'b'], [3, 4, 5])
print(dict(x))
# {'a': 3, 'b': 4}


x = [1, 2, 3]
y = [4, 5, 6, 7]
# вычисление при помощи встроенной функции 'pow()' 
# 'x' в степени 'y' для каждого элемента 2-х списков
list(map(pow, x, y))
# [1, 32, 729]


x = map(len, ('apple', 'banana', 'cherry'))
list(x)
# [5, 6, 6]


x = map(lambda *args: args, [1, 2], [3, 4])
dict(x)
 # {1: 3, 2: 4}

import re
def clean(word):
     return re.sub(r"[`!?.:;,'\"()-]", "", word.strip())

text = """С помощью цикла `for .. in:` программе
необходимо хранить в памяти системы весь (список)! """
word = text.split()
word = map(clean, word)
text = ' '.join(word)
text
# 'С помощью цикла for  in программе необходимо 
# хранить в памяти системы весь список'
