from tkinter import *
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/home")
from datetime import datetime, date


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Home(Frame):
    def __init__(self, parent, **kwargs):
        Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.context = self.parent.context
        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=600,
            width=840,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        canvas.place(x=0, y=0)
        canvas.create_rectangle(0.0, 0.0, 840.0, 600.0, fill="#F6F6F6", outline="")

        self.assets = {
            "small_box": PhotoImage(file=relative_to_assets("small_box.png")),
            "normal_box": PhotoImage(file=relative_to_assets("normal_box.png")),
            "large_box": PhotoImage(file=relative_to_assets("large_box.png")),
            "heavy_box": PhotoImage(file=relative_to_assets("heavy_box.png")),
        }
        self.update_items()
        canvas.create_image(112.0, 207.95877075195312, image=self.assets["small_box"])
        canvas.create_image(331.0, 207.95877075195312, image=self.assets["normal_box"])

        canvas.create_image(638.0, 207.95877075195312, image=self.assets["large_box"])

        canvas.create_text(
            65.0,
            172.95877075195312,
            anchor="nw",
            text="Số đơn",
            fill="#000000",
            font=("Inter", 18 * -1),
        )

        canvas.create_text(
            240.0,
            172.95877075195312,
            anchor="nw",
            text="Doanh thu",
            fill="#000000",
            font=("Inter", 18 * -1),
        )

        canvas.create_text(
            502.0,
            172.95877075195312,
            anchor="nw",
            text="Ưu đãi hôm nay",
            fill="#000000",
            font=("Inter", 18 * -1),
        )

        canvas.create_text(
            43.0,
            115.0,
            anchor="nw",
            text="Hôm nay",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )

        canvas.create_text(
            43.0,
            279.0,
            anchor="nw",
            text="Tổng hợp",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )

        canvas.create_image(112.0, 371.9999694824219, image=self.assets["small_box"])

        canvas.create_image(330.0, 371.9999694824219, image=self.assets["normal_box"])

        canvas.create_image(638.0, 371.9999694824219, image=self.assets["large_box"])

        canvas.create_text(
            65.0,
            336.9999694824219,
            anchor="nw",
            text="Số đơn",
            fill="#000000",
            font=("Inter", 18 * -1),
        )

        canvas.create_text(
            240.0,
            336.9999694824219,
            anchor="nw",
            text="Doanh thu",
            fill="#000000",
            font=("Inter", 18 * -1),
        )
        image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
        canvas.create_image(647.0, 344.9999694824219, image=image_image_7)

        image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
        canvas.create_image(620.0, 370.9999694824219, image=image_image_8)

        image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
        canvas.create_image(601.0, 396.9999694824219, image=image_image_9)

        canvas.create_image(243.0, 493.9999694824219, image=self.assets["heavy_box"])

        canvas.create_image(638.0, 493.9999694824219, image=self.assets["large_box"])

        image_image_12 = PhotoImage(file=relative_to_assets("image_12.png"))
        canvas.create_image(632.0, 512.9999694824219, image=image_image_12)

        image_image_13 = PhotoImage(file=relative_to_assets("image_13.png"))
        canvas.create_image(536.0, 513.0412292480469, image=image_image_13)

        canvas.create_text(
            502.0,
            458.9999694824219,
            anchor="nw",
            text="Tiến trình KPI",
            fill="#000000",
            font=("Inter", 18 * -1),
        )

        canvas.create_text(
            65.0,
            458.9999694824219,
            anchor="nw",
            text="Bán chạy nhất",
            fill="#000000",
            font=("Inter", 18 * -1),
        )
        canvas.create_text(
            43.0,
            55.0,
            anchor="nw",
            text="Trang chủ",
            fill="#000000",
            font=("Inter Bold", 40 * -1),
        )
        a = Label(
            self,
            text=str(self.today_revenue_count),
            bd=0,
            bg="white",
            fg="#675CEC",
            highlightthickness=0,
            justify="right",
            font=("Inter Bold", 20),
            anchor="e",
        )
        a.place(x=234.0, y=211.0, width=190.0, height=28.0)
        b = Label(
            self,
            text=str(self.today_discount) + "%",
            bd=0,
            bg="white",
            fg="#675CEC",
            highlightthickness=0,
            justify="right",
            font=("Inter Bold", 20),
            anchor="e",
        )
        b.place(x=504.0, y=211.0, width=270.0, height=28.0)
        c = Label(
            self,
            text=str(self.today_invoice_count),
            bd=0,
            bg="white",
            fg="#675CEC",
            highlightthickness=0,
            justify="right",
            font=("Inter Bold", 20),
            anchor="e",
        )
        c.place(x=61.0, y=211.0, width=103.0, height=28.0)
        d = Label(
            self,
            text=str(self.total_revenue_count),
            bd=0,
            bg="white",
            fg="#675CEC",
            highlightthickness=0,
            justify="right",
            font=("Inter Bold", 20),
            anchor="e",
        )
        d.place(x=243.0, y=379.0, width=181.0, height=28.0)
        e = Label(
            self,
            text=str(self.total_invoice_count),
            bd=0,
            bg="white",
            fg="#675CEC",
            highlightthickness=0,
            justify="right",
            font=("Inter Bold", 20),
            anchor="e",
        )
        e.place(x=61.0, y=379.0, width=101.0, height=28.0)
        f = Label(
            self,
            text=str(self.most_common_drink),
            bd=0,
            bg="white",
            fg="#675CEC",
            highlightthickness=0,
            justify="right",
            font=("Inter Bold", 20),
            anchor="e",
        )
        f.place(x=66.0, y=495.0, width=354.0, height=32.0)

    def update_items(self):
        self.today_invoice_count = 0
        self.today_revenue_count = 0
        self.total_revenue_count = 0
        self.month_revenue_count = 0
        today = date.today()
        for invoice in self.context.currentInvoice:
            self.total_revenue_count += int(invoice.total)
            temp = datetime.strptime(invoice.created_at, "%Y-%m-%d %H:%M:%S").date()
            if temp == today:
                self.today_invoice_count += 1
                self.today_revenue_count += int(invoice.total)
            if temp.year == today.year and temp.month == today.month:
                self.month_revenue_count += int(invoice.total)
        self.today_discount = self.context.currentDiscount
        self.total_invoice_count = len(self.context.currentInvoice)
        drink_count = {}
        for invoice in self.context.currentInvoiceDrink:
            drink = invoice.drink
            drink_count[drink] = drink_count.get(drink, 0) + invoice.quantity
        mostdrink = max(drink_count, key=drink_count.get)
        self.most_common_drink = ""
        for drink in self.context.currentDrink:
            if drink.id == mostdrink:
                self.most_common_drink = drink.name
                break
        self.kpi_progress = round((
            self.month_revenue_count / (self.context.currentKPI.value)
        ) * 100, 2) 
        self.kpi_full = Button(
            self,
            state="disabled",
            background="#EDEDED",
            highlightthickness=0,
            relief="flat",
            text=str(self.kpi_progress)+'%',
            justify='right',
            anchor='e',
            font=("Inter",12)
        )
        self.kpi_full.place(x=502.0, y=493.9999694824219, width=275, height=36.0)
        self.kpi_current = Button(
            self,
            state="disabled",
            background="#FFD53E",
            highlightthickness=0,
            relief="flat",
        )
        new_width = min(275 * (self.kpi_progress / 100), 275)
        self.kpi_current.place(x=502.0, y=493.9999694824219, width=new_width, height=36.0)
