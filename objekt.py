��� �������� ������� ������ ������������ ��������� ���������:
��������, ��������� ���������� ����� Person, ������� ����� ������������ ��������:

class Person:
    name = "Tom"
 
    def display_info(self):
        print("������, ���� �����", self.name)
 
person1 = Person()
person1.display_info()         # ������, ���� ����� Tom
 
person2 = Person()
person2.name = "Sam"
person2.display_info()         # ������, ���� ����� Sam