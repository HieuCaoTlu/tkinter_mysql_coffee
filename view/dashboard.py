from pathlib import Path
from tkinter import Canvas, Button, PhotoImage, Frame
from view.home import Home
from view.info.main import Info
from view.orders.main import Orders
from view.drinks.main import Drinks
OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/dashboard")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Dashboard(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.context = self.parent.context
        self.windows = {}
        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=600,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.place(x=0, y=0)

        self.assets = {
            "home": (
                PhotoImage(file=relative_to_assets("home.png")),
                PhotoImage(file=relative_to_assets("home_choose.png")),
            ),
            "drinks": (
                PhotoImage(file=relative_to_assets("drinks.png")),
                PhotoImage(file=relative_to_assets("drinks_choose.png")),
            ),
            "orders": (
                PhotoImage(file=relative_to_assets("orders.png")),
                PhotoImage(file=relative_to_assets("orders_choose.png")),
            ),
            "info": (
                PhotoImage(file=relative_to_assets("info.png")),
                PhotoImage(file=relative_to_assets("info_choose.png")),
            ),
        }
        home_button = Button(
            self,
            image=self.assets["home"][0],
            background="white",
            activebackground="white",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.change_window("home"),
            relief="flat",
        )
        home_button.place(x=38.0, y=56.0, width=76.0, height=97.0)
        drinks_button = Button(
            self,
            image=self.assets["drinks"][0],
            background="white",
            activebackground="white",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.change_window("drinks"),
            relief="flat",
        )
        drinks_button.place(x=38.0, y=158.0, width=76.0, height=97.0)
        orders_button = Button(
            self,
            image=self.assets["orders"][0],
            background="white",
            activebackground="white",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.change_window("orders"),
            relief="flat",
        )
        orders_button.place(x=38.0, y=260.0, width=76.0, height=97.0)
        info_button = Button(
            self,
            image=self.assets["info"][0],
            background="white",
            activebackground="white",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.change_window("info"),
            relief="flat",
        )
        info_button.place(x=38.0, y=362.0, width=76.0, height=97.0)
        logout_button = Button(
            self,
            background="white",
            activebackground="white",
            borderwidth=0,
            highlightthickness=0,
            command=lambda:self.parent.logout(),
            relief="flat",
            text="Đăng xuất",
            font=("Inter SemiBold", 12),
            foreground="#675CEC",
            activeforeground="#675CEC"    
        )
        logout_button.place(x=25.0, y=542, width=100, height=20)
        self.buttons = {
            'home':home_button,
            'drinks':drinks_button,
            'orders':orders_button,
            'info':info_button    
        }
        self.change_window("home")

    def change_window(self, name):
        for button_name, button in self.buttons.items():
            if button_name == name:
                button.config(image=self.assets[button_name][0])
            else:
                button.config(image=self.assets[button_name][1])
        
        for window in self.windows.values():
            window.place_forget()
            del window
        if name == 'home':
            self.windows[name] = Home(self)
        elif name == 'drinks':
            self.windows[name] = Drinks(self)
        elif name == 'orders':
            self.windows[name] = Orders(self)
        elif name == 'info':
            self.windows[name] = Info(self)
        else:
            return None
        self.windows[name].place(x=150, y=0, width=1000, height=600)
        self.windows[name].tkraise()
        self.windows[name].focus_set()
        