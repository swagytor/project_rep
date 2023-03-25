from random import randint


class Coin:

    def __init__(self):
        self.__sideup = 'Орел'

    def toss(self):
        if randint(0, 1):
            self.__sideup = 'Орел'
        else:
            self.__sideup = 'Решка'

    def get_sideup(self):
        return self.__sideup
