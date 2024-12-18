from abc import *


class schoolmember(metaclass=ABCMeta):
    '''Представляет любого человека в школе.'''
    def __init__(self, name, age):
        self .name = name
        self .age = age
        print('(Создан SchoolMember: {0})'.format(self.name))
    @abstractmethod
    def tell(self):
        '''Вывести информацию.'''
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")


class teacher(schoolmember):
    '''Представляет преподавателя.'''
    def __init__(self, name, age, salary):
        schoolmember .__init__(self, name, age)
        self .salary = salary
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        schoolmember .tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))
class student(schoolmember):
    '''Представляет студента.'''
    def __init__(self, name, age, marks):
        schoolmember .__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))
    def tell(self):
        schoolmember .tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))

t = teacher('Mrs. Shrividya', 40, 30000)
s = student('Swaroop', 25, 75)
#m = SchoolMember('abc', 10)
# Это приведёт к ошибке: "TypeError: Can't instantiate abstract class
# SchoolMember with abstract methods tell"

print()# печатает пустую строку

members = [t, s]
for member in members:
  member.tell() # работает как для преподавателя, так и для студента