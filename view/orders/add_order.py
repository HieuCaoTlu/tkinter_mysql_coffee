import platform
from tkinter import *
from pathlib import Path
from model.category import Category
from model.invoice import Invoice, InvoiceDrink
import asyncio
from async_tkinter_loop import async_handler
from controller.invoice_ctl import add_invoice
from view.util import alert_message, success_message

OUTPUT_PATH = Path(__file__).parent.parent.parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/orders")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class AddOrder(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.context = self.parent.context
        self.initial_items = self.context.currentDrink
        self.filter = [Category(-1,'Tất cả')] + self.context.currentCat
        self.items = self.initial_items.copy()
        self.orders = []
        self.discount = self.context.currentDiscount
        self.tax = self.context.currentTax
        self.amount = 0
        self.total = 0
        canvas = Canvas(
            self,
            bg="#F6F6F6",
            height=600,
            width=840,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        canvas.place(x=0, y=0)
        canvas.create_text(
            43.0,
            55.0,
            anchor="nw",
            text="Đơn mua",
            fill="#000000",
            font=("Inter Bold", 40 * -1),
        )

        canvas.create_text(
            43.0,
            115.0,
            anchor="nw",
            text="Thêm đơn",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )

        canvas.create_text(
            431.0,
            115.0,
            anchor="nw",
            text="Tìm món",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )

        self.assets = {
            "all_order": PhotoImage(file=relative_to_assets("button_10.png")),
            "search_img": PhotoImage(file=relative_to_assets("search.png")),
            "search_icon": PhotoImage(file=relative_to_assets("image_6.png")),
            "add_bgr": PhotoImage(file=relative_to_assets("image_2.png")),
            "menu": PhotoImage(file=relative_to_assets("image_1.png")),
            "drink": PhotoImage(file=relative_to_assets("item.png")),
            "entry": PhotoImage(file=relative_to_assets("button_2.png")),
            "confirm": PhotoImage(file=relative_to_assets("button_9.png")),
            "choose": PhotoImage(file=relative_to_assets("choose.png")),
            "unchoose": PhotoImage(file=relative_to_assets("unchoose.png")),
        }

        all_orders_button = Button(
            self,
            image=self.assets["all_order"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.change_section("orders"),
            relief="flat",
        )
        all_orders_button.place(x=634.0, y=71.0, width=152.0, height=42.0)
        canvas.create_image(217.0, 364.0, image=self.assets["add_bgr"])
        canvas.create_image(614.0, 180.0, image=self.assets["search_img"])
        canvas.create_image(766.0, 180.0, image=self.assets["search_icon"])
        self.entry_search = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Inter Regular", 15),
        )
        canvas.create_text(
            68.0,
            370.0,
            anchor="nw",
            text="Tạm tính",
            fill="#000000",
            font=("Inter", 15 * -1),
        )
        self.amount_txt = Label(
            self,
            font=("Inter", 15 * -1),
            justify="right",
            text=str(0),
            anchor="e",
            compound="center",
            background='white'
        )
        self.amount_txt.place(x=368, y=380, anchor="e", width=218,height=16)
        canvas.create_text(
            339.0,
            396.0,
            anchor="nw",
            text=self.tax,
            fill="#000000",
            font=("Inter", 15 * -1),
        )

        canvas.create_text(
            298.0,
            460.0,
            anchor="nw",
            text="33.000",
            fill="#000000",
            font=("Inter Medium", 20 * -1),
        )

        canvas.create_text(
            67.0,
            396.0,
            anchor="nw",
            text="Thuế",
            fill="#000000",
            font=("Inter", 15 * -1),
        )
        self.tax_txt = Label(
            self,
            font=("Inter", 15 * -1),
            justify="right",
            text=str(self.tax)+'%',
            anchor="e",
            compound="center",
            background='white'
        )
        self.tax_txt.place(x=368, y=407, anchor="e", width=218,height=16)
        self.discount_txt = Label(
            self,
            font=("Inter", 15 * -1),
            justify="right",
            text=str(self.discount)+'%',
            anchor="e",
            compound="center",
            background='white'
        )
        self.discount_txt.place(x=368, y=432, anchor="e", width=100,height=16)
        self.total_txt = Label(
            self,
            font=("Inter", 25 * -1),
            justify="right",
            text=str(self.total),
            anchor="e",
            compound="center",
            background='white'
        )
        self.total_txt.place(x=368, y=470, anchor="e", width=230,height=25)
        canvas.create_text(
            346.0,
            422.0,
            anchor="nw",
            text=self.discount,
            fill="#000000",
            font=("Inter", 15 * -1),
        )

        canvas.create_text(
            67.0,
            422.0,
            anchor="nw",
            text="Khuyến mại",
            fill="#000000",
            font=("Inter", 15 * -1),
        )

        canvas.create_text(
            68.0,
            460.0,
            anchor="nw",
            text="Tổng",
            fill="#000000",
            font=("Inter Medium", 20 * -1),
        )

        confirm = Button(
            self,
            image=self.assets["confirm"],
            borderwidth=0,
            highlightthickness=0,
            background="white",
            activebackground="white",
            command=async_handler(self.executePay),
            relief="flat",
        )
        self.cat_button = dict()
        for i in range(len(self.filter)):
            button_cat = Button(
                self, 
                background="#f6f6f6",
                activebackground="#f6f6f6",
                borderwidth=0,
                highlightthickness=0,
                command=lambda i=i: self.set_category(self.filter[i].id),
                relief="flat",
                text=self.filter[i].name,
                compound="center",
                font=("Inter SemiBold",10)
            )
            button_cat.config(image=self.assets["unchoose"])
            button_cat.place(x=431+i*76, y=223, width=61, height=37)
            
            self.cat_button[self.filter[i].id] = button_cat

        self.entry_search.place(x=472.0, y=157.0, width=256.0, height=44.0)
        self.menu = Scrolling(self, img=self.assets["drink"], bgr="#f6f6f6")
        self.menu.place_configure(width=500, height=295, x=431.0, y=280.0)
        self.ordermenu = ScrollingOrder(self, img=self.assets["entry"], bgr="white")
        self.ordermenu.place_configure(width=322, height=190, x=70, y=175)
        confirm.place(x=125.0, y=501.0, width=183.0, height=50.0)
        self.entry_search.bind("<KeyRelease>", self.search_items)
        self.set_category(-1)

    async def executePay(self):
        list_order = self.orders.copy()
        invoice = Invoice()
        invoice.amount = self.amount
        invoice.tax = self.tax
        invoice.discount = self.discount
        invoice.total = self.total
        invoice.employee = self.context.currentUser
        task = asyncio.create_task(add_invoice(invoice, list_order))
        result = await task
        if result:
            invoice.employee_name = self.context.currentUser.name
            self.context.currentInvoice.append(invoice)
            for each in list_order:
                each.invoice = invoice.id
                each.drink_name = each.drink.name
                each.price = each.drink.price
                self.context.currentInvoiceDrink.append(each)
            success_message('Thanh toán thành công!')
            self.orders = []
            self.ordermenu.create_buttons()
            self.amount = 0
            self.total = 0
            self.amount_txt.config(text=str(0))
            self.total_txt.config(text=str(0))
        else:
            alert_message('Thanh toán thất bại')

    def search_items(self, event):
        query = self.entry_search.get().strip().lower()
        filtered_items = self.initial_items
        if query:
            filtered_items = [item for item in self.initial_items if query in item.name.lower()]
        if self.category != -1:
            filtered_items = [item for item in filtered_items if item.category == self.category]

        if filtered_items:
            self.items = filtered_items
            self.menu.create_buttons(self.items)
        else:
            self.items = []
            self.menu.create_buttons(self.items)  

    def set_category(self, category):
        self.category = category
        for key, values in self.cat_button.items():
            if key == category:
                values.config(image=self.assets['choose'],foreground='white')
            else:
                values.config(image=self.assets['unchoose'],foreground='black')
        if self.category != -1:
            filtered_items = [item for item in self.initial_items if item.category == self.category]
            self.items = filtered_items
        else:
            self.items = self.initial_items
        self.search_items(event=None)

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
    def __init__(self, root, img, bgr):

        Frame.__init__(self, root)
        self.scrollFrame = ScrollFrame(self)
        self.scrollFrame.viewPort.config(background=bgr, width=0)
        self.scrollFrame.canvas.config(bg=bgr)
        self.scrollFrame.length = 6
        self.img = img
        self.bgr = bgr
        self.parent = root
        self.buttons = []
        self.scrollFrame.pack(side="top", fill="both", expand=True)

    def create_buttons(self, data=False):
        self.data = data
        for widget in self.scrollFrame.viewPort.winfo_children():
            widget.grid_forget()
        if not self.data:
            return
        self.scrollFrame.setDataCount(len(self.data))
        for row, item in enumerate(self.data):
            a = row
            bt = Button(
                self.scrollFrame.viewPort,
                image=self.img,
                background=self.bgr,
                activebackground=self.bgr,
                borderwidth=0,
                highlightthickness=0,
                relief="flat",
                text=f"{item.name} - {item.price//1000}k",
                compound="center",
                wraplength=250,
                command=lambda item=item: self.addToOrder(item),
                font=("Inter Regular",12),
                justify="left",
                anchor="w"
            ).grid(row=row, column=1, pady=7)

    def addToOrder(self, item):
        tempReach = []
        temp = None
        for each in self.parent.orders:
            tempReach.append(each.drink)
        if item not in tempReach:
            temp = InvoiceDrink()
            temp.drink = item
            temp.quantity = 0
            temp.drink_name = item.name
            temp.price = item.price
            self.parent.orders.append(temp)
        else:
            for each in self.parent.orders:
                if each.drink == item:
                    temp = each
                    break
        self.parent.ordermenu.add_quantity(temp)
        
class ScrollingOrder(Frame):
    def __init__(self, root, img, bgr):
        Frame.__init__(self, root)
        self.scrollFrame = ScrollFrame(self)
        self.scrollFrame.viewPort.config(background=bgr, width=0)
        self.scrollFrame.canvas.config(bg=bgr)
        self.scrollFrame.length = 5
        self.img = img
        self.bgr = bgr
        self.parent = root
        self.buttons = []
        self.scrollFrame.pack(side="top", fill="both", expand=True)
        self.assets = {
            "add": PhotoImage(file=relative_to_assets("add.png")),
            "sub": PhotoImage(file=relative_to_assets("sub.png")),
        }

    def create_buttons(self):
        for widget in self.scrollFrame.viewPort.winfo_children():
            widget.grid_forget()
        if not self.parent.orders:
            return
        self.scrollFrame.setDataCount(len(self.parent.orders))
        for row, item in enumerate(self.parent.orders):
            sub_button = Button(
                self.scrollFrame.viewPort,
                image=self.assets['sub'],
                command=lambda item=item: self.subtract_quantity(item),
                font=("Inter Regular", 12),
                background=self.bgr,
                activebackground=self.bgr,
                borderwidth=0,
                highlightthickness=0,
                relief="flat"
            )
            sub_button.grid(row=row, column=0, pady=7)

            item_label = Label(
                self.scrollFrame.viewPort,
                text=f"{item.quantity} {item.drink.name}",
                background=self.bgr,
                font=("Inter Regular", 12),
                anchor="w",
                justify="left",
                width=20
            )
            item_label.grid(row=row, column=1, pady=7, padx=10)

            add_button = Button(
                self.scrollFrame.viewPort,
                image=self.assets['add'],
                command=lambda item=item: self.add_quantity(item),
                font=("Inter Regular", 12),
                background=self.bgr,
                activebackground=self.bgr,
                borderwidth=0,
                highlightthickness=0,
                relief="flat"
            )
            add_button.grid(row=row, column=2, pady=7)

    def updateOrder(self, item, change):
        item.quantity += change
        self.parent.amount += item.drink.price * change
        if item.quantity <= 0:
            self.parent.orders.remove(item)
        self.parent.amount_txt.config(text=str(self.parent.amount))
        self.parent.total = self.parent.amount * (1 - (self.parent.tax / 100) - (self.parent.discount / 100))
        self.parent.total_txt.config(text=str(int(self.parent.total)))
        self.create_buttons()

    def subtract_quantity(self, item):
        self.updateOrder(item, -1)

    def add_quantity(self, item):
        self.updateOrder(item, 1)

