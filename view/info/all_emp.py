from pathlib import Path
import platform
from tkinter import *

OUTPUT_PATH = Path(__file__).parent.parent.parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/info")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class AllEmp(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.context = self.parent.context
        self.initial_items = self.context.currentEmp
        self.items = self.initial_items.copy()
        self.filter = ["Tất cả", "Quản trị", "Nhân viên"]
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
        self.assets = {
            "tag": PhotoImage(file=relative_to_assets("b.png")),
            "back": PhotoImage(file=relative_to_assets("back.png")),
            "emp": PhotoImage(file=relative_to_assets("bg.png")),
            "search_icon": PhotoImage(file=relative_to_assets("image_6.png")),
            "search_img": PhotoImage(file=relative_to_assets("long_te.png")),
            "each": PhotoImage(file=relative_to_assets("plh.png")),
            "entry": PhotoImage(file=relative_to_assets("button_2.png")),
            "all": PhotoImage(file=relative_to_assets("all.png")),
            "edit": PhotoImage(file=relative_to_assets("edit.png")),
            "add": PhotoImage(file=relative_to_assets("add.png")),
            "choose": PhotoImage(file=relative_to_assets("choose_date.png")),
            "unchoose": PhotoImage(file=relative_to_assets("unchoose_date.png")),
        }
        canvas.create_text(
            113.0,
            57.0,
            anchor="nw",
            text="Danh sách nhân viên",
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
        image_2 = canvas.create_image(161.0, 364.0, image=self.assets["emp"])
        image_4 = canvas.create_image(87.0, 180.0, image=self.assets["tag"])
        canvas.create_text(
            306.0,
            115.0,
            anchor="nw",
            text="Tìm kiếm",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )
        image_3 = canvas.create_image(554.0, 180.0, image=self.assets["search_img"])
        canvas.create_text(
            58.0,
            323.0,
            anchor="nw",
            text="Tài khoản:",
            fill="#000000",
            font=("Inter", 15 * -1)
        )
        canvas.create_text(
            58.0,
            290.0,
            anchor="nw",
            text="Tham gia:",
            fill="#000000",
            font=("Inter", 15 * -1)
        )
        canvas.create_text(
            58.0,
            257.0,
            anchor="nw",
            text="Giới tính:",
            fill="#000000",
            font=("Inter", 15 * -1)
        )
        canvas.create_text(
            58.0,
            356.0,
            anchor="nw",
            text="Chức vụ:",
            fill="#000000",
            font=("Inter", 15 * -1)
        )
        self.entry_search = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Inter Regular", 15),
        )
        self.entry_search.place(x=350.0, y=157.0, width=330.0, height=44.0)
        canvas.create_image(766.0, 180.0, image=self.assets["search_icon"])
        button_6 = Button(
            self,
            image=self.assets["back"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.change_section("info"),
            background="#f6f6f6",
            activebackground="#f6f6f6",
            relief="flat",
        )
        button_6.place(x=43.0, y=60.0, width=47.0, height=45.0)
        self.emp = None
        button_1 = Button(
            self,
            image=self.assets["edit"],
            borderwidth=0,
            highlightthickness=0,
            command=self.editEmployee,
            relief="flat",
            activebackground="white",
            background="white"
        )
        button_1.place(x=170.0, y=512.0, width=85.0, height=45.0)
        button_5 = Button(
            self,
            image=self.assets["add"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.change_section("emp_info"),
            relief="flat",
        )
        button_5.place(x=645.0, y=65.0, width=152.0, height=42.0)
        self.emp_id = StringVar()
        self.emp_name = StringVar()
        self.emp_gender = StringVar()
        self.emp_username = StringVar()
        self.emp_position = StringVar()
        self.emp_date = StringVar()
        id_appear = Label(
            self,
            bd=0,
            highlightthickness=0,
            textvariable=self.emp_id,
            justify="right",
            cursor="arrow",
            background="#675CEC",
            anchor="w",
            wraplength=150,
            font=("Inter SemiBold", 13),
            fg='white'
        )
        id_appear.place(x=52.0,y=169.0,width=70.0,height=20.0)
        name_appear = Label(
            self,
            bd=0,
            highlightthickness=0,
            textvariable=self.emp_name,
            justify="left",
            cursor="arrow",
            background="white",
            anchor="w",
            wraplength=200,
            font=("Inter SemiBold", 13)
        )
        name_appear.place(x=59.0,y=223.0,width=170.0,height=22.0)
        gender_appear = Label(
            self,
            bd=0,
            highlightthickness=0,
            textvariable=self.emp_gender,
            justify="left",
            cursor="arrow",
            background="white",
            anchor="w",
            wraplength=150,
            font=("Inter", 11)
        )
        gender_appear.place(x=132.0, y=257.0, width=123.0, height=16.0)
        username_appear = Label(
            self,
            bd=0,
            highlightthickness=0,
            textvariable=self.emp_username,
            justify="left",
            cursor="arrow",
            background="white",
            anchor="w",
            wraplength=150,
            font=("Inter", 11)
        )
        username_appear.place(x=140.0, y=324.0, width=107.0, height=20.0)
        position_appear = Label(
            self,
            bd=0,
            highlightthickness=0,
            textvariable=self.emp_position,
            justify="left",
            cursor="arrow",
            background="white",
            anchor="w",
            wraplength=150,
            font=("Inter", 11)
        )
        position_appear.place(x=140.0, y=357.0, width=107.0, height=16.0)
        date_appear = Label(
            self,
            bd=0,
            highlightthickness=0,
            textvariable=self.emp_date,
            justify="left",
            cursor="arrow",
            background="white",
            anchor="w",
            wraplength=150,
            font=("Inter", 11)
        )
        date_appear.place(x=140.0, y=291.0, width=107.0, height=16.0)
        self.menu = Scrolling(self, bgr="#f6f6f6")
        self.menu.place_configure(width=500, height=295, x=303, y=280)
        self.cat_button = {}
        self.category = 'Tất cả'
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
                font=("Inter SemiBold", 10),
            )
            button_cat.config(image=self.assets["unchoose"])
            button_cat.place(x=300 + i * 100, y=223, width=95, height=37)
            self.cat_button[self.filter[i]] = button_cat
        self.search_items('Tất cả')

    def search_items(self,category, event=None ):
        self.category = category
        for key, values in self.cat_button.items():
            if key == category:
                values.config(image=self.assets["choose"], foreground="white")
            else:
                values.config(image=self.assets["unchoose"], foreground="black")

        query = self.entry_search.get().strip().lower()
        filtered_items = self.initial_items

        if query:
            filtered_items = [
                item
                for item in self.initial_items
                if query in item.name.lower()
            ]

        if category != "Tất cả" and category in self.filter:
            if category == "Quản trị":
                filtered_items = [item for item in filtered_items if item.position == 1]
            elif category == "Nhân viên":
                filtered_items = [item for item in filtered_items if item.position == 0]
        self.items = filtered_items
        self.menu.create_buttons()

    def update_items(self):
        self.items = self.context.currentEmp
        self.menu.create_buttons()
        self.emp_id.set('')
        self.emp_name.set('')
        self.emp_gender.set('')
        self.emp_username.set('')
        self.emp_position.set('')
        self.emp_date.set('')

    def editEmployee(self):
        if self.emp:
            self.parent.change_section("emp_info", self.emp)

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
            appear = "Quản trị"
            if item.position == 0:
                appear = "Nhân viên"
            bt = Button(
                self.scrollFrame.viewPort,
                image=self.assets["unchoose_invoice"],
                background=self.bgr,
                activebackground=self.bgr,
                borderwidth=0,
                highlightthickness=0,
                relief="flat",
                text=f"{item.name} - {appear}",
                compound="center",
                wraplength=500,
                font=("Inter Regular", 12),
                justify="left",
                anchor="w",
            )
            bt.grid(
                row=row,
                column=1,
                pady=7,
                padx=(0, 30),
            )
            bt.config(
                command=lambda current_item=item, current_button=bt: self.create_check_detail(
                    current_item, current_button
                )
            )

    def create_check_detail(self, item, button):
        for widget in self.scrollFrame.viewPort.winfo_children():
            widget.config(image=self.assets["unchoose_invoice"])
            widget.config(fg="black")
        self.parent.emp_id.set(item.id)
        self.parent.emp_gender.set(f"{"Nam" if item.gender else "Nữ"}")
        self.parent.emp_position.set(f"{"Quản trị" if item.position else "Nhân viên"}")
        self.parent.emp_date.set(f"{item.created_at}")
        self.parent.emp_username.set(f"{item.username}")
        self.parent.emp_name.set(item.name)
        self.parent.emp = item
        button.config(image=self.assets["choose_invoice"])
        button.config(fg="white")
