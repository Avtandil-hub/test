#Для создания объекта класса используется следующий синтаксис:
#Например, определим простейший класс Person, который будет представлять человека:
class Person:
    name = "Tom"
 
    def display_info(self):
        print("Привет, меня зовут", self.name)
 
person1 = Person()
person1.display_info()        
 
person2 = Person()
person2.name = "Sam"
person2.display_info()         