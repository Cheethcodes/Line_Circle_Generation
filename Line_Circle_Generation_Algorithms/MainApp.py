import matplotlib
matplotlib.use("TkAgg")

from tkinter import *
from decimal import Decimal, ROUND_HALF_UP
from math import cos, sin, radians
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk

def getNumber(x):
    y = x.get()
    if (y == ""):
        return 0
    else:
        return int(y)

class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1090x710")
        self.title("CS 208 Project")
        self.resizable(False, False)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartUp, Bressenham, DDA, Modular, Midpoint):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartUp")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

###############################################################################################################

class StartUp(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.ttk.Separator(self, orient="vertical").grid(column=1, row=0, rowspan=900, sticky='ns')

        label = tk.Label(self, text="CS 208 PROJECT - Home", font=controller.title_font)
        label.grid(row=0, column=2, pady=10, padx=10, columnspan=20, sticky="w")

        label_subtitle_1 = tk.Label(self, text="--------Main Page--------", font=("Times New Roman", 18))
        label_subtitle_1.grid(row=3, column=0, pady=5, rowspan=2)

        button1 = tk.Button(self, text="Main Page", command=lambda: controller.show_frame("StartUp"), width=19,
                            height=2)
        button1.grid(row=5, column=0, padx=5, pady=5, rowspan=2)

        label_subtitle_2 = tk.Label(self, text="-----Line Generation-----", font=("Times New Roman", 18))
        label_subtitle_2.grid(row=7, column=0, pady=20, rowspan=2)

        button2 = tk.Button(self, text="Bressenham Algorithm", command=lambda: controller.show_frame("Bressenham"), width=19, height=2)
        button2.grid(row=9, column=0, pady=5, rowspan=2)

        button3 = tk.Button(self, text="DDA Algorithm", command=lambda: controller.show_frame("DDA"), width=19,
                            height=2)
        button3.grid(row=11, column=0, pady=5, rowspan=2)

        label_subtitle_3 = tk.Label(self, text="----Circle Generation----", font=("Times New Roman", 18))
        label_subtitle_3.grid(row=13, column=0, pady=20, rowspan=2)

        button4 = tk.Button(self, text="Midpoint Algorithm", command=lambda: controller.show_frame("Midpoint"),
                            width=19, height=2)
        button4.grid(row=15, column=0, pady=5, rowspan=2)

        button5 = tk.Button(self, text="Modular Algorithm", command=lambda: controller.show_frame("Modular"), width=19,
                            height=2)
        button5.grid(row=17, column=0, pady=5, rowspan=2)

        label_subtitle_4 = tk.Label(self, text="-----------About-----------", font=("Times New Roman", 18))
        label_subtitle_4.grid(row=19, column=0, pady=20, rowspan=2)

        label_subtitle_4_body = tk.Label(self,
                                         text="Project created by Lyle Steven R. Biscocho and Gabriel Hansley C. Suarez in partial fulfillment of CS 208",
                                         wraplength=220)
        label_subtitle_4_body.grid(row=21, column=0, pady=5)

        label_footer = tk.Label(self, text="              ", font=("Helvetica", 18))
        label_footer.grid(row=22, column=2, pady=5)

        label_footer2 = tk.Label(self, text="              ", font=("Helvetica", 18))
        label_footer2.grid(row=23, column=2, pady=5)

###############################################################################################################

class Bressenham(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.ttk.Separator(self, orient="vertical").grid(column=1, row=0, rowspan=900, sticky='ns')

        label = tk.Label(self, text="CS 208 PROJECT - Bressenham Line Generation", font=controller.title_font)
        label.grid(row=0, column=2, pady=10, ipadx=10, columnspan=20, sticky="w")

        label_subtitle_1 = tk.Label(self, text="--------Main Page--------", font=("Times New Roman", 18))
        label_subtitle_1.grid(row=3, column=0, pady=5, rowspan=2)

        button1 = tk.Button(self, text="Main Page", command=lambda: controller.show_frame("StartUp"), width=19,
                            height=2)
        button1.grid(row=5, column=0, padx=5, pady=5, rowspan=2)

        label_subtitle_2 = tk.Label(self, text="-----Line Generation-----", font=("Times New Roman", 18))
        label_subtitle_2.grid(row=7, column=0, pady=20, rowspan=2)

        button2 = tk.Button(self, text="Bressenham Algorithm", width=19, height=2)
        button2.grid(row=9, column=0, pady=5, rowspan=2)

        button3 = tk.Button(self, text="DDA Algorithm", command=lambda: controller.show_frame("DDA"), width=19,
                            height=2)
        button3.grid(row=11, column=0, pady=5, rowspan=2)

        label_subtitle_3 = tk.Label(self, text="----Circle Generation----", font=("Times New Roman", 18))
        label_subtitle_3.grid(row=13, column=0, pady=20, rowspan=2)

        button4 = tk.Button(self, text="Midpoint Algorithm", command=lambda: controller.show_frame("Midpoint"),
                            width=19, height=2)
        button4.grid(row=15, column=0, pady=5, rowspan=2)

        button5 = tk.Button(self, text="Modular Algorithm", command=lambda: controller.show_frame("Modular"), width=19,
                            height=2)
        button5.grid(row=17, column=0, pady=5, rowspan=2)

        label_subtitle_4 = tk.Label(self, text="-----------About-----------", font=("Times New Roman", 18))
        label_subtitle_4.grid(row=19, column=0, pady=20, rowspan=2)

        label_subtitle_4_body = tk.Label(self,
                                         text="Project created by Lyle Steven R. Biscocho and Gabriel Hansley C. Suarez in partial fulfillment of CS 208",
                                         wraplength=220)
        label_subtitle_4_body.grid(row=21, column=0, pady=5)

        label_footer = tk.Label(self, text="              ", font=("Helvetica", 18))
        label_footer.grid(row=22, column=2, pady=5)

        label_footer2 = tk.Label(self, text="              ", font=("Helvetica", 18))
        label_footer2.grid(row=23, column=2, pady=5)

        label_coordinate1_bressenham = tk.Label(self, text="Coord 1 >")
        label_coordinate2_bressenham = tk.Label(self, text="Coord 2 >")

        label_Pointa_bressenham = tk.Label(self, text="X1 ")
        label_Pointb_bressenham = tk.Label(self, text="Y1 ")
        label_Pointc_bressenham = tk.Label(self, text="X2 ")
        label_Pointd_bressenham = tk.Label(self, text="Y2 ")
        txt_Pointa_bressenham = tk.Entry(self, width=30)
        txt_Pointb_bressenham = tk.Entry(self, width=30)
        txt_Pointc_bressenham = tk.Entry(self, width=30)
        txt_Pointd_bressenham = tk.Entry(self, width=30)

        label_coordinate1_bressenham.grid(row=3, column=2)

        label_Pointa_bressenham.grid(row=3, column=3)
        txt_Pointa_bressenham.grid(row=3, column=4, pady=5, padx=5)

        label_Pointb_bressenham.grid(row=3, column=5)
        txt_Pointb_bressenham.grid(row=3, column=6, pady=5, padx=5)

        label_coordinate2_bressenham.grid(row=5, column=2)

        label_Pointc_bressenham.grid(row=5, column=3)
        txt_Pointc_bressenham.grid(row=5, column=4, pady=5, padx=5)

        label_Pointd_bressenham.grid(row=5, column=5)
        txt_Pointd_bressenham.grid(row=5, column=6, pady=5, padx=5)

        def execBressenham():
            listbox.delete(2, END)
            errMsg = StringVar()
            errMsgColor = "red"

            label_errMsg = tk.Label(self, textvariable=errMsg, fg=errMsgColor, font=("Times New Roman", 12))
            label_errMsg.grid(row=7, column=3, columnspan=20, sticky="nesw")

            a = getNumber(txt_Pointa_bressenham)
            b = getNumber(txt_Pointb_bressenham)
            c = getNumber(txt_Pointc_bressenham)
            d = getNumber(txt_Pointd_bressenham)

            dx = abs(c - a)
            dy = abs(d - b)

            if (a==0 and b==0 and c==0 and d==0 or dx == 0):
                errMsg.set("No line to draw!")
                label_errMsg.update()
                errMsgColor = "red"
                label_errMsg['fg'] = errMsgColor

            else:
                errMsg.set(" Line is drawn ! ")
                label_errMsg.update()
                errMsgColor = "green"
                label_errMsg['fg'] = errMsgColor

                m = dy / dx
                x, y = a, b

                listX = []
                listY = []

                listbox.insert(END, '-, -, %s, %s' % (x, y))

                listX.append(x)
                listY.append(y)

                ddx = 2 * dx
                ddy = 2 * dy
                p = 0

                if m < 1:

                    Rp = ddy - dx

                    if b > d:

                        if a > c:

                            x -= 1

                            if Rp >= 0:
                                y = y - 1
                            else:
                                y = y

                            listbox.insert(END, '%s, %s, %s, %s' % (p, Rp, x, y))

                            listX.append(x)
                            listY.append(y)

                            for i in range(c + 2, a + 1):
                                p += 1
                                x -= 1

                                if Rp >= 0:
                                    Rp = Rp + ddy - ddx
                                else:
                                    Rp = Rp + ddy

                                if Rp >= 0:
                                    y = y - 1
                                else:
                                    y = y

                                listbox.insert(END, '%s, %s, %s, %s' % (p, Rp, x, y))

                                listX.append(x)
                                listY.append(y)

                        else:

                            x += 1

                            if Rp >= 0:
                                y = y - 1
                            else:
                                y = y

                            listbox.insert(END, '%s, %s, %s, %s' % (p, Rp, x, y))

                            listX.append(x)
                            listY.append(y)

                            for i in range(a + 2, c + 1):
                                p += 1
                                x += 1

                                if Rp >= 0:
                                    Rp = Rp + ddy - ddx
                                else:
                                    Rp = Rp + ddy

                                if Rp >= 0:
                                    y = y - 1
                                else:
                                    y = y

                                listbox.insert(END, '%s, %s, %s, %s' % (p, Rp, x, y))

                                listX.append(x)
                                listY.append(y)

                    else:

                        if a > c:

                            x -= 1

                            if Rp >= 0:
                                y = y + 1
                            else:
                                y = y

                            listbox.insert(END, '%s, %s, %s, %s' % (p, Rp, x, y))

                            listX.append(x)
                            listY.append(y)

                            for i in range(c + 2, a + 1):
                                p += 1
                                x -= 1

                                if Rp >= 0:
                                    Rp = Rp + ddy - ddx
                                else:
                                    Rp = Rp + ddy

                                if Rp >= 0:
                                    y = y + 1
                                else:
                                    y = y

                                listbox.insert(END, '%s, %s, %s, %s' % (p, Rp, x, y))

                                listX.append(x)
                                listY.append(y)

                        else:

                            x += 1

                            if Rp >= 0:
                                y = y + 1
                            else:
                                y = y

                            listbox.insert(END, '%s, %s, %s, %s' % (p, Rp, x, y))

                            listX.append(x)
                            listY.append(y)

                            for i in range(a + 2, c + 1):
                                p += 1
                                x += 1

                                if Rp >= 0:
                                    Rp = Rp + ddy - ddx
                                else:
                                    Rp = Rp + ddy

                                if Rp >= 0:
                                    y = y + 1
                                else:
                                    y = y

                                listbox.insert(END, '%s, %s, %s, %s' % (p, Rp, x, y))

                                listX.append(x)
                                listY.append(y)

                else:
                    Rp = ddx - dy

                    if a > c:

                        if b > d:

                            y -= 1

                            if Rp >= 0:
                                x = x - 1
                            else:
                                x = x

                            listbox.insert(END, '%s, %s, %s, %s' % (p, Rp, x, y))

                            listX.append(x)
                            listY.append(y)

                            for i in range(d + 2, b + 1):
                                p += 1
                                y -= 1

                                if Rp >= 0:
                                    Rp = Rp + ddx - ddy
                                else:
                                    Rp = Rp + ddx

                                if Rp >= 0:
                                    x = x - 1
                                else:
                                    x = x

                                listbox.insert(END, '%s, %s, %s, %s' % (p, Rp, x, y))

                                listX.append(x)
                                listY.append(y)

                        else:

                            y += 1

                            if Rp >= 0:
                                x = x - 1
                            else:
                                x = x

                            listbox.insert(END, '%s, %s, %s, %s' % (p, Rp, x, y))

                            listX.append(x)
                            listY.append(y)

                            for i in range(b + 2, d + 1):
                                p += 1
                                y += 1

                                if Rp >= 0:
                                    Rp = Rp + ddx - ddy
                                else:
                                    Rp = Rp + ddx

                                if Rp >= 0:
                                    x = x - 1
                                else:
                                    x = x

                                listbox.insert(END, '%s, %s, %s, %s' % (p, Rp, x, y))

                                listX.append(x)
                                listY.append(y)

                    else:

                        if b > d:

                            y -= 1

                            if Rp >= 0:
                                x = x + 1
                            else:
                                x = x

                            listbox.insert(END, '%s, %s, %s, %s' % (p, Rp, x, y))

                            listX.append(x)
                            listY.append(y)

                            for i in range(d + 2, b + 1):
                                p += 1
                                y -= 1

                                if Rp >= 0:
                                    Rp = Rp + ddx - ddy
                                else:
                                    Rp = Rp + ddx

                                if Rp >= 0:
                                    x = x + 1
                                else:
                                    x = x

                                listbox.insert(END, '%s, %s, %s, %s' % (p, Rp, x, y))

                                listX.append(x)
                                listY.append(y)

                        else:

                            y += 1

                            if Rp >= 0:
                                x = x + 1
                            else:
                                x = x

                            listbox.insert(END, '%s, %s, %s, %s' % (p, Rp, x, y))

                            listX.append(x)
                            listY.append(y)

                            for i in range(b + 2, d + 1):
                                p += 1
                                y += 1

                                if Rp >= 0:
                                    Rp = Rp + ddx - ddy
                                else:
                                    Rp = Rp + ddx

                                if Rp >= 0:
                                    x = x + 1
                                else:
                                    x = x

                                listbox.insert(END, '%s, %s, %s, %s' % (p, Rp, x, y))

                                listX.append(x)
                                listY.append(y)

                listbox.pack(side=LEFT, padx=5)
                scroll.pack(side=RIGHT, fill=Y)
                scroll.config(command=listbox.yview)

                f = Figure(figsize=(5, 5), dpi=100)
                a = f.add_subplot(111)
                a.scatter(listX, listY)

                canvas = FigureCanvasTkAgg(f, self)
                canvas.draw()
                canvas.get_tk_widget().grid(row=8, column=5, rowspan=100, columnspan=100, sticky="nw")

        label_blankbtn = tk.Label(self, text=" ")
        btnCalc_bressenham = tk.Button(self, text="Calculate", width=15, font=("Helvetica", 20, "bold"), command=execBressenham)

        label_blankbtn.grid(row=3, column=7)
        btnCalc_bressenham.grid(row=3, column=8, rowspan=3)

        frame = Frame(self)
        frame.grid(row=8, column=2, columnspan=20, rowspan=100, sticky="nw")
        scroll = Scrollbar(frame)
        listbox = Listbox(frame, yscrollcommand=scroll.set, width=40, height=31)
        listbox.insert(END, "p | Rp | x | y")
        listbox.insert(END, "----------------------------------------------------------------------------------------------------------------")

##################################################################################################################

class DDA(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.ttk.Separator(self, orient="vertical").grid(column=1, row=0, rowspan=900, sticky='ns')

        label = tk.Label(self, text="CS 208 PROJECT - DDA Line Generation", font=controller.title_font)
        label.grid(row=0, column=2, pady=10, ipadx=10, columnspan=20, sticky="w")

        label_subtitle_1 = tk.Label(self, text="--------Main Page--------", font=("Times New Roman", 18))
        label_subtitle_1.grid(row=3, column=0, pady=5, rowspan=2)

        button1 = tk.Button(self, text="Main Page", command=lambda: controller.show_frame("StartUp"), width=19,
                            height=2)
        button1.grid(row=5, column=0, padx=5, pady=5, rowspan=2)

        label_subtitle_2 = tk.Label(self, text="-----Line Generation-----", font=("Times New Roman", 18))
        label_subtitle_2.grid(row=7, column=0, pady=20, rowspan=2)

        button2 = tk.Button(self, text="Bressenham Algorithm", command=lambda: controller.show_frame("Bressenham"), width=19, height=2)
        button2.grid(row=9, column=0, pady=5, rowspan=2)

        button3 = tk.Button(self, text="DDA Algorithm", width=19, height=2)
        button3.grid(row=11, column=0, pady=5, rowspan=2)

        label_subtitle_3 = tk.Label(self, text="----Circle Generation----", font=("Times New Roman", 18))
        label_subtitle_3.grid(row=13, column=0, pady=20, rowspan=2)

        button4 = tk.Button(self, text="Midpoint Algorithm", command=lambda: controller.show_frame("Midpoint"),
                            width=19, height=2)
        button4.grid(row=15, column=0, pady=5, rowspan=2)

        button5 = tk.Button(self, text="Modular Algorithm", command=lambda: controller.show_frame("Modular"), width=19,
                            height=2)
        button5.grid(row=17, column=0, pady=5, rowspan=2)

        label_subtitle_4 = tk.Label(self, text="-----------About-----------", font=("Times New Roman", 18))
        label_subtitle_4.grid(row=19, column=0, pady=20, rowspan=2)

        label_subtitle_4_body = tk.Label(self,
                                         text="Project created by Lyle Steven R. Biscocho and Gabriel Hansley C. Suarez in partial fulfillment of CS 208",
                                         wraplength=220)
        label_subtitle_4_body.grid(row=21, column=0, pady=5)

        label_footer = tk.Label(self, text="              ", font=("Helvetica", 18))
        label_footer.grid(row=22, column=2, pady=5)

        label_footer2 = tk.Label(self, text="              ", font=("Helvetica", 18))
        label_footer2.grid(row=23, column=2, pady=5)

        label_coordinate1_DDA = tk.Label(self, text="Coord 1 >")
        label_coordinate2_DDA = tk.Label(self, text="Coord 2 >")

        label_Pointa_DDA = tk.Label(self, text="X1 ")
        label_Pointb_DDA = tk.Label(self, text="Y1 ")
        label_Pointc_DDA = tk.Label(self, text="X2 ")
        label_Pointd_DDA = tk.Label(self, text="Y2 ")
        txt_Pointa_DDA = tk.Entry(self, width=30)
        txt_Pointb_DDA = tk.Entry(self, width=30)
        txt_Pointc_DDA = tk.Entry(self, width=30)
        txt_Pointd_DDA = tk.Entry(self, width=30)

        label_coordinate1_DDA.grid(row=3, column=2)

        label_Pointa_DDA.grid(row=3, column=3)
        txt_Pointa_DDA.grid(row=3, column=4, pady=5, padx=5)

        label_Pointb_DDA.grid(row=3, column=5)
        txt_Pointb_DDA.grid(row=3, column=6, pady=5, padx=5)

        label_coordinate2_DDA.grid(row=5, column=2)

        label_Pointc_DDA.grid(row=5, column=3)
        txt_Pointc_DDA.grid(row=5, column=4, pady=5, padx=5)

        label_Pointd_DDA.grid(row=5, column=5)
        txt_Pointd_DDA.grid(row=5, column=6, pady=5, padx=5)

        def execDDA():
            listbox.delete(2, END)
            errMsg = StringVar()
            errMsgColor = "red"

            label_errMsg = tk.Label(self, textvariable=errMsg, fg=errMsgColor, font=("Times New Roman", 12))
            label_errMsg.grid(row=7, column=3, columnspan=20, sticky="nesw")

            x1 = getNumber(txt_Pointa_DDA)
            y1 = getNumber(txt_Pointb_DDA)
            x2 = getNumber(txt_Pointc_DDA)
            y2 = getNumber(txt_Pointd_DDA)

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)

            if (x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0 or dx == 0):
                errMsg.set("No line to draw!")
                label_errMsg.update()
                errMsgColor = "red"
                label_errMsg['fg'] = errMsgColor

            else:
                errMsg.set(" Line is drawn ! ")
                label_errMsg.update()
                errMsgColor = "green"
                label_errMsg['fg'] = errMsgColor

                m = dy / dx
                x, y = x1, y1

                listX = []
                listY = []

                if m < 1:

                    if y1 > y2:

                        if x1 > x2:

                            for i in range(x2, x1 + 1):
                                listbox.insert(END, '%s, %s' % (x, round(y)))

                                listX.append(x)
                                listY.append(round(y))

                                x -= 1
                                y = y - m

                        else:

                            for i in range(x1, x2 + 1):
                                listbox.insert(END, '%s, %s' % (x, round(y)))

                                listX.append(x)
                                listY.append(round(y))

                                x += 1
                                y = y - m

                    else:

                        if x1 > x2:

                            for i in range(x2, x1 + 1):
                                listbox.insert(END, '%s, %s' % (x, round(y)))

                                listX.append(x)
                                listY.append(round(y))

                                x -= 1
                                y = y + m

                        else:

                            for i in range(x1, x2 + 1):
                                listbox.insert(END, '%s, %s' % (x, round(y)))

                                listX.append(x)
                                listY.append(round(y))

                                x += 1
                                y = y + m

                else:

                    if x1 > x2:

                        if y1 > y2:

                            for i in range(y2, y1 + 1):
                                listbox.insert(END, '%s, %s' % (round(x), y))

                                listX.append(round(x))
                                listY.append(y)

                                y -= 1
                                x = x - (1 / m)

                        else:

                            for i in range(y1, y2 + 1):
                                listbox.insert(END, '%s, %s' % (round(x), y))

                                listX.append(round(x))
                                listY.append(y)

                                y += 1
                                x = x - (1 / m)

                    else:

                        if y1 > y2:

                            for i in range(y2, y1 + 1):
                                listbox.insert(END, '%s, %s' % (round(x), y))

                                listX.append(round(x))
                                listY.append(y)

                                y -= 1
                                x = x + (1 / m)

                        else:

                            for i in range(y1, y2 + 1):
                                listbox.insert(END, '%s, %s' % (round(x), y))

                                listX.append(round(x))
                                listY.append(y)

                                y += 1
                                x = x + (1 / m)

                listbox.pack(side=LEFT, padx=5)
                scroll.pack(side=RIGHT, fill=Y)
                scroll.config(command=listbox.yview)

                f = Figure(figsize=(5, 5), dpi=100)
                a = f.add_subplot(111)
                a.scatter(listX, listY)

                canvas = FigureCanvasTkAgg(f, self)
                canvas.draw()
                canvas.get_tk_widget().grid(row=8, column=5, rowspan=100, columnspan=100, sticky="nw")

        label_blankbtn = tk.Label(self, text=" ")
        btnCalc_DDA = tk.Button(self, text="Calculate", width=15, font=("Helvetica", 20, "bold"), command=execDDA)

        label_blankbtn.grid(row=3, column=7)
        btnCalc_DDA.grid(row=3, column=8, rowspan=3)

        frame = Frame(self)
        frame.grid(row=8, column=2, columnspan=20, rowspan=100, sticky="nw")

        scroll = Scrollbar(frame)
        listbox = Listbox(frame, yscrollcommand=scroll.set, width=40, height=31)
        listbox.insert(END, "x | y")
        listbox.insert(END, "----------------------------------------------------------------------------------------------------------------")

##################################################################################################################

class Modular(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller

        tk.ttk.Separator(self, orient="vertical").grid(column=1, row=0, rowspan=900, sticky='ns')

        label = tk.Label(self, text="CS 208 PROJECT - Modular Circle Generation", font=controller.title_font)
        label.grid(row=0, column=2, pady=10, padx=10, columnspan=20, sticky="w")

        label_subtitle_1 = tk.Label(self, text="--------Main Page--------", font=("Times New Roman", 18))
        label_subtitle_1.grid(row=3, column=0, pady=5, rowspan=2)

        button1 = tk.Button(self, text="Main Page", command=lambda: controller.show_frame("StartUp"), width=19,
                            height=2)
        button1.grid(row=5, column=0, padx=5, pady=5, rowspan=2)

        label_subtitle_2 = tk.Label(self, text="-----Line Generation-----", font=("Times New Roman", 18))
        label_subtitle_2.grid(row=7, column=0, pady=20, rowspan=2)

        button2 = tk.Button(self, text="Bressenham Algorithm", command=lambda: controller.show_frame("Bressenham"), width=19, height=2)
        button2.grid(row=9, column=0, pady=5, rowspan=2)

        button3 = tk.Button(self, text="DDA Algorithm", command=lambda: controller.show_frame("DDA"), width=19,
                            height=2)
        button3.grid(row=11, column=0, pady=5, rowspan=2)

        label_subtitle_3 = tk.Label(self, text="----Circle Generation----", font=("Times New Roman", 18))
        label_subtitle_3.grid(row=13, column=0, pady=20, rowspan=2)

        button4 = tk.Button(self, text="Midpoint Algorithm", command=lambda: controller.show_frame("Midpoint"),
                            width=19, height=2)
        button4.grid(row=15, column=0, pady=5, rowspan=2)

        button5 = tk.Button(self, text="Modular Algorithm", width=19, height=2)
        button5.grid(row=17, column=0, pady=5, rowspan=2)

        label_subtitle_4 = tk.Label(self, text="-----------About-----------", font=("Times New Roman", 18))
        label_subtitle_4.grid(row=19, column=0, pady=20, rowspan=2)

        label_subtitle_4_body = tk.Label(self,
                                         text="Project created by Lyle Steven R. Biscocho and Gabriel Hansley C. Suarez in partial fulfillment of CS 208",
                                         wraplength=220)
        label_subtitle_4_body.grid(row=21, column=0, pady=5)

        label_footer = tk.Label(self, text="              ", font=("Helvetica", 18))
        label_footer.grid(row=22, column=2, pady=5)

        label_footer2 = tk.Label(self, text="              ", font=("Helvetica", 18))
        label_footer2.grid(row=23, column=2, pady=5)

        label_coordinates_Modular = tk.Label(self, text="Center >")
        label_Pointa_Modular = tk.Label(self, text=" X ")
        label_Pointb_Modular = tk.Label(self, text=" Y ")
        label_Pointc_Modular = tk.Label(self, text=" R ")
        txt_Pointsa_Modular = tk.Entry(self, width=30)
        txt_Pointsb_Modular = tk.Entry(self, width=30)
        txt_Pointsc_Modular = tk.Entry(self, width=30)
        label_BtnBlank = tk.Label(self, text=" ")

        label_coordinates_Modular.grid(row=3, column=2)
        label_Pointa_Modular.grid(row=3, column=3)
        txt_Pointsa_Modular.grid(row=3, column=4, pady=5, padx=5)
        label_Pointb_Modular.grid(row=3, column=5)
        txt_Pointsb_Modular.grid(row=3, column=6, pady=5, padx=5)
        label_Pointc_Modular.grid(row=5, column=3)
        txt_Pointsc_Modular.grid(row=5, column=4, pady=5, padx=5)
        label_BtnBlank.grid(row=3, column=7)

        def execModular():

            xValues = []
            yValues = []
            roundedXValues = []
            roundedYValues = []
            shiftedXValues = []
            shiftedYValues = []
            finalXValues = []
            finalYValues = []

            def getXCoordinate():
                corX = getNumber(txt_Pointsa_Modular)
                return corX

            def getYCoordinate():
                corY = getNumber(txt_Pointsb_Modular)
                return corY

            def getCircleRadius():
                radius = getNumber(txt_Pointsc_Modular)
                return radius

            def firstPart(radius, angle):
                firstList = []
                radA = radius * Decimal((cos(radians(angle))))
                x1 = Decimal(radA.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
                firstList.append(float(x1))
                radB = radius * Decimal((sin(radians(angle))))
                y1 = Decimal(radB.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
                firstList.append(float(y1))
                convertX = Decimal(x1.quantize(Decimal('1'), rounding=ROUND_HALF_UP))
                convertY = Decimal(y1.quantize(Decimal('1'), rounding=ROUND_HALF_UP))
                firstList.append(float(convertX))
                firstList.append(float(convertY))

                return firstList

            def firstPart(radius, angle):
                firstList = []
                radA = radius * Decimal((cos(radians(angle))))
                x1 = Decimal(radA.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
                firstList.append(float(x1))
                radB = radius * Decimal((sin(radians(angle))))
                y1 = Decimal(radB.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
                firstList.append(float(y1))
                convertX = Decimal(x1.quantize(Decimal('1'), rounding=ROUND_HALF_UP))
                convertY = Decimal(y1.quantize(Decimal('1'), rounding=ROUND_HALF_UP))
                firstList.append(float(convertX))
                firstList.append(float(convertY))
                return firstList

            def secondPart(radius, angle):
                secondList = []
                radA = radius * Decimal((cos(radians(2 * angle))))
                x2 = Decimal(radA.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
                secondList.append(float(x2))
                radB = radius * Decimal((sin(radians(2 * angle))))
                y2 = Decimal(radB.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
                secondList.append(float(y2))
                convertX = Decimal(x2.quantize(Decimal('1'), rounding=ROUND_HALF_UP))
                convertY = Decimal(y2.quantize(Decimal('1'), rounding=ROUND_HALF_UP))
                secondList.append(float(convertX))
                secondList.append(float(convertY))
                return secondList

            def succeedingParts(dAngle, x, y):
                succeedingList = []
                radA = Decimal(x) * Decimal(cos(radians(dAngle))) - Decimal(y) * Decimal(sin(radians(dAngle)))
                xn = Decimal(radA.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
                succeedingList.append(float(xn))
                radB = Decimal(y) * Decimal(cos(radians(dAngle))) + Decimal(x) * Decimal(sin(radians(dAngle)))
                yn = Decimal(radB.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))
                succeedingList.append(float(yn))
                convertX = Decimal(xn.quantize(Decimal('1'), rounding=ROUND_HALF_UP))
                convertY = Decimal(yn.quantize(Decimal('1'), rounding=ROUND_HALF_UP))
                succeedingList.append(float(convertX))
                succeedingList.append(float(convertY))
                return succeedingList

            def checkerFunction(x, y):
                checker = True
                if x == y:
                    checker = False
                return checker

            def shiftValues():

                for x in roundedXValues:
                    new = x + corX
                    shiftedXValues.append(new)

                for y in roundedYValues:
                    new = y + corY
                    shiftedYValues.append(new)

            def getPoints():

                finalXValues.append(corX)
                finalYValues.append(corY)

                for x in roundedXValues:
                    new = x + corX
                    finalXValues.append(new)

                for y in roundedYValues:
                    new = y + corX
                    finalXValues.append(new)

                for y in roundedYValues:
                    temp = -y
                    new = temp + corX

                    finalXValues.append(new)

                for x in roundedXValues:
                    temp = -x
                    new = temp + corX
                    finalXValues.append(new)

                for x in roundedXValues:
                    temp = -x
                    new = temp + corX
                    finalXValues.append(new)

                for y in roundedYValues:
                    temp = -y
                    new = temp + corX
                    finalXValues.append(new)

                for y in roundedYValues:
                    new = y + corX
                    finalXValues.append(new)

                for x in roundedXValues:
                    new = x + corX
                    finalXValues.append(new)

                for y in roundedYValues:
                    new = y + corY
                    finalYValues.append(new)

                for x in roundedXValues:
                    new = x + corY
                    finalYValues.append(new)

                for x in roundedXValues:
                    new = x + corY
                    finalYValues.append(new)

                for y in roundedYValues:
                    new = y + corY
                    finalYValues.append(new)

                for y in roundedYValues:
                    temp = -y
                    new = temp + corY
                    finalYValues.append(new)

                for x in roundedXValues:
                    temp = -x
                    new = temp + corY
                    finalYValues.append(new)

                for x in roundedXValues:
                    temp = -x
                    new = temp + corY
                    finalYValues.append(new)

                for y in roundedYValues:
                    temp = -y
                    new = temp + corY
                    finalYValues.append(new)

                finalXValues.append(corX + radius)
                finalXValues.append(corX - radius)
                finalXValues.append(corX)
                finalXValues.append(corX)
                finalYValues.append(corY)
                finalYValues.append(corY)
                finalYValues.append(corY + radius)
                finalYValues.append(corY - radius)

            def displayResult():

                listbox_shifted.delete(3, END)
                listbox_unshifted.delete(3, END)

                # UNSHIFTED VALUES + NOT ESTIMATED
                rowCnt = 0
                for x in xValues:
                    listbox_unshifted.insert(END, '%s %s' % (int(x), int(roundedYValues[rowCnt])))
                    rowCnt += 1

                # UNSHIFTED VALUES + ESTIMATED
                rowCnt1 = 0
                for x in roundedXValues:
                    rowCnt1 += 1

                # SHIFTED VALUES
                rowCnt2 = 0
                for x in shiftedXValues:
                    listbox_shifted.insert(END, '%s %s' % (int(x), int(shiftedYValues[rowCnt2])))
                    rowCnt2 += 1

                listbox_shifted.pack(side=LEFT, padx=5)
                scroll2.pack(side=RIGHT, fill=Y)
                scroll2.config(command=listbox_shifted.yview)

                listbox_unshifted.pack(side=LEFT, padx=5)
                scroll3.pack(side=RIGHT, fill=Y)
                scroll3.config(command=listbox_unshifted.yview)

            def displayPoints():
                listbox_points.delete(3, END)
                rowCnt = 0

                for x in finalXValues:
                    listbox_points.insert(END, '%s, %s' % (int(x), int(finalYValues[rowCnt])))
                    rowCnt += 1

                listbox_points.pack(side=LEFT, padx=5)
                scroll1.pack(side=RIGHT, fill=Y)
                scroll1.config(command=listbox_points.yview)

            def scatterPlot():
                f = Figure(figsize=(5, 5), dpi=100)
                a = f.add_subplot(111)
                a.scatter(finalXValues, finalYValues)

                canvas = FigureCanvasTkAgg(f, self)
                canvas.draw()
                canvas.get_tk_widget().grid(row=8, column=5, rowspan=100, columnspan=100, sticky="nw")

            def main():
                cont = True
                iterCnt = 0

                while cont == True:

                    if iterCnt == 0:

                        firstList = firstPart(radius, angle)
                        xValues.append(firstList[0])
                        yValues.append(firstList[1])
                        roundedXValues.append(firstList[2])
                        roundedYValues.append(firstList[3])

                    elif iterCnt == 1:

                        secondList = secondPart(radius, angle)
                        xValues.append(secondList[0])
                        yValues.append(secondList[1])
                        roundedXValues.append(secondList[2])
                        roundedYValues.append(secondList[3])

                    elif iterCnt > 1:
                        listLength = len(xValues)
                        succeedingList = succeedingParts(dAngle, xValues[listLength - 1], yValues[listLength - 1])
                        xValues.append(succeedingList[0])
                        yValues.append(succeedingList[1])
                        roundedXValues.append(succeedingList[2])
                        roundedYValues.append(succeedingList[3])

                    iterCnt += 1

                    listLength = len(roundedXValues)
                    cont = checkerFunction(roundedXValues[listLength - 1], roundedYValues[listLength - 1])

                label_errMsg = tk.Label(self, text=" Circle drawn! ", fg="green", font=("Times New Roman", 12))
                label_errMsg.grid(row=7, column=2, columnspan=100, sticky="nesw")

            corX = getXCoordinate()
            corY = getYCoordinate()

            radius = getCircleRadius()

            angle = Decimal(45 / radius)
            dAngle = angle

            main()
            shiftValues()
            getPoints()

            displayPoints()
            displayResult()
            scatterPlot()

        buttonCalc_Modular = tk.Button(self, text="Calculate", width=15, font=("Helvetica", 20, "bold"), command=execModular)
        buttonCalc_Modular.grid(row=3, column=8, columnspan=2, rowspan=3)

        mainframedisplay = Frame(self)
        mainframedisplay.grid(row=8, column=2, rowspan=100, columnspan=100, sticky="nw")

        frame1 = Frame(mainframedisplay)
        frame1.grid(row=1, column=1, rowspan=100, sticky="nw")
        scroll1 = Scrollbar(frame1)

        listbox_points = Listbox(frame1, yscrollcommand=scroll1.set, width=20, height=31)
        listbox_points.insert(END, "---------POINTS---------")
        listbox_points.insert(END, "x | y")
        listbox_points.insert(END, "----------------------------------------------------------------------------------------------------------------")

        frame2 = Frame(mainframedisplay)
        frame2.grid(row=1, column=2, rowspan=10, sticky="nw")
        scroll2 = Scrollbar(frame2)

        listbox_shifted = Listbox(frame2, yscrollcommand=scroll2.set, width=20, height=15)
        listbox_shifted.insert(END, "-------SHIFTED-------")
        listbox_shifted.insert(END, "x | y")
        listbox_shifted.insert(END, "----------------------------------------------------------------------------------------------------------------")

        frame3 = Frame(mainframedisplay)
        frame3.grid(row=11, column=2, rowspan=100, sticky="nw")
        scroll3 = Scrollbar(frame3)

        listbox_unshifted = Listbox(frame3, yscrollcommand=scroll3.set, width=20, height=16)
        listbox_unshifted.insert(END, "------UNSHIFTED------")
        listbox_unshifted.insert(END, "x | y")
        listbox_unshifted.insert(END, "----------------------------------------------------------------------------------------------------------------")

##################################################################################################################

class Midpoint(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.ttk.Separator(self, orient="vertical").grid(column=1, row=0, rowspan=900, sticky='ns')

        label = tk.Label(self, text="CS 208 PROJECT - Midpoint Circle Generation", font=controller.title_font)
        label.grid(row=0, column=2, pady=10, padx=10, columnspan=20, sticky="w")

        label_subtitle_1 = tk.Label(self, text="--------Main Page--------", font=("Times New Roman", 18))
        label_subtitle_1.grid(row=3, column=0, pady=5, rowspan=2)

        button1 = tk.Button(self, text="Main Page", command=lambda: controller.show_frame("StartUp"), width=19,
                            height=2)
        button1.grid(row=5, column=0, padx=5, pady=5, rowspan=2)

        label_subtitle_2 = tk.Label(self, text="-----Line Generation-----", font=("Times New Roman", 18))
        label_subtitle_2.grid(row=7, column=0, pady=20, rowspan=2)

        button2 = tk.Button(self, text="Bressenham Algorithm", command=lambda: controller.show_frame("Bressenham"), width=19, height=2)
        button2.grid(row=9, column=0, pady=5, rowspan=2)

        button3 = tk.Button(self, text="DDA Algorithm", command=lambda: controller.show_frame("DDA"), width=19,
                            height=2)
        button3.grid(row=11, column=0, pady=5, rowspan=2)

        label_subtitle_3 = tk.Label(self, text="----Circle Generation----", font=("Times New Roman", 18))
        label_subtitle_3.grid(row=13, column=0, pady=20, rowspan=2)

        button4 = tk.Button(self, text="Midpoint Algorithm", width=19, height=2)
        button4.grid(row=15, column=0, pady=5, rowspan=2)

        button5 = tk.Button(self, text="Modular Algorithm", command=lambda: controller.show_frame("Modular"), width=19,
                            height=2)
        button5.grid(row=17, column=0, pady=5, rowspan=2)

        label_subtitle_4 = tk.Label(self, text="-----------About-----------", font=("Times New Roman", 18))
        label_subtitle_4.grid(row=19, column=0, pady=20, rowspan=2)

        label_subtitle_4_body = tk.Label(self,
                                         text="Project created by Lyle Steven R. Biscocho and Gabriel Hansley C. Suarez in partial fulfillment of CS 208",
                                         wraplength=220)
        label_subtitle_4_body.grid(row=21, column=0, pady=5)

        label_footer = tk.Label(self, text="              ", font=("Helvetica", 18))
        label_footer.grid(row=22, column=2, pady=5)

        label_footer2 = tk.Label(self, text="              ", font=("Helvetica", 18))
        label_footer2.grid(row=23, column=2, pady=5)

        label_coordinates_Mid = tk.Label(self, text="Center >")
        label_Pointa_Mid = tk.Label(self, text=" X ")
        label_Pointb_Mid = tk.Label(self, text=" Y ")
        label_Pointc_Mid = tk.Label(self, text=" R ")
        txt_Pointsa_Mid = tk.Entry(self, width=30)
        txt_Pointsb_Mid = tk.Entry(self, width=30)
        txt_Pointsc_Mid = tk.Entry(self, width=30)
        label_BtnBlank = tk.Label(self, text=" ")

        label_coordinates_Mid.grid(row=3, column=2)
        label_Pointa_Mid.grid(row=3, column=3)
        txt_Pointsa_Mid.grid(row=3, column=4, pady=5, padx=5)
        label_Pointb_Mid.grid(row=3, column=5)
        txt_Pointsb_Mid.grid(row=3, column=6, pady=5, padx=5)
        label_Pointc_Mid.grid(row=5, column=3)
        txt_Pointsc_Mid.grid(row=5, column=4, pady=5, padx=5)
        label_BtnBlank.grid(row=3, column=7)

        def execMid():
            listRp = []
            listX = []
            listY = []
            actX = []
            actY = []
            finalX = []
            finalY = []

            def getXCoordinate():
                corX = getNumber(txt_Pointsa_Mid)
                return corX

            def getYCoordinate():
                corY = getNumber(txt_Pointsb_Mid)
                return corY

            def decisionXY(r, x, y):
                decisionArray = []
                if r < 0:
                    x += 1
                elif x >= 0:
                    x += 1
                    y -= 1

                decisionArray.append(x)
                decisionArray.append(y)

                return decisionArray

            def computeRp(r, x, y):
                if r < 0:
                    Rp = r + (2 * x) + 1
                else:
                    Rp = r + (2 * x) - Decimal((2 * y)) + 1

                return Rp

            def actual():
                for x in listX:
                    x = x + corX
                    actX.append(x)
                for y in listY:
                    y = y + corY
                    actY.append(y)

            def getPoints():
                finalX.append(corX)
                finalY.append(corY)

                for x in listX:
                    new = x + corX
                    finalX.append(new)

                for y in listY:
                    new = y + corX
                    finalX.append(new)

                for y in listY:
                    temp = -y
                    new = temp + corX
                    finalX.append(new)

                for x in listX:
                    temp = -x
                    new = temp + corX
                    finalX.append(new)

                for x in listX:
                    temp = -x
                    new = temp + corX
                    finalX.append(new)

                for y in listY:
                    temp = -y
                    new = temp + corX
                    finalX.append(new)

                for y in listY:
                    new = y + corX
                    finalX.append(new)

                for x in listX:
                    new = x + corX
                    finalX.append(new)

                for y in listY:
                    new = y + corY
                    finalY.append(new)

                for x in listX:
                    new = x + corY
                    finalY.append(new)

                for x in listX:
                    new = x + corY
                    finalY.append(new)

                for y in listY:
                    new = y + corY
                    finalY.append(new)

                for y in listY:
                    temp = -y
                    new = temp + corY
                    finalY.append(new)

                for x in listX:
                    temp = -x
                    new = temp + corY
                    finalY.append(new)

                for x in listX:
                    temp = -x
                    new = temp + corY
                    finalY.append(new)

                for y in listY:
                    temp = -y
                    new = temp + corY
                    finalY.append(new)

                finalX.append(corX + radius)
                finalX.append(corX - radius)
                finalX.append(corX)
                finalX.append(corX)
                finalY.append(corY)
                finalY.append(corY)
                finalY.append(corY + radius)
                finalY.append(corY - radius)

            def displayValues():
                listbox_values.delete(3, END)
                rowCnt = 0
                for r in listRp:
                    listbox_values.insert(END, '%.2f, %s, %s, %s, %s' % (r, int(listX[rowCnt]), int(listY[rowCnt]), int(actX[rowCnt]), int(actY[rowCnt])))
                    rowCnt += 1

                listbox_values.pack(side=LEFT, padx=5)
                scroll2.pack(side=RIGHT, fill=Y)
                scroll2.config(command=listbox_values.yview)

            def displayPoints():
                listbox_points.delete(3, END)
                rowCnt = 0
                for x in finalX:
                    listbox_points.insert(END, '%s, %s' % (int(x), int(finalY[rowCnt])))
                    rowCnt += 1

                listbox_points.pack(side=LEFT, padx=5)
                scroll1.pack(side=RIGHT, fill=Y)
                scroll1.config(command=listbox_points.yview)

            def scatterPlot():
                f = Figure(figsize=(5, 5), dpi=100)
                a = f.add_subplot(111)
                a.scatter(finalX, finalY)

                canvas = FigureCanvasTkAgg(f, self)
                canvas.draw()
                canvas.get_tk_widget().grid(row=8, column=5, rowspan=100, columnspan=100, sticky="nw")

            def main():
                cont = True
                iterCnt = 0

                while cont == True:

                    if iterCnt == 0:
                        listRp.append(Ro)
                        decA = decisionXY(listRp[len(listRp) - 1], initX, initY)
                        listX.append(decA[0])
                        listY.append(decA[1])

                    elif iterCnt != 0:
                        decA = computeRp(listRp[len(listRp) - 1], listX[len(listX) - 1], listY[len(listY) - 1])
                        listRp.append(decA)
                        decB = decisionXY(listRp[len(listRp) - 1], listX[len(listX) - 1], listY[len(listY) - 1])
                        listX.append(decB[0])
                        listY.append(decB[1])

                    iterCnt += 1

                    if listX[len(listX) - 1] >= listY[len(listY) - 1]:
                        cont = False

                label_errMsg = tk.Label(self, text=" Circle drawn! ", fg="green", font=("Times New Roman", 12))
                label_errMsg.grid(row=7, column=2, columnspan=100, sticky="nesw")

            corX = getXCoordinate()
            corY = getYCoordinate()
            radius = getNumber(txt_Pointsc_Mid)
            Ro = Decimal((5 / 4) - radius).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
            initX = 0
            initY = radius
            main()
            actual()
            getPoints()
            displayPoints()
            displayValues()
            scatterPlot()

        buttonCalc_Mid = tk.Button(self, text="Calculate", width=15, font=("Helvetica", 20, "bold"), command=execMid)
        buttonCalc_Mid.grid(row=3, column=8, columnspan=2, rowspan=3)

        mainframedisplay = Frame(self)
        mainframedisplay.grid(row=8, column=2, rowspan=100, columnspan=100, sticky="nw")

        frame1 = Frame(mainframedisplay)
        frame1.grid(row=1, column=1, rowspan=100, sticky="nw")
        scroll1 = Scrollbar(frame1)

        listbox_points = Listbox(frame1, yscrollcommand=scroll1.set, width=20, height=31)
        listbox_points.insert(END, "---------POINTS---------")
        listbox_points.insert(END, "x | y")
        listbox_points.insert(END, "----------------------------------------------------------------------------------------------------------------")

        frame2 = Frame(mainframedisplay)
        frame2.grid(row=1, column=2, rowspan=100, sticky="nw")
        scroll2 = Scrollbar(frame2)

        listbox_values = Listbox(frame2, yscrollcommand=scroll2.set, width=20, height=31)
        listbox_values.insert(END, "---ACTUAL VALUES---")
        listbox_values.insert(END, "Rp | x | y | Ax | Ay")
        listbox_values.insert(END, "----------------------------------------------------------------------------------------------------------------")

##################################################################################################################

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()