# Генераторы позволяют значительно упростить работу по конструированию итераторов. 
# В предыдущих примерах, для построения итератора и работы с ним, 
# мы создавали отдельный класс. Генератор – это функция,
# которая будучи вызванной в функции next() возвращает следующий объект согласно алгоритму ее работы. 
# Вместо ключевого слова return в генераторе используется yield.
def simple_generator(val):
   while val > 0:
       val -= 1
       yield 1

gen_iter = simple_generator(5)
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
