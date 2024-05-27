from tkinter import Tk
from view.login import Login
from view.dashboard import Dashboard
from async_tkinter_loop import async_mainloop

class AppContext:
    def __init__(self):
        self.currentUser = None
        self.currentDrink = None
        self.currentInvoice = None
        self.currentInvoiceDrink = []
        self.currentEmp = None
        self.currentCat = None
        self.currentKPI = 0
        self.currentTax = 0
        self.currentDiscount = 0

class WindowApp(Tk):
    global user
    def __init__(self):
        Tk.__init__(self)
        self.context = AppContext()
        self.iconbitmap('assets/icon.ico')
        self.title("TLUCoffee POS")
        self.geometry("1000x600")
        self.resizable(False, False)
        self.windows = dict()
        self.create_window("login",Login(self))

    def create_window(self, name, window):
        if name in self.windows:
            self.windows[name].destroy()
        self.windows[name] = window
        window.place(x=0, y=0, width=1000, height=600)
        window.tkraise()
        window.focus_set()
        

    def executeDashboard(self):
        self.create_window("dashboard", Dashboard(self))

    def logout(self):
        self.create_window("login", Login(self))

master = WindowApp()
async_mainloop(master)