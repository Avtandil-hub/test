# то объект, который возвращает свои элементы по одному за раз.
# С точки зрения Python - это любой объект, 
# у которого есть метод __next__. Этот метод возвращает следующий элемент, если он есть, 
# или возвращает исключение StopIteration, когда элементы закончились.

number = [1, 2, 3]

i = iter(number)

print(next(i))
print(next(i))
print(next(i))
print(next(i))