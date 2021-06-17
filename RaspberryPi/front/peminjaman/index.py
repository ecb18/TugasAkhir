import tkinter as tk
import time
from tkinter import ttk
from tkinter import messagebox as mb

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

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()