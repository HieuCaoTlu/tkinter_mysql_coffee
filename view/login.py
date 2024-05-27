from pathlib import Path
from tkinter import Canvas, Entry, Button, PhotoImage, Frame, StringVar, Label
from controller.login_ctl import login
from controller.drink_ctl import drinks
from controller.invoice_ctl import invoices, get_invoice_drink
from controller.employee_ctl import employees
from controller.category_ctl import categories
from controller.kpi_ctl import get_kpi
from controller.other_ctl import get_other
from .util import alert_message
from async_tkinter_loop import async_handler
import asyncio

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/login")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Login(Frame):

    async def authenticate(self):
        if self.username_txt.get() == "" or self.password_txt.get() == "":
            alert_message("Vui lòng nhập đủ thông tin đăng nhập")
            return
        else:
            label = Label(self, text="Đang đăng nhập..", font=("Inter", 18))
            label.pack()
            self.login_button.place_forget()
            try:
                task = asyncio.create_task(
                    login(self.username_txt.get(), self.password_txt.get())
                )
                self.context.currentUser = await task
            except Exception as e:
                alert_message(f"Đăng nhập thất bại {e}")
            if self.context.currentUser == None:
                alert_message("Sai thông tin đăng nhập")
            else:
                label.config(text="Đang nạp dữ liệu..")
                task2 = asyncio.create_task(invoices())
                self.context.currentInvoice = await task2
                task3 = asyncio.create_task(drinks())
                self.context.currentDrink = await task3
                task4 = asyncio.create_task(employees())
                self.context.currentEmp = await task4
                task5 = asyncio.create_task(categories())
                self.context.currentCat = await task5
                task6 = asyncio.create_task(get_invoice_drink())
                self.context.currentInvoiceDrink = await task6
                task7 = asyncio.create_task(get_kpi())
                self.context.currentKPI = await task7
                task8 = asyncio.create_task(get_other())
                self.context.currentTax, self.context.currentDiscount = await task8
                self.username_txt.set("")
                self.password_txt.set("")
                self.parent.executeDashboard()
            label.pack_forget()
            self.login_button.place(x=235.0, y=419.0, width=192.0, height=50.0)

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.context = self.parent.context
        self.assets = {
            "bg": PhotoImage(file=relative_to_assets("bg.png")),
            "user": PhotoImage(file=relative_to_assets("user.png")),
            "pass": PhotoImage(file=relative_to_assets("pass.png")),
            "place": PhotoImage(file=relative_to_assets("place.png")),
            "login": PhotoImage(file=relative_to_assets("login.png")),
        }
        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=600,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        canvas.place(x=0, y=0)
        canvas.create_rectangle(750.0, 0.0, 1000.0, 600.0, fill="#675BEB", outline="")
        canvas.create_image(336.0, 267.0, image=self.assets["place"])
        canvas.create_image(336.0, 356.0, image=self.assets["place"])

        self.username_txt = StringVar()
        self.password_txt = StringVar()

        self.login_button = Button(
            self,
            image=self.assets["login"],
            borderwidth=0,
            highlightthickness=0,
            command=async_handler(self.authenticate),
            relief="flat",
            background="white",
            activebackground="white",
        )
        self.login_button.place(x=235.0, y=419.0, width=192.0, height=50.0)

        canvas.create_text(
            173.0,
            95.0,
            anchor="nw",
            text="TLUCoffee",
            fill="#675BEB",
            font=("Inter Bold", 60 * -1),
        )

        canvas.create_text(
            159.0,
            168.0,
            anchor="nw",
            text="Phần mềm quản lý quán cà phê TLU",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )

        canvas.create_text(
            230.0,
            525.0,
            anchor="nw",
            text="© Cao Trung Hiếu 2024",
            fill="#595959",
            font=("Inter", 18 * -1),
        )

        canvas.create_image(212.0, 355.0, image=self.assets["pass"])
        canvas.create_image(211.0, 267.0, image=self.assets["user"])
        canvas.create_image(779.0, 300.0, image=self.assets["bg"])
        entry_1 = Entry(
            self,
            bd=0,
            bg="#F3F3F3",
            fg="#000716",
            highlightthickness=0,
            font=("Inter", 18 * -1),
            textvariable=self.username_txt,
        )
        entry_1.place(
            x=245.0,
            y=245.0,
            width=199.0,
            height=42.0,
        )
        entry_2 = Entry(
            self,
            bd=0,
            bg="#F3F3F3",
            fg="#000716",
            highlightthickness=0,
            font=("Inter", 18 * -1),
            textvariable=self.password_txt,
            show="*",
        )
        entry_2.place(x=245.0, y=334.0, width=199.0, height=42.0)
