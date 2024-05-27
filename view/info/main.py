from tkinter import Frame
from .all_info import AllInfo
from .all_emp import AllEmp
from .emp_info import EmpInfo
from view.util import alert_message
class Info(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.context = self.parent.context
        self.sections = {
            "info": AllInfo(self),
            "all_emp": AllEmp(self),
            "emp_info": EmpInfo(self)
        }
        self.change_section("info")

    def change_section(self, name, emp=None):
        if name == "emp_info":
            self.sections["emp_info"] = EmpInfo(self, emp)
        if name == "all_emp":
            if self.context.currentUser.position:
                self.sections["all_emp"].update_items()
            else:
                alert_message("Nhân viên không được truy cập mục này")
                return
        for section in self.sections.values():
            section.place_forget()
        self.sections[name].place(x=0, y=0, width=1000, height=600)
        self.sections[name].tkraise()