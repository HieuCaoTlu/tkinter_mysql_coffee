import platform
from tkinter import *
from pathlib import Path
from datetime import datetime, timedelta
import pytz

OUTPUT_PATH = Path(__file__).parent.parent.parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/orders")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class AllOrders(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.context = self.parent.context
        self.initial_items = self.context.currentInvoice
        self.items = self.initial_items.copy()
        self.filter = ["Tất cả", "Hôm nay", "Tuần này", "Tháng này", "Năm nay"]
        label = Label(self, text="Orders", font=("Arial", 24))
        label.place(x=300, y=300, width=500, height=400)

        self.assets = {
            "back": PhotoImage(file=relative_to_assets("back.png")),
            "search_icon": PhotoImage(file=relative_to_assets("image_6.png")),
            "all": PhotoImage(file=relative_to_assets("all.png")),
            "emp": PhotoImage(file=relative_to_assets("employees.png")),
            "day": PhotoImage(file=relative_to_assets("day.png")),
            "week": PhotoImage(file=relative_to_assets("tuan.png")),
            "month": PhotoImage(file=relative_to_assets("thang.png")),
            "search_img": PhotoImage(file=relative_to_assets("long_te.png")),
            "order": PhotoImage(file=relative_to_assets("bg.png")),
            "tag": PhotoImage(file=relative_to_assets("b.png")),
            "each": PhotoImage(file=relative_to_assets("plh.png")),
            "entry": PhotoImage(file=relative_to_assets("button_2.png")),
            "choose": PhotoImage(file=relative_to_assets("choose_date.png")),
            "unchoose": PhotoImage(file=relative_to_assets("unchoose_date.png")),
        }
        canvas = Canvas(
            self,
            bg="#F6F6F6",
            height=600,
            width=840,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        button_6 = Button(
            self,
            image=self.assets["back"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.change_section("add_order"),
            background="#f6f6f6",
            activebackground="#f6f6f6",
            relief="flat",
        )
        button_6.place(x=43.0, y=60.0, width=47.0, height=45.0)
        canvas.place(x=0, y=0)
        canvas.create_text(
            113.0,
            57.0,
            anchor="nw",
            text="Toàn bộ",
            fill="#000000",
            font=("Inter Bold", 40 * -1),
        )

        canvas.create_text(
            43.0,
            115.0,
            anchor="nw",
            text="Chi tiết",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )

        canvas.create_text(
            306.0,
            115.0,
            anchor="nw",
            text="Tìm hóa đơn theo tên NV",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        ) 
        canvas.create_image(554.0, 180.0, image=self.assets["search_img"])
        canvas.create_image(766.0, 180.0, image=self.assets["search_icon"])
        canvas.create_image(161.0, 364.0, image=self.assets["order"])
        canvas.create_rectangle(57.0, 512.0, 263.0, 513.0, fill="#B3B3B3", outline="")
        canvas.create_text(
            59.0,
            425.0,
            anchor="nw",
            text="Tạm tính",
            fill="#000000",
            font=("Inter", 15 * -1),
        )

        canvas.create_text(
            58.0,
            451.0,
            anchor="nw",
            text="Thuế",
            fill="#000000",
            font=("Inter", 15 * -1),
        )

        canvas.create_text(
            58.0,
            477.0,
            anchor="nw",
            text="Khuyến mại",
            fill="#000000",
            font=("Inter", 15 * -1),
        )

        canvas.create_text(
            59.0,
            523.0,
            anchor="nw",
            text="Tổng",
            fill="#000000",
            font=("Inter Medium", 20 * -1),
        )
        canvas.create_image(87.0, 180.0, image=self.assets["tag"])
        canvas.create_text(
            58.0,
            169.0,
            anchor="nw",
            text="00001",
            fill="#FFFFFF",
            font=("Inter SemiBold", 18 * -1),
        )
        self.basic_txt = StringVar()
        self.invoice_id = StringVar()
        self.list_drink = []
        self.invoice_amount = StringVar()
        self.invoice_tax = StringVar()
        self.invoice_discount = StringVar()
        self.invoice_total = StringVar()

        basic = Label(
            self,
            bd=0,
            highlightthickness=0,
            textvariable=self.basic_txt,
            justify="right",
            cursor="arrow",
            background="white",
            anchor="e",
            wraplength=150,
            font=("Inter", 8),
        )
        basic.place(x=146.0, y=170.0, width=117.0, height=30.0)
        self.entry_search = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Inter Regular", 15),
        )
        self.entry_search.place(x=350.0, y=157.0, width=330.0, height=44.0)
        id_appear = Label(
            self,
            bd=0,
            highlightthickness=0,
            textvariable=self.invoice_id,
            justify="right",
            cursor="arrow",
            background="#675CEC",
            anchor="e",
            wraplength=150,
            foreground="white",
            font=("Inter SemiBold", 13),
        )
        id_appear.place(x=58.0, y=169.0, width=57.0, height=20.0)
        amount_appear = Label(
            self,
            bd=0,
            highlightthickness=0,
            textvariable=self.invoice_amount,
            justify="right",
            cursor="arrow",
            background="white",
            anchor="e",
            wraplength=150,
            font=("Inter", 12),
        )
        amount_appear.place(x=132.0, y=425.0, width=131.0, height=16.0)
        tax_appear = Label(
            self,
            bd=0,
            highlightthickness=0,
            textvariable=self.invoice_tax,
            justify="right",
            cursor="arrow",
            background="white",
            anchor="e",
            wraplength=150,
            font=("Inter", 12),
        )
        tax_appear.place(x=137.0, y=452.0, width=126.0, height=16.0)
        discount_appear = Label(
            self,
            bd=0,
            highlightthickness=0,
            textvariable=self.invoice_discount,
            justify="right",
            cursor="arrow",
            background="white",
            anchor="e",
            wraplength=150,
            font=("Inter", 12),
        )
        discount_appear.place(x=152.0, y=478.0, width=110.0, height=16.0)
        total_appear = Label(
            self,
            bd=0,
            highlightthickness=0,
            textvariable=self.invoice_total,
            justify="right",
            cursor="arrow",
            background="white",
            anchor="e",
            wraplength=150,
            font=("Inter Regular", 15),
        )
        total_appear.place(x=109.0, y=523.0, width=154.0, height=22.0)
        self.menu = Scrolling(self, bgr="#f6f6f6")
        self.menu.place_configure(width=500, height=295, x=303, y=280)
        self.detail = ScrollingDetail(self, bgr="white")
        self.detail.place_configure(x=58.0, y=223.0, width=220.0, height=188.0)
        self.cat_button = {}
        self.entry_search.bind("<KeyRelease>", lambda event:self.search_items(self.category))
        for i in range(len(self.filter)):
            button_cat = Button(
                self, 
                background="#f6f6f6",
                activebackground="#f6f6f6",
                borderwidth=0,
                highlightthickness=0,
                command=lambda i=i: self.search_items(self.filter[i]),
                relief="flat",
                text=self.filter[i],
                compound="center",
                font=("Inter SemiBold",10)
            )
            button_cat.config(image=self.assets["unchoose"])
            button_cat.place(x=300+i*100, y=223, width=95, height=37)
            self.cat_button[self.filter[i]]=button_cat
        self.search_items('Tất cả')

    def search_items(self, category, event=None):
        self.category = category
        for key, values in self.cat_button.items():
            if key == category:
                values.config(image=self.assets['choose'], foreground='white')
            else:
                values.config(image=self.assets['unchoose'], foreground='black')

        query = self.entry_search.get().strip().lower()
        filtered_items = self.initial_items
        
        if query:
            filtered_items = [item for item in self.initial_items if query in item.employee_name.lower()]

        vn_tz = pytz.timezone('Asia/Ho_Chi_Minh')
        for item in self.initial_items:
            if not hasattr(item, 'created_at_dt'):
                item.created_at_dt = datetime.strptime(item.created_at, '%Y-%m-%d %H:%M:%S').astimezone(vn_tz)

        now = datetime.now(vn_tz)
        if category != 'Tất cả':
            if category == 'Hôm nay':
                start_of_today = now.replace(hour=0, minute=0, second=0, microsecond=0)
                filtered_items = [item for item in filtered_items if item.created_at_dt.date() == start_of_today.date()]
            elif category == 'Tuần này':
                start_of_week = now - timedelta(days=now.weekday())
                start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
                filtered_items = [item for item in filtered_items if start_of_week <= item.created_at_dt < start_of_week + timedelta(days=7)]
            elif category == 'Tháng này':
                start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
                next_month = (start_of_month + timedelta(days=32)).replace(day=1)
                filtered_items = [item for item in filtered_items if start_of_month <= item.created_at_dt < next_month]
            elif category == 'Năm nay':
                start_of_year = now.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
                start_of_next_year = (start_of_year + timedelta(days=365)).replace(day=1)
                filtered_items = [item for item in filtered_items if start_of_year <= item.created_at_dt < start_of_next_year]

        self.items = filtered_items
        self.menu.create_buttons()

    def update_items(self):
        self.items = self.context.currentInvoice
        self.menu.create_buttons()

class ScrollFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = Canvas(
            self,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.viewPort = Frame(self.canvas)
        self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.config(width=0)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas_window = self.canvas.create_window(
            (4, 4), window=self.viewPort, anchor="nw", tags="self.viewPort"
        )

        self.viewPort.bind("<Configure>", self.onFrameConfigure)
        self.canvas.bind("<Configure>", self.onCanvasConfigure)

        self.viewPort.bind("<Enter>", self.onEnter)
        self.viewPort.bind("<Leave>", self.onLeave)
        self.onFrameConfigure(None)
        self.data_count = 0
        self.length = 0

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def onCanvasConfigure(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)

    def onMouseWheel(self, event):  #
        if platform.system() == "Windows":
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif platform.system() == "Darwin":
            self.canvas.yview_scroll(int(-1 * event.delta), "units")
        else:
            if event.num == 4:
                self.canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self.canvas.yview_scroll(1, "units")

    def setDataCount(self, count):
        self.data_count = count

    def onEnter(self, event):
        if self.data_count >= self.length:  
            self.canvas.bind_all("<MouseWheel>", self.onMouseWheel)

    def onLeave(self, event):
        self.canvas.unbind_all("<MouseWheel>")

class Scrolling(Frame):
    def __init__(self, root, bgr):

        Frame.__init__(self, root)
        self.scrollFrame = ScrollFrame(self)
        self.scrollFrame.viewPort.config(background=bgr, width=0)
        self.scrollFrame.canvas.config(bg=bgr)
        self.scrollFrame.length = 6
        self.parent = root
        self.bgr = bgr
        self.assets = {
            "choose_invoice": PhotoImage(file=relative_to_assets("choose_invoice.png")),
            "unchoose_invoice": PhotoImage(
                file=relative_to_assets("unchoose_invoice.png")
            ),
        }
        self.buttons = []
        self.scrollFrame.pack(side="top", fill="both", expand=True)

    def create_buttons(self):
        for widget in self.scrollFrame.viewPort.winfo_children():
            widget.grid_forget()
        self.scrollFrame.setDataCount(len(self.parent.items))
        for row, item in enumerate(self.parent.items):
            bt = Button(
                self.scrollFrame.viewPort,
                image=self.assets["unchoose_invoice"],
                background=self.bgr,
                activebackground=self.bgr,
                borderwidth=0,
                highlightthickness=0,
                relief="flat",
                text=f"{row+1}  {' ' * 15} {item.created_at} {' ' * 30} {int(item.total)}",
                compound="center",
                wraplength=500,
                font=("Inter Regular", 12),
                justify="left",
                anchor="w",
            )
            bt.grid(row=row, column=1, pady=7)
            bt.config(
                command=lambda current_item=item, current_button=bt: self.create_check_detail(
                    current_item, current_button
                )
            )

    def create_check_detail(self, item, button):
        for widget in self.scrollFrame.viewPort.winfo_children():
            widget.config(image=self.assets["unchoose_invoice"])
            widget.config(fg="black")
        self.parent.basic_txt.set(item.employee_name + "\n" + item.created_at)
        tempstr = []
        for each in self.parent.context.currentInvoiceDrink:
            if int(each.invoice) == int(item.id):
                tempstr.append(each)
        self.parent.invoice_id.set(item.id)
        self.parent.list_drink = tempstr
        self.parent.invoice_amount.set(f"{int(item.amount)}")
        self.parent.invoice_tax.set(f"{int(item.tax)}%")
        self.parent.invoice_discount.set(f"{int(item.discount)}%")
        self.parent.invoice_total.set(f"{int(item.total)}")
        button.config(image=self.assets["choose_invoice"])
        button.config(fg="white")
        self.parent.detail.create_buttons()

class ScrollingDetail(Frame):
    def __init__(self, root, bgr):

        Frame.__init__(self, root)
        self.scrollFrame = ScrollFrame(self)
        self.scrollFrame.viewPort.config(background=bgr, width=0)
        self.scrollFrame.canvas.config(bg=bgr)
        self.scrollFrame.length = 6
        self.parent = root
        self.bgr = bgr
        self.scrollFrame.pack(side="top", fill="both", expand=True)

    def create_buttons(self):
        for widget in self.scrollFrame.viewPort.winfo_children():
            widget.grid_forget()
        self.scrollFrame.setDataCount(len(self.parent.list_drink))
        for row, item in enumerate(self.parent.list_drink):
            bt = Label(
                self.scrollFrame.viewPort,
                background=self.bgr,
                relief="flat",
                text=f"{item.quantity} {item.drink_name}",
                font=("Inter Regular", 10),
                justify="left",
                anchor="w",
                width=20
            )
            bt.grid(row=row, column=1, pady=7)
