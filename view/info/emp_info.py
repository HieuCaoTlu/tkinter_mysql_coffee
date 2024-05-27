from pathlib import Path
from tkinter import *
from controller.employee_ctl import add_employee, change_employee, delete_employee
from model.employee import Employee
import asyncio
from view.util import alert_message, success_message
from async_tkinter_loop import async_handler

OUTPUT_PATH = Path(__file__).parent.parent.parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/info")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class EmpInfo(Frame):

    def __init__(self, parent, emp=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.emp = emp if emp else Employee()
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
            "back": PhotoImage(file=relative_to_assets("back.png")),
            "add_emp": PhotoImage(file=relative_to_assets("add_emp.png")),
            "del": PhotoImage(file=relative_to_assets("del.png")),
            "female": PhotoImage(file=relative_to_assets("female.png")),
            "male": PhotoImage(file=relative_to_assets("male.png")),
            "choose": PhotoImage(file=relative_to_assets("choose.png")),
            "unchoose": PhotoImage(file=relative_to_assets("unchoose.png")),
            "choose_g": PhotoImage(file=relative_to_assets("choose_gender.png")),
            "unchoose_g": PhotoImage(file=relative_to_assets("unchoose_gender.png")),
            "verify": PhotoImage(file=relative_to_assets("verify.png")),
            "place": PhotoImage(file=relative_to_assets("place.png")),
        }
        if self.emp.id:
            canvas.create_text(
                113.0,
                57.0,
                anchor="nw",
                text="Sửa thông tin nhân viên",
                fill="#000000",
                font=("Inter Bold", 40 * -1),
            )
        else:
            canvas.create_text(
                113.0,
                57.0,
                anchor="nw",
                text="Thêm nhân viên",
                fill="#000000",
                font=("Inter Bold", 40 * -1),
            )
        button_6 = Button(
            self,
            image=self.assets["back"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.change_section("all_emp"),
            background="#f6f6f6",
            activebackground="#f6f6f6",
            relief="flat",
        )
        button_6.place(x=43.0, y=60.0, width=47.0, height=45.0)

        if self.emp.id:
            button_2 = Button(
                self,
                image=self.assets["verify"],
                borderwidth=0,
                highlightthickness=0,
                command=async_handler(self.executeUpdate),
                relief="flat",
                background="#f6f6f6",
                activebackground="#f6f6f6",
            )
            button_2.place(x=559.0, y=499.0, width=167.0, height=61.0)
        else:
            button_1 = Button(
                self,
                image=self.assets["add_emp"],
                borderwidth=0,
                highlightthickness=0,
                command=async_handler(self.executeAdd),
                relief="flat",
                background="#f6f6f6",
                activebackground="#f6f6f6",
            )
            button_1.place(x=559.0, y=499.0, width=152.0, height=61.0)

        if self.emp.id:
            button_3 = Button(
                self,
                image=self.assets["del"],
                borderwidth=0,
                highlightthickness=0,
                command=async_handler(self.executeDelete),
                relief="flat",
                background="#f6f6f6",
                activebackground="#f6f6f6",
            )
            button_3.place(x=410.0, y=499.0, width=122.0, height=61.0)

        self.quantri_btn = Button(
            self,
            image=self.assets['unchoose'],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.set_emp_position(1),
            compound="center",
            text="Quản trị",
            font=("Inter SemiBold",13),
            relief="flat",
            background="#f6f6f6",
            activebackground="#f6f6f6",
        )
        self.quantri_btn.place(x=153.0, y=158.0, width=120.0, height=48.0)

        self.nhanvien_btn = Button(
            self,
            image=self.assets['unchoose'],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.set_emp_position(0),
            compound="center",
            text="Nhân viên",
            font=("Inter SemiBold",13),
            relief="flat",
            background="#f6f6f6",
            activebackground="#f6f6f6",
        )
        self.nhanvien_btn.place(x=296.0, y=158.0, width=120.0, height=48.0)
        if self.emp.position:
            self.quantri_btn.config(image=self.assets['choose'])
            self.quantri_btn.config(fg='white')
        else:
            self.nhanvien_btn.config(image=self.assets['choose'])
            self.nhanvien_btn.config(fg='white')
        self.male_btn = Button(
            self,
            image=self.assets["unchoose_g"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.set_emp_gender(1),
            relief="flat",
            compound="center",
            text="Nam",
            font=("Inter SemiBold",13),
            background="#f6f6f6",
            activebackground="#f6f6f6",
        )
        self.male_btn.place(x=550.0, y=158.0, width=85, height=48.0)

        self.female_btn = Button(
            self,
            image=self.assets["unchoose_g"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.set_emp_gender(0),
            compound="center",
            relief="flat",
            text="Nữ",
            font=("Inter SemiBold",13),
            background="#f6f6f6",
            activebackground="#f6f6f6",
        )
        self.female_btn.place(x=645.0, y=158.0, width=85, height=48.0)
        if self.emp.gender:
            self.male_btn.config(image=self.assets['choose_g'])
            self.male_btn.config(fg='white')
        else:
            self.female_btn.config(image=self.assets['choose_g'])
            self.female_btn.config(fg='white')            
        canvas.create_image(439.0, 263.0, image=self.assets["place"])
        self.name_txt = StringVar()
        self.username_txt = StringVar()
        self.psw_txt = StringVar()
        if self.emp.id:
            self.name_txt.set(emp.name)
            self.username_txt.set(emp.username)
            self.psw_txt.set(emp.psw)
        entry_1 = Entry(
            self,
            bd=0,
            bg="#ffffff",
            font=("Inter Regular", 15),
            fg="#000716",
            highlightthickness=0,
            textvariable=self.name_txt
        )
        entry_1.place(x=180.0, y=249.0, width=470, height=28.0)

        canvas.create_text(
            48.0,
            171.0,
            anchor="nw",
            text="Vai trò",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )

        canvas.create_text(
            452.0,
            171.0,
            anchor="nw",
            text="Giới tính",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )

        canvas.create_text(
            43.0,
            251.0,
            anchor="nw",
            text="Họ tên",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )

        image_2 = canvas.create_image(439.0, 352.0, image=self.assets["place"])

        entry_2 = Entry(
            self,
            bd=0,
            bg="#ffffff",
            font=("Inter Regular", 15),
            fg="#000716",
            highlightthickness=0,
            textvariable=self.username_txt

        )
        entry_2.place(x=180.0, y=338.0, width=470, height=28.0)

        canvas.create_text(
            43.0,
            340.0,
            anchor="nw",
            text="Tài khoản",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )

        image_3 = canvas.create_image(439.0, 443.0, image=self.assets["place"])

        entry_3 = Entry(
            self,
            bd=0,
            bg="#ffffff",
            font=("Inter Regular", 15),
            fg="#000716",
            highlightthickness=0,
            show='*',
            textvariable=self.psw_txt

        )
        entry_3.place(x=178.0, y=425.0, width=470, height=28.0)

        canvas.create_text(
            43.0,
            431.0,
            anchor="nw",
            text="Mật khẩu",
            fill="#000000",
            font=("Inter SemiBold", 20 * -1),
        )

    def set_emp_position(self, position):
        self.emp.position = position
        if position:
            self.quantri_btn.config(image=self.assets['choose'])
            self.quantri_btn.config(fg='white')
            self.nhanvien_btn.config(image=self.assets['unchoose'])
            self.nhanvien_btn.config(fg='black')
        else:
            self.nhanvien_btn.config(image=self.assets['choose'])
            self.nhanvien_btn.config(fg='white')
            self.quantri_btn.config(image=self.assets['unchoose'])
            self.quantri_btn.config(fg='black')            

    def set_emp_gender(self, gender):
        self.emp.gender = gender
        if gender:
            self.male_btn.config(image=self.assets['choose_g'])
            self.male_btn.config(fg='white')
            self.female_btn.config(image=self.assets['unchoose_g'])
            self.female_btn.config(fg='black')
        else:
            self.female_btn.config(image=self.assets['choose_g'])
            self.female_btn.config(fg='white')
            self.male_btn.config(image=self.assets['unchoose_g'])
            self.male_btn.config(fg='black') 

    async def executeUpdate(self):
        self.emp.name = self.name_txt.get()
        self.emp.username = self.username_txt.get()
        self.emp.psw = self.psw_txt.get()
        task = asyncio.create_task(change_employee(self.emp))
        result = await task
        if result:
            success_message('Thay đổi thông tin thành công!')
            for each in self.parent.context.currentEmp:
                if each.id == self.emp.id:
                    each = self.emp
                    break
        else:
            alert_message('Thay đổi thông tin thất bại')

    async def executeAdd(self):
        self.emp.name = self.name_txt.get()
        self.emp.username = self.username_txt.get()
        self.emp.psw = self.psw_txt.get()
        task = asyncio.create_task(add_employee(self.emp))
        results = await task
        if results:
            alert_message('Thêm nhân viên thành công!')
            self.parent.change_section('emp_info',self.emp)
            self.parent.context.currentEmp.append(self.emp)
        else:
            alert_message('Thêm nhân viên thất bại')

    async def executeDelete(self):
        task = asyncio.create_task(delete_employee(self.emp.id))
        result = await task
        if result:
            success_message('Đã xóa đối tượng khỏi danh sách nhân viên!')
            for i, each in enumerate(self.parent.context.currentEmp):
                if each.id == self.emp.id:
                    del self.parent.context.currentEmp[i]
                    break
            self.parent.change_section('all_emp')
        else:
            alert_message('Hành động xóa thất bại!')