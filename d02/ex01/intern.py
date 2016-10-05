# -*- coding: utf-8 -*-

class Intern(object):

    def __init__(self, Name="My name ? I'm nobody, an intern, I have no name."):
        self.name = Name

    def __str__(self):
        return self.name

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee()

    class Coffee(object):
        def __str__(self):
            return "This is the worst coffee you ever tasted."
