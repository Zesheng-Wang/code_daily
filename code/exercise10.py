# -*- coding: utf-8 -*-


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def say_age(self):
        print(self.name, "的年龄是：", self.__age)


class Student(Person):
    def __init__(self, name, age, gender):
        self.gender = gender
        Person.__init__(self, name, age)


stu1 = Student('VN', 10, 'man')
print(stu1.name)
print(stu1.gender)
stu1.say_age()
print(dir(stu1))
print(stu1)
