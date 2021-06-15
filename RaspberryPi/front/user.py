import tkinter as tk
import time
from tkinter import ttk

columns = ('#1', '#2', '#3')

current_balance = 1000

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {'Balance': tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in ( MenuPage, AbsenPage, PeminjamanPage, PengembalianPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MenuPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='Sistem Peminjaman Buku',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        main_menu_label = tk.Label(self,
                                   text='Main Menu',
                                   font=('orbitron', 13),
                                   fg='white',
                                   bg='#3d3d5c')
        main_menu_label.pack()

        selection_label = tk.Label(self,
                                   text='Please make a selection',
                                   font=('orbitron', 13),
                                   fg='white',
                                   bg='#3d3d5c',
                                   anchor='w')
        selection_label.pack(fill='x')

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        def Absen():
            controller.show_frame('AbsenPage')

        absen_button = tk.Button(button_frame,
                                    text='Absen',
                                    command=Absen,
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        absen_button.grid(row=0, column=0, pady=5)

        def peminjaman():
            controller.show_frame('PeminjamanPage')

        deposit_button = tk.Button(button_frame,
                                   text='Peminjaman',
                                   command=peminjaman,
                                   relief='raised',
                                   borderwidth=3,
                                   width=50,
                                   height=5)
        deposit_button.grid(row=1, column=0, pady=5)

        def pengembalian():
            controller.show_frame('PengembalianPage')

        balance_button = tk.Button(button_frame,
                                   text='Pengembalian',
                                   command=pengembalian,
                                   relief='raised',
                                   borderwidth=3,
                                   width=50,
                                   height=5)
        balance_button.grid(row=2, column=0, pady=5)


        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()


class AbsenPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='Absensi',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        scan_label = tk.Label(self,
                                       text='Scan Your KTM',
                                       font=('orbitron', 13),
                                       fg='white',
                                       bg='#3d3d5c')
        scan_label.pack()

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        def back():
            controller.show_frame('MenuPage')

        back_button = tk.Button(button_frame,
                                command=back,
                                text='Back',
                                relief='raised',
                                borderwidth=3,
                                width=10,
                                height=2)
        back_button.grid(row=0, column=0, pady=5)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()


class PeminjamanPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='Peminjaman Buku',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        # TABEL
        data = [["Tri", "Biologi"],
                ["Tri", "Fisika"]]

        frame = tk.Frame(self)
        frame.pack()
        tree = ttk.Treeview(frame, columns=(1, 2), height=15, show="headings")
        tree.pack(side='left')

        tree.heading(1, text="Penulis")
        tree.heading(2, text="Nama Buku")

        tree.column(1, width=300)
        tree.column(2, width=300)

        # scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        # scroll.pack(side='right', fill='y')
        #
        # tree.configure(yscrollcommand=scroll.set)

        for val in data:
            tree.insert('', 'end', values=(val[0], val[1]))
        # END TABEL

        # TOMBOL BUTTON
        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        def back():
            controller.show_frame('MenuPage')

        back_button = tk.Button(button_frame,
                                command=back,
                                text='Back',
                                relief='raised',
                                borderwidth=3,
                                width=10,
                                height=2)
        back_button.grid(row=0, column=0, pady=5)

        two_tone_label = tk.Label(self, bg='#33334d')
        two_tone_label.pack(fill='both', expand=True)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()

class PengembalianPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='Pengembalian Buku',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        # BUKU DIPINJAM
        buku = {
            'Harry' : 'poter',
            'weig' : 'tanduk'
        }

        heading_borrow = tk.Label(self, text='Buku yang dipinjam')
        heading_borrow.pack()
        lb = tk.Listbox(self)
        for x, y in enumerate(buku):
            lb.insert(x+1, y)
        lb.pack(padx=5, pady=10)

        # BUKU DISCAN
        book = {
            'Harry' : 'poter',
            'weig' : 'tanduk'
        }

        book_scan = tk.Label(self, text='Buku yang discan')
        book_scan.pack()
        lb = tk.Listbox(self)
        for x, y in enumerate(book):
            lb.insert(x+1, y)
        lb.pack(padx=5, pady=10)

        # TOMBOL BUTTON
        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        def back():
            controller.show_frame('MenuPage')

        back_button = tk.Button(button_frame,
                                command=back,
                                text='Back',
                                relief='raised',
                                borderwidth=3,
                                width=10,
                                height=2)
        back_button.grid(row=0, column=0)

        send_frame = tk.Frame(self, bg='#33334d')
        send_frame.pack(fill='both', expand=True)
        def send():
            controller.show_frame('MenuPage')

        send_button = tk.Button(send_frame,
                                command=send,
                                text='Confirm',
                                relief='raised',
                                borderwidth=3,
                                width=10,
                                height=2)
        send_button.grid(row=0, column=1)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        visa_photo = tk.PhotoImage(file='visa.png')
        visa_label = tk.Label(bottom_frame, image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='mastercard.png')
        mastercard_label = tk.Label(bottom_frame, image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        american_express_photo = tk.PhotoImage(file='american-express.png')
        american_express_label = tk.Label(bottom_frame, image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image = american_express_photo

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
