from tkinter import Frame
from .drink_info import DrinkInfo
from .drinks import AllDrinks

class Drinks(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.context = self.parent.context
        self.sections = {
            "drinks": AllDrinks(self),
            "drink_info": DrinkInfo(self),
        }
        self.change_section("drinks")

    def change_section(self, name, drink=None):
        if name == "drink_info":
            self.sections["drink_info"] = DrinkInfo(self, drink)
        elif name == "drinks":
            self.sections["drinks"] = AllDrinks(self)
        for section in self.sections.values():
            section.place_forget()
        self.sections[name].place(x=0, y=0, width=1000, height=600)
        self.sections[name].tkraise()