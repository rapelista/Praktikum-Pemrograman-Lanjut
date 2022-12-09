from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import datetime
import csv
import os


class Label(Label):

    def __init__(
        self,
        master,
        text=None,
        width=None,
        var=None,
        bg=None,
        fg=None,
        size=None,
        weight='normal'
    ):
        super().__init__(
            master,
            text=None if text is None else text,
            textvariable=None if var is None else var,
            bg="#081c34" if var is None else bg,
            width=None if width is None else width,
            font=Font(family="Arial", size=20, weight=weight) if size is None else Font(
                family="Arial", size=size, weight=weight),
            anchor=CENTER,
            fg=None if fg is None else fg,
        )


class Button(Button):

    def __init__(
        self,
        master,
        text=None,
        command=None
    ):
        super().__init__(
            master,
            text=None if text is None else text,
            command=None if command is None else command
        )


class App(Frame):

    def __init__(self, master):
        super().__init__(master)

        self.title = "Restaurant Management System"
        self.file = "data.csv"
        self.data = {
            "menu": [
                # nama | harga | qty | total
                ["Nasi", 10000, StringVar(), StringVar()],
                ["Ayam Goreng", 15000, StringVar(), StringVar()],
                ["Ayam Bakar", 20000, StringVar(), StringVar()],
                ["Tahu Telur", 10000, StringVar(), StringVar()],
                ["Tahu", 5000, StringVar(), StringVar()],
                ["Tempe", 5000, StringVar(), StringVar()],
            ],
            "total_bayar": StringVar(),
            "nominal_bayar": StringVar(),
            "nominal_kembalian": StringVar()
        }

        if os.path.exists(self.file):
            os.remove(self.file)

        with open(self.file, "w") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow(["Rincian", "Total Harga",
                            "Uang Bayar", "Kembalian", "Tanggal"])

        master.title(self.title)
        self.reset()
        self.main()
        self.data["nominal_bayar"].trace_add(
            'write', self.nominal_handler)
        self.config(bg="#081c34")
        self.pack()

    def main(self):
        self.main_frame = Frame(self, bg="#081c34")
        Label(
            self.main_frame, self.title.upper(),
            size=35,
            fg="#ebc304",
            weight='bold'
        ).grid()
        Label(
            self.main_frame,
            "Menu - UAP Pemrograman Lanjut",
            weight='bold',
            size=25
        ).grid(pady=(20, 20))
        _ = Frame(self.main_frame, bg="#081c34")
        for row, menu in enumerate(self.data["menu"]):
            menu[2].set("0")
            menu[3].set("Rp0")
            Label(
                _,
                f"{menu[0]} - Rp{menu[1]}",
                25
            ).grid(column=0, row=row + 2)
            Button(
                _,
                "-",
                lambda menu=menu: self.btn_minus(menu)
            ).grid(column=1, row=row + 2)
            Button(
                _,
                "+",
                lambda menu=menu: self.btn_plus(menu)
            ).grid(column=2, row=row + 2)
            Entry(
                _,
                bg="white",
                fg="black",
                width=3,
                textvariable=menu[2],
                justify="center"
            ).grid(column=3, row=row + 2, padx=(10, 0))
            Label(
                _,
                var=menu[3]
            ).grid(column=4, row=row + 2)
        Label(
            _,
            f"Total",
            25
        ).grid(column=0, row=2+len(self.data["menu"]), pady=(10, 0))
        Label(
            _,
            var=self.data["total_bayar"]
        ).grid(column=4, row=2+len(self.data["menu"]))
        Label(
            _,
            f"Nominal Bayar",
            25
        ).grid(column=0, row=3+len(self.data["menu"]))
        Entry(
            _,
            bg="white",
            fg="black",
            width=25,
            justify="center",
            textvariable=self.data["nominal_bayar"]
        ).grid(column=4, row=3+len(self.data["menu"]))
        Label(
            _,
            f"Nominal Kembalian",
            25
        ).grid(column=0, row=4+len(self.data["menu"]))
        Label(
            _,
            var=self.data["nominal_kembalian"]
        ).grid(column=4, row=4+len(self.data["menu"]))
        _.grid()
        Button(
            self.main_frame,
            "BAYAR",
            command=self.btn_pay
        ).grid(pady=(20, 0))
        self.main_frame.grid(padx=(20, 20), pady=(20, 20))

    def nominal_handler(self, *args):
        nominal_bayar = self.data["nominal_bayar"].get()
        self.data["nominal_bayar"].set(nominal_bayar)
        self.update_kembalian()

    def set_menu(self, menu, qty):
        menu[2].set(f"{qty}")
        menu[3].set(f"Rp{qty * menu[1]}")

    def btn_plus(self, menu):
        qty = int(menu[2].get())
        qty += 1
        self.set_menu(menu, qty)
        self.update_total()

    def btn_minus(self, menu):
        qty = int(menu[2].get())
        if qty == 0:
            return
        qty -= 1
        self.set_menu(menu, qty)
        self.update_total()

    def update_total(self):
        total_bayar = 0
        for _, harga, qty, __ in self.data["menu"]:
            total_bayar += harga * int(qty.get())
        self.data["total_bayar"].set(f"Rp{total_bayar}")
        self.update_kembalian()

    def update_kembalian(self):
        try:
            nominal_bayar = int(self.data["nominal_bayar"].get())
        except ValueError:
            nominal_bayar = 0
        total_bayar = int(self.data["total_bayar"].get()[2:])
        kembalian = nominal_bayar - total_bayar
        self.data["nominal_kembalian"].set(f"Rp{kembalian}")

    def btn_pay(self):
        if self.data["total_bayar"].get()[2:] == "0":
            messagebox.showerror("Error", "Belum ada pesanan")
        elif self.data["nominal_bayar"].get()[2:] == "":
            messagebox.showerror("Error", "Masukkan nominal bayar")
        elif int(self.data["nominal_kembalian"].get()[2:]) < 0:
            messagebox.showwarning("Error", "Nominal bayar kurang")
        else:
            messagebox.showinfo("Success", "Terima kasih sudah berbelanja")
            self.write_data()
            self.reset()

    def reset(self):
        for _, _, qty, total in self.data["menu"]:
            qty.set("0")
            total.set("Rp0")
        self.data["total_bayar"].set("Rp0")
        self.data["nominal_bayar"].set("0")
        self.data["nominal_kembalian"].set("Rp0")

    def write_data(self):
        data = self.data
        total_bayar = int(data["total_bayar"].get()[2:])
        nominal_bayar = int(data["nominal_bayar"].get())
        nominal_kembalian = int(data["nominal_kembalian"].get()[2:])
        rincian = ""
        for menu, _, qty, total in data["menu"]:
            rincian += f"{menu} x {qty.get()} = {total.get()}, "
        rincian = rincian[:-2]

        with open(self.file, "a") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow([rincian, total_bayar, nominal_bayar,
                             nominal_kembalian, datetime.datetime.now()])


window = Tk()
app = App(window)
window.mainloop()
