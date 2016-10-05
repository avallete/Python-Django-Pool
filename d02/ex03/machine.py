# -*- coding: utf-8 -*-

import beverages
import random


class CoffeeMachine(object):


    class BrokenMachineException(Exception):

        def __init__(self):
            Exception.__init__(self, "This coffee machine has to be repaired.")


    class EmptyCup(beverages.HotBeverage):

        def __init__(self, Price=0.90, Name="empty cup"):
            beverages.HotBeverage.__init__(self, Price, Name)

        def description(self):
            return "An empty cup?! Gimme my money back"

    def __init__(self):
        self.broken = 0

    def repair(self):
        self.broken = 0

    def serve(self, hot_beverage_class):
        if not issubclass(hot_beverage_class, beverages.HotBeverage):
            raise Exception("Error, your the parameter must be a class inherited from of HotBeverage")
        if self.broken >= 10:
            raise self.BrokenMachineException()
        else:
            self.broken += 1
            return hot_beverage_class() if random.randrange(2) else self.EmptyCup()
