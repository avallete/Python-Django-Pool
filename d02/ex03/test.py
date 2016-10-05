# -*- coding: utf-8 -*-

import random
import machine
import beverages

class   Caca(object):

    def __init__(self):
        self.poop = 1

cf = machine.CoffeeMachine()
possibility = [beverages.Cappuccino, beverages.Coffee, beverages.Tea, beverages.Chocolate, beverages.HotBeverage]

for i in range(0, 30):
    try:
        cup = cf.serve(random.choice(possibility))
        print("Yes, we have a delicious: %s" % cup.description())
    except cf.BrokenMachineException as e:
        print(e)
        print("Ohhh, the machine is broken, let's fix it !")
        cf.repair()

print("Try to pass an bad Class to serve method.")
cf.serve(Caca)
cf.serve(Caca)
cf.serve(Caca)