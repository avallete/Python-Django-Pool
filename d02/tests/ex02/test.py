# -*- coding: utf-8 -*-

import beverages

def HotBeverageTest(MyClass):
    cl = MyClass()
    print("_______________________")
    print("%s :" % MyClass.__name__)
    print(cl)
    print(cl.description())
    print("_______________________")

HotBeverageTest(beverages.HotBeverage)
HotBeverageTest(beverages.Coffee)
HotBeverageTest(beverages.Tea)
HotBeverageTest(beverages.Cappuccino)