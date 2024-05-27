from tkinter import messagebox

def alert_message(message):
    messagebox.showwarning(title='Thông báo', message=message)

def success_message(message):
    messagebox.showinfo(title="Thành công", message=message)