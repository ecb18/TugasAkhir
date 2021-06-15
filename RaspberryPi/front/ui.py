import tkinter as tk
from tkinter import ttk
from tkinter import *
root = tk.Tk()


filemenu = Menu(root)
filemenu.add_command(label="Peminjaman")
filemenu.add_command(label="Pengembalian")
filemenu.add_command(label="Absen")
root.config(menu=filemenu)

toolbarFrame = Frame(root, bg="#ccc")
toolbarFrame.pack(side=TOP, fill=X)

judul_kolom = ("Nama Peminjam", "Nama Buku")
data_mhs = [
    ('Rijal',  'Fisika'),
    ('Tri',  'Biologi'),
    ('Evan', 'Bahasa Indonesia')
]


class DemoTabelMHS:
    def __init__(self, induk, judul):
        self.induk = induk

        self.induk.title(judul)
        self.induk.protocol("WM_DELETE_WINDOW", self.Tutup)
        self.induk.resizable(False, False)

        self.aturKomponen()
        self.isiTabel()

    def aturKomponen(self):
        # buat frame utama
        mainFrame = Frame(self.induk)
        mainFrame.pack(fill=BOTH, expand=YES)

        # buat frame untuk tabel beserta scrollbar-nya
        fr_data = Frame(mainFrame, bd=10)
        fr_data.pack(fill=BOTH, expand=YES)

        # buat tabel dengan Treeview
        self.trvTabel = ttk.Treeview(fr_data, columns=judul_kolom,
                                     show='headings')

        # buat scrollbar
        sbVer = Scrollbar(fr_data, orient='vertical',
                          command=self.trvTabel.yview)
        sbHor = Scrollbar(fr_data, orient='horizontal',
                          command=self.trvTabel.xview)
        # pasang dengan layout manager pack()
        sbVer.pack(side=RIGHT, fill=Y)
        sbHor.pack(side=BOTTOM, fill=X)
        self.trvTabel.pack(side=LEFT, fill=BOTH)

        # buat statusbar
        lblStatus = Label(mainFrame,
                          text='www.pnj.com', bd=1, relief=SUNKEN)
        lblStatus.pack(side=BOTTOM, fill=X)

    def isiTabel(self):
        # isi judul tabel
        for kolom in judul_kolom:
            self.trvTabel.heading(kolom, text=kolom)

        # isi data tabel
        for dat in data_mhs:
            self.trvTabel.insert('', 'end', values=dat)

    def Tutup(self, event=None):
        self.induk.destroy()


if __name__ == '__main__':
    app = DemoTabelMHS(root, "Sistem Peminjaman Buku")

    root.mainloop()
