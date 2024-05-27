from pathlib import Path
import platform
from tkinter import Frame, PhotoImage, Canvas, Button, Entry, Scrollbar
from model.category import Category
from view.util import alert_message
OUTPUT_PATH = Path(__file__).parent.parent.parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/drinks")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class AllDrinks(Frame):

    def __init__(self, parent):
        self.parent = parent
        self.context = self.parent.context
        self.initial_items = self.context.currentDrink
        self.filter = [Category(-1,'Tất cả')] + self.context.currentCat
        self.items = self.initial_items.copy()
        self.assets = {
            "add_new": PhotoImage(file=relative_to_assets("button_6.png")),
            "item": PhotoImage(file=relative_to_assets("button_7.png")),
            "prev": PhotoImage(file=relative_to_assets("button_11.png")),
            "next": PhotoImage(file=relative_to_assets("button_10.png")),
            "search_img": PhotoImage(file=relative_to_assets("search_img.png")),
            "search_icon": PhotoImage(file=relative_to_assets("search_icon.png")),
            "choose": PhotoImage(file=relative_to_assets("mautim.png")),
            "unchoose": PhotoImage(file=relative_to_assets("mautrang.png")),
            "other": PhotoImage(file=relative_to_assets("other.png")),
            "all": PhotoImage(file=relative_to_assets("all.png")),
        }

        Frame.__init__(self, parent)
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
            text="Thực đơn",
            fill="#000000",
            font=("Inter Bold", 40 * -1),
        )

        canvas.create_text(
            43.0,
            115.0,
            anchor="nw",
            text="Danh sách",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )

        canvas.create_image(155.0, 177.0, image=self.assets["search_img"])

        self.button_add = Button(
            self,
            image=self.assets["add_new"],
            borderwidth=0,
            highlightthickness=0,
            command=self.new_items,
            relief="flat",
            background="#f6f6f6",
            activebackground="#f6f6f6",
        )
        self.button_add.place(x=634.0, y=71.0, width=152.0, height=42.0)

        self.entry_search = Entry(
            self,
            font=("Inter Medium", 14),
            bd=0,
            relief="flat",
            highlightthickness=0,
            bg="#ffffff",
        )
        self.entry_search.bind("<KeyRelease>", self.search_items)
        self.entry_search.place(x=76, y=153.0, width=134, height=46.0)
        canvas.create_image(242, 175, image=self.assets["search_icon"])

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
                font=("Inter SemiBold",13)
            )
            button_cat.config(image=self.assets["unchoose"])
            button_cat.place(x=285.0+i*103, y=153.0, width=90, height=48.0)
            
            self.cat_button[self.filter[i].id] = button_cat

        self.menu = ScrollingThree(self, img=self.assets["item"], bgr="#f6f6f6")
        self.menu.place_configure(width=753, height=320, x=32, y=232)
        self.set_category(-1)

    def handle_item_click(self, item):
        if not self.context.currentUser.position:
            alert_message('Nhân viên không được chỉnh sửa món')
            return
        self.parent.change_section("drink_info", item)

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
    
    def update_items(self):
        self.items = self.context.currentDrink
        self.menu.create_buttons(self.items)

    def new_items(self):
        if not self.context.currentUser.position:
            alert_message('Nhân viên không được thêm món')
            return
        self.parent.change_section("drink_info")

class ScrollFrameThree(Frame):
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
        if self.data_count >= 9:  
            self.canvas.bind_all("<MouseWheel>", self.onMouseWheel)

    def onLeave(self, event):
        self.canvas.unbind_all("<MouseWheel>")

class ScrollingThree(Frame):
    def __init__(self, root, img, bgr):
        Frame.__init__(self, root)
        self.scrollFrame = ScrollFrameThree(self)
        self.scrollFrame.viewPort.config(background=bgr, width=0)
        self.scrollFrame.canvas.config(bg=bgr)
        self.img = img
        self.bgr = bgr
        self.root = root
        self.buttons = []
        self.scrollFrame.pack(side="top", fill="both", expand=True)

    def create_buttons(self, data=False):
        self.data = data
        for widget in self.scrollFrame.viewPort.winfo_children():
            widget.grid_forget()
        if not self.data:
            return
        self.scrollFrame.setDataCount(len(self.data))
        for i, item in enumerate(self.data):
            row = i // 3 
            col = i % 3   
            bt = Button(
                self.scrollFrame.viewPort,
                image=self.img,
                background=self.bgr,
                activebackground=self.bgr,
                borderwidth=0,
                highlightthickness=0,
                relief="flat",
                compound="center",
                wraplength=170,
                text=f"{item.name} - {item.price//1000}k",
                font=("Inter Regular",12),
                command=lambda item=item: self.root.handle_item_click(item),
            ).grid(row=row, column=col, padx=15, pady=10)
