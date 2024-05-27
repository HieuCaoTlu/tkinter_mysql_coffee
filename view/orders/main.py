from tkinter import Frame
from .orders import AllOrders
from .add_order import AddOrder

class Orders(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.context = self.parent.context
        self.sections = {
            "orders": AllOrders(self),
            "add_order": AddOrder(self),
        }
        self.change_section("add_order")

    def change_section(self, name):
        if name == "orders":
            self.sections["orders"].update_items()
        for section in self.sections.values():
            section.place_forget()
        self.sections[name].place(x=0, y=0, width=1000, height=600)
        self.sections[name].tkraise()