#https://www.youtube.com/watch?v=Dx2SE4hYy4g&list=PLRDzFCPr95fIgPrFFW-0nXT5YH6ZnjRM6&index=1

from abc import ABC, abstractclassmethod

class Person(ABC):
    name = 'Vladimir'
    age = 23

    #общий метод, который будут использовать все наследники
    def draw(self):
        print('Drew a chess piece')

    #абстрактный метод, который будет необходимо переопределять для каждого подкласса
    @abstractclassmethod
    def move(self):
        print('Abstract method')

vladimir = Person()

print(vladimir)