from pathlib import Path
from tkinter import *
from async_tkinter_loop import async_handler
from controller.drink_ctl import change_drink, add_drink, delete_drink
import asyncio
from view.util import alert_message, success_message
from model.drink import Drink

OUTPUT_PATH = Path(__file__).parent.parent.parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/drinks")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class DrinkInfo(Frame):

    def __init__(self, parent, drink=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.drink = drink if drink else Drink()  
        self.filter = self.parent.context.currentCat
        canvas = Canvas(
            self,
            height=600,
            width=840,
            bd=0,
            highlightthickness=0,
            relief="ridge",
            background="#f6f6f6",
        )

        canvas.place(x=0, y=0)
        self.assets = {
            "add": PhotoImage(file=relative_to_assets("add.png")),
            "back": PhotoImage(file=relative_to_assets("prev.png")),
            "delete": PhotoImage(file=relative_to_assets("del.png")),
            "entry": PhotoImage(file=relative_to_assets("name.png")),
            "entry_img": PhotoImage(file=relative_to_assets("name_img.png")),
            "confirm": PhotoImage(file=relative_to_assets("confirm.png")),
            "choose": PhotoImage(file=relative_to_assets("choose.png")),
            "unchoose": PhotoImage(file=relative_to_assets("notchoose.png")),
        }

        if self.drink.id:
            button_1 = Button(
                self,
                image=self.assets["confirm"],
                borderwidth=0,
                highlightthickness=0,
                command=async_handler(self.executeUpdate),
                relief="flat",
            )

            button_1.place(x=574.0, y=415.0, width=152.0, height=61.0)
        else:
            button_1 = Button(
                self,
                image=self.assets["add"],
                borderwidth=0,
                highlightthickness=0,
                command=async_handler(self.executeAdd),
                background="#f6f6f6",
                activebackground="#f6f6f6",
                relief="flat",
            )

            button_1.place(x=574.0, y=415.0, width=152.0, height=61.0)

        self.cat_button = dict()
        for i in range(len(self.filter)):
            button_cat = Button(
                self,
                background="#f6f6f6",
                activebackground="#f6f6f6",
                borderwidth=0,
                command=lambda i=i: self.set_category(self.filter[i].id),
                highlightthickness=0,
                relief="flat",
                text=self.filter[i].name,
                compound="center",
                font=("Inter SemiBold", 13),
            )
            button_cat.config(image=self.assets["unchoose"])
            button_cat.place(x=153 + i * 143, y=158.0, width=120, height=48.0)
            self.cat_button[self.filter[i].id] = button_cat
        if self.drink.id:
            self.set_category(self.drink.category)

        self.name_txt = StringVar()
        self.price_txt = StringVar()
        if self.drink.id:
            self.name_txt.set(drink.name)
            self.price_txt.set(drink.price)

        canvas.create_image(439.0, 263.0, image=self.assets["entry_img"])
        canvas.create_image(435.0, 263.5, image=self.assets["entry"])
        entry_1 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.name_txt,
            font=("Inter", 20),
        )
        entry_1.place(x=200.0, y=233.0, width=470.0, height=59.0)

        canvas.create_image(435.0, 351.5, image=self.assets["entry_img"])
        entry_2 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.price_txt,
            font=("Inter", 20),
        )
        entry_2.place(x=200.0, y=321.0, width=470.0, height=59.0)

        if self.drink.id:
            canvas.create_text(
                113.0,
                57.0,
                anchor="nw",
                text="Sửa món",
                fill="#000000",
                font=("Inter Bold", 40 * -1),
            )
        else:
            canvas.create_text(
                113.0,
                57.0,
                anchor="nw",
                text="Thêm món",
                fill="#000000",
                font=("Inter Bold", 40 * -1),
            )

        canvas.create_text(
            48.0,
            171.0,
            anchor="nw",
            text="Loại",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )

        canvas.create_text(
            43.0,
            251.0,
            anchor="nw",
            text="Tên món",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )

        image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        canvas.create_image(439.0, 352.0, image=image_image_2)

        canvas.create_text(
            43.0,
            340.0,
            anchor="nw",
            text="Giá bán",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )

        button_6 = Button(
            self,
            image=self.assets["back"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda:self.parent.change_section("drinks"),
            background="#f6f6f6",
            activebackground="#f6f6f6",
            relief="flat",
        )
        button_6.place(x=43.0, y=60.0, width=47.0, height=45.0)

        button_7 = Button(
            self,
            image=self.assets["delete"],
            borderwidth=0,
            highlightthickness=0,
            command=async_handler(self.executeDelete),
            background="#f6f6f6",
            activebackground="#f6f6f6",
            relief="flat",
        )
        if self.drink.id:
            button_7.place(x=426.0, y=415.0, width=122.0, height=61.0)

    def set_category(self, category):
        for key, button in self.cat_button.items():
            if key == category:
                button.config(image=self.assets["choose"], foreground="white")
                self.drink.category = key
            else:
                button.config(image=self.assets["unchoose"], foreground="black")

    async def executeUpdate(self):
        self.drink.name = self.name_txt.get()
        self.drink.price = int(self.price_txt.get())
        task = asyncio.create_task(change_drink(self.drink))
        result = await task
        if result:
            success_message('Thay đổi thông tin thành công!')
            for each in self.parent.context.currentDrink:
                if each.id == self.drink.id:
                    each = self.drink
                    break
        else:
            alert_message('Thay đổi thông tin thất bại')

    async def executeAdd(self):
        self.drink.name = self.name_txt.get()
        self.drink.price = int(self.price_txt.get())
        task = asyncio.create_task(add_drink(self.drink))
        results = await task
        if results:
            success_message('Thêm món thành công!')
            self.parent.change_section('drink_info',self.drink)
            self.parent.context.currentDrink.append(self.drink)
        else:
            alert_message('Thêm món thất bại')

    async def executeDelete(self):
        task = asyncio.create_task(delete_drink(self.drink.id))
        result = await task
        if result:
            success_message('Đã xóa món khỏi menu!')
            for i, each in enumerate(self.parent.context.currentDrink):
                if each.id == self.drink.id:
                    del self.parent.context.currentDrink[i]
                    break
            self.parent.change_section('drinks')
        else:
            alert_message('Xóa món thất bại')