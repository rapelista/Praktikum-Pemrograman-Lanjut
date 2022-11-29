from tkinter import *


class App(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.login_page()
        self.pack()

    def alert(self, msg):
        alert = Tk()
        Message(alert, text=msg, background="red").pack()
        alert.mainloop()

    def login_page(self):
        self.login_frame = Frame(self)
        self.login_info = {}
        for i, label in enumerate(["Username", "Password"]):
            self.login_info[label.lower()] = StringVar()
            Label(self.login_frame, text=label, width=10,
                  anchor=W).grid(column=0, row=i)
            Entry(self.login_frame, textvariable=self.login_info[label.lower()]).grid(
                column=1, row=i)
        _ = Frame(self.login_frame)
        Button(_, text="Masuk", command=self.login_btn).grid(column=0, row=0)
        Button(_, text="Cancel", command=self.master.destroy).grid(
            column=1, row=0)
        _.grid(columnspan=2)
        self.login_frame.pack()

    def login_btn(self):
        db_uname, db_pass = ["akmal", "123"]

        username, password = [value.get()
                              for value in self.login_info.values()]
        if db_uname == username and db_pass == password:
            self.login_frame.destroy()
            self.welcome_page(username)
        else:
            if db_pass != password:
                self.alert("salah password")

    def welcome_page(self, username):
        self.welcome_frame = Frame(self)
        Label(self.welcome_frame,
              text=f"Halo, selamat datang {username.capitalize()}!").pack()
        Button(self.welcome_frame, text="Keluar",
               command=self.welcome_btn).pack()
        self.welcome_frame.pack()

    def welcome_btn(self):
        self.welcome_frame.destroy()
        self.login_page()


window = Tk()
window.title("Pertemuan 10")
app = App(window)
window.mainloop()
