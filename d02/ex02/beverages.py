# -*- coding: utf-8 -*-

class HotBeverage(object):

    def __init__(self, Price=0.30, Name="hot beverage"):
        self.Price = Price
        self.Name = Name

    def __str__(self):
        return """
Name : %s
Price : %0.2f
description: %s""" % (self.Name, self.Price, self.description())

    def description(self):
        return "Just some hot water in a cup."


class Coffee(HotBeverage):

    def __init__(self, Price=0.40, Name="coffee"):
        HotBeverage.__init__(self, Price, Name)

    def description(self):
        return "A coffee, to stay awake."


class Tea(HotBeverage):

    def __init__(self, Price=0.30, Name="tea"):
        HotBeverage.__init__(self, Price, Name)


class Chocolate(HotBeverage):

    def __init__(self, Price=0.50, Name="chocolate"):
        HotBeverage.__init__(self, Price, Name)

    def description(self):
        return "Chocolate, sweet chocolate.."


class Cappuccino(HotBeverage):

    def __init__(self, Price=0.45, Name="cappuccino"):
        HotBeverage.__init__(self, Price, Name)

    def description(self):
        return "Un po’ di Italia nella sua tazza!"