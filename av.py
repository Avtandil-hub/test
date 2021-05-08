# from turtle import*
# width(5)
# x = - 150
# y = 250 
# up()
# goto(x,y)
# down()
# tracer(2)
# for x in range(-100,300):
#     clear()
#     begin_fill()
#     color('red', 'blue')
#     goto(x,y-100)
#     goto(x,y)
#     goto(x-100,y)
#     goto(x-100,y-100)
#     end_fill()
#for y in range (250, - 150,-1):

#HOME WORK

# lesson 1
# n = 179
# def reversedigits(n):
#     if n < 10:
#         print(n, end = '')
#     else:
#         print(n % 10, end = '')
#         reversedigits( n // 10 )
    

# print(n)
# reversedigits(n)

# #lesson 2

# import random

# quest = int(input("Enter length: "))

# def generate_list_with_random_numbers(ln):
#     lst = []
#     i = 0
#     while i <= ln:
#         i += 1
#         lst.append(random.randint(1, ln))
#     return lst

# lst = generate_list_with_random_numbers(quest)

# def generate_list_with_square_numbers(ln):
#     return list(map(lambda ln: ln ** 2, ln))

# new_lst = generate_list_with_square_numbers(lst)

# print(lst, end="\n")
# print(new_lst)

def test_1():
    def test_2():
        print('hello')
        print('world')

    test_2()

test_1()