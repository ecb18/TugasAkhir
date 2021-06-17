import tkinter as tk
import time
from tkinter import messagebox as mb

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


        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0', ' ')
            time_label.config(text=current_time)
            time_label.after(200, tick)

        time_label = tk.Label(bottom_frame, font=('orbitron', 12))
        time_label.pack(side='right')

        tick()