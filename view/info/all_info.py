from pathlib import Path
from tkinter import *
from controller.kpi_ctl import change_kpi, add_kpi
import asyncio
from async_tkinter_loop import async_handler
from controller.other_ctl import change_other
from model.kpi import KPI
from view.util import alert_message, success_message
from datetime import datetime

OUTPUT_PATH = Path(__file__).parent.parent.parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/info")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class AllInfo(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.context = self.parent.context
        label = Label(self, text="Info", font=("Arial", 24))
        label.place(x=300, y=300, width=500, height=400)

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=600,
            width=840,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.assets = {
            "emps": PhotoImage(file=relative_to_assets("button_1.png")),
            "btn": PhotoImage(file=relative_to_assets("image_1.png")),
            "btn-small": PhotoImage(file=relative_to_assets("image_2.png")),
            "btn-normal": PhotoImage(file=relative_to_assets("image_3.png")),
            "confirm": PhotoImage(file=relative_to_assets("button_4.png")),
        }

        canvas.place(x=0, y=0)
        canvas.create_rectangle(0.0, 0.0, 840.0, 600.0, fill="#F9F9F9", outline="")

        canvas.create_text(
            43.0,
            115.0,
            anchor="nw",
            text="Chính sách",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )

        canvas.create_text(
            43.0,
            321.0,
            anchor="nw",
            text="Tiện ích khác",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )

        canvas.create_text(
            43.0,
            529.0,
            anchor="nw",
            text="TLUCoffee POS ",
            fill="#828282",
            font=("Inter", 25 * -1),
        )

        canvas.create_text(
            259.0,
            527.0,
            anchor="nw",
            text="Phiên bản: 0.5 Thử nghiệm",
            fill="#828282",
            font=("Inter Light", 12 * -1),
        )

        canvas.create_text(
            259.0,
            545.0,
            anchor="nw",
            text="Phát triển: A44212 - Cao Trung Hiếu",
            fill="#828282",
            font=("Inter Light", 12 * -1),
        )

        canvas.create_text(
            65.0,
            172.958740234375,
            anchor="nw",
            text="Chỉ tiêu tháng này",
            fill="#000000",
            font=("Inter", 18 * -1),
        )
        canvas.create_text(
            43.0,
            55.0,
            anchor="nw",
            text="Vận hành",
            fill="#000000",
            font=("Inter Bold", 40 * -1),
        )
        canvas.create_image(183.0, 221.0, image=self.assets["btn"])
        canvas.create_image(452.0, 221.0, image=self.assets["btn-small"])
        canvas.create_image(687.0, 221.0, image=self.assets["btn-normal"])
        canvas.create_text(
            599.0,
            173.0,
            anchor="nw",
            text="Khuyến mại",
            fill="#000000",
            font=("Inter", 18 * -1),
        )
        canvas.create_text(
            371.0,
            173.0,
            anchor="nw",
            text="Thuế áp dụng",
            fill="#000000",
            font=("Inter", 18 * -1),
        )
        canvas.create_text(
            65.0,
            172.958740234375,
            anchor="nw",
            text="Chỉ tiêu tháng này",
            fill="#000000",
            font=("Inter", 18 * -1),
        )
        self.kpi = StringVar()
        self.tax = StringVar()
        self.discount = StringVar()
        if self.context.currentKPI:
            self.kpi.set(str(self.context.currentKPI.value))
        self.tax.set(str(self.context.currentTax) + "%")
        self.discount.set(str(self.context.currentDiscount) + "%")
        button_1 = Button(
            self,
            image=self.assets["emps"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.change_section("all_emp"),
            relief="flat",
            background="#f6f6f6",
            activebackground="#f6f6f6",
        )
        button_1.place(x=43.0, y=362.0, width=280.0, height=141.0)
        self.kpi_btn = Entry(
            self,
            bd=0,
            bg="#675BEB",
            fg="#000716",
            highlightthickness=0,
            background="#f6f6f6",
            justify="right",
            font=("Inter Bold", 18),
            textvariable=self.kpi,
            state="readonly",
            foreground="#675CEC",
            readonlybackground="white",
        )
        self.kpi_btn.place(
            x=67.0,
            y=233.0,
            width=230.0,
            height=28.0,
        )
        self.tax_btn = Entry(
            self,
            bd=0,
            bg="#675BEB",
            fg="#000716",
            highlightthickness=0,
            background="#f6f6f6",
            justify="right",
            font=("Inter Bold", 18),
            textvariable=self.tax,
            state="readonly",
            foreground="#675CEC",
            readonlybackground="white",
        )
        self.tax_btn.place(x=374.0, y=233.0, width=155.0, height=28.0)
        self.discount_btn = Entry(
            self,
            bd=0,
            bg="#675BEB",
            fg="#000716",
            highlightthickness=0,
            background="#f6f6f6",
            justify="right",
            font=("Inter Bold", 18),
            textvariable=self.discount,
            state="readonly",
            foreground="#675CEC",
            readonlybackground="white",
        )
        self.discount_btn.place(x=611.0, y=233.0, width=168.0, height=28.0)
        self.confirm_btn = Button(
            self,
            image=self.assets["confirm"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            background="#f6f6f6",
            activebackground="#f6f6f6",
            command=self.change,
            compound="center",
            text="Đổi",
            font=("Inter SemiBold",13),
            foreground="white"
        )
        self.confirm_btn.place(x=713.0, y=100.0, width=82.0, height=40.0)

    def change(self):
        if not self.context.currentUser.position:
            alert_message('Nhân viên không được sử dụng tính năng này!')
            return
        self.discount_btn.config(state="normal")
        self.tax_btn.config(state="normal")
        self.kpi_btn.config(state="normal")
        self.confirm_btn.config(text="Xác nhận")
        self.confirm_btn.config(command=async_handler(self.confirm))

    async def confirm(self):
        self.confirm_btn.config(text="Đổi")
        self.discount_btn.config(state="readonly")
        self.tax_btn.config(state="readonly")
        self.kpi_btn.config(state="readonly")
        # kpi
        if not self.context.currentKPI:
            now = datetime.now()
            self.context.currentKPI = KPI()
            self.context.currentKPI.value = int(self.kpi.get())
            task = asyncio.create_task(add_kpi(self.context.currentKPI))
            results = await task
            if results:
                self.context.currentKPI.year = int(now.year)
                self.context.currentKPI.month = int(now.month)
                self.context.currentKPI.edit = 0
                self.kpi.set(self.context.currentKPI.value)
                success_message('Tạo KPI thành công!')
            else:
                alert_message('Tạo KPI thất bại!')
        else:
            if int(self.kpi.get()) != self.context.currentKPI.value:
                if self.context.currentKPI.edit < 3:
                    self.context.currentKPI.value = int(self.kpi.get())
                    task = asyncio.create_task(change_kpi(self.context.currentKPI))
                    results = await task
                    if results:
                        self.context.currentKPI.edit += 1
                        self.kpi.set(self.context.currentKPI.value)
                        success_message('Đổi KPI thành công!')
                else:
                    alert_message('Bạn chỉ được đổi KPI 3 lần trong 1 tháng')
            else:
                pass
        # tax
        change = False
        if int(self.tax.get()[:-1]) != self.context.currentTax:
            change = True
            self.context.currentTax = int(self.tax.get()[:-1])

        # discount
        if int(self.discount.get()[:-1]) != self.context.currentDiscount:
            change = True
            self.context.currentDiscount = int(self.discount.get()[:-1])

        if change:
            task2 = asyncio.create_task(change_other(self.context.currentTax, self.context.currentDiscount))
            results = await task2
            if not results:
                alert_message('Đổi không thành công!')
            else:
                success_message('Đổi thuế và khuyến mại thành công!')

        self.confirm_btn.config(command=self.change)
            


