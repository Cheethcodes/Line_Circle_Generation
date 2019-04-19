import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
from tkinter import ttk
from matplotlib import pyplot as plt

def getNumber(x):
    y = x.get()
    if (y == ""):
        return 0
    else:
        return int(y)

def showPlotBressenham(self, listX, listY):
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.scatter(listX, listY, s=7, c="g")
    plt.show()

def showPlotDDA(self, listX, listY):
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.scatter(listX, listY, s=7, c="g")
    plt.show()

class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1280x710")
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

                listbox.insert(END, '- | - | %s | %s' % (x, y))

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

                            listbox.insert(END, '%s | %s | %s | %s' % (p, Rp, x, y))

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

                                listbox.insert(END, '%s | %s | %s | %s' % (p, Rp, x, y))

                                listX.append(x)
                                listY.append(y)

                        else:

                            x += 1

                            if Rp >= 0:
                                y = y - 1
                            else:
                                y = y

                            listbox.insert(END, '%s | %s | %s | %s' % (p, Rp, x, y))

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

                                listbox.insert(END, '%s | %s | %s | %s' % (p, Rp, x, y))

                                listX.append(x)
                                listY.append(y)

                    else:

                        if a > c:

                            x -= 1

                            if Rp >= 0:
                                y = y + 1
                            else:
                                y = y

                            listbox.insert(END, '%s | %s | %s | %s' % (p, Rp, x, y))

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

                                listbox.insert(END, '%s | %s | %s | %s' % (p, Rp, x, y))

                                listX.append(x)
                                listY.append(y)

                        else:

                            x += 1

                            if Rp >= 0:
                                y = y + 1
                            else:
                                y = y

                            listbox.insert(END, '%s | %s | %s | %s' % (p, Rp, x, y))

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

                                listbox.insert(END, '%s | %s | %s | %s' % (p, Rp, x, y))

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

                            listbox.insert(END, '%s | %s | %s | %s' % (p, Rp, x, y))

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

                                listbox.insert(END, '%s | %s | %s | %s' % (p, Rp, x, y))

                                listX.append(x)
                                listY.append(y)

                        else:

                            y += 1

                            if Rp >= 0:
                                x = x - 1
                            else:
                                x = x

                            listbox.insert(END, '%s | %s | %s | %s' % (p, Rp, x, y))

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

                                listbox.insert(END, '%s | %s | %s | %s' % (p, Rp, x, y))

                                listX.append(x)
                                listY.append(y)

                    else:

                        if b > d:

                            y -= 1

                            if Rp >= 0:
                                x = x + 1
                            else:
                                x = x

                            listbox.insert(END, '%s | %s | %s | %s' % (p, Rp, x, y))

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

                                listbox.insert(END, '%s | %s | %s | %s' % (p, Rp, x, y))

                                listX.append(x)
                                listY.append(y)

                        else:

                            y += 1

                            if Rp >= 0:
                                x = x + 1
                            else:
                                x = x

                            listbox.insert(END, '%s | %s | %s | %s' % (p, Rp, x, y))

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

                                listbox.insert(END, '%s | %s | %s | %s' % (p, Rp, x, y))

                                listX.append(x)
                                listY.append(y)

                listbox.pack(side=LEFT, padx=5)
                scroll.pack(side=RIGHT, fill=Y)
                scroll.config(command=listbox.yview)
                frame.grid(row=8, column=2, columnspan=20, rowspan=100, sticky="nw")

        label_blankbtn = tk.Label(self, text=" ")
        btnCalc_bressenham = tk.Button(self, text="Calculate", width=15, font=("Helvetica", 20, "bold"), command=execBressenham)

        label_blankbtn.grid(row=3, column=7)
        btnCalc_bressenham.grid(row=3, column=8, rowspan=3)

        frame = Frame(self)
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
                frame.grid(row=8, column=2, columnspan=20, rowspan=100, sticky="nw")

        label_blankbtn = tk.Label(self, text=" ")
        btnCalc_DDA = tk.Button(self, text="Calculate", width=15, font=("Helvetica", 20, "bold"), command=execDDA)

        label_blankbtn.grid(row=3, column=7)
        btnCalc_DDA.grid(row=3, column=8, rowspan=3)

        frame = Frame(self)
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

        label_coordinates_Modular = tk.Label(self, text="Coord Center >")
        label_Pointa_Modular = tk.Label(self, text="X ")
        label_Pointb_Modular = tk.Label(self, text="Y ")
        label_Pointc_Modular = tk.Label(self, text="Radius ")
        txt_Pointsa_Modular = tk.Entry(self, width=30)
        txt_Pointsb_Modular = tk.Entry(self, width=30)
        txt_Pointsc_Modular = tk.Entry(self, width=30)
        buttonCalc_Modular = tk.Button(self, text="Calculate", width=25)

        label_coordinates_Modular.grid(row=3, column=2)
        label_Pointa_Modular.grid(row=3, column=3)
        txt_Pointsa_Modular.grid(row=3, column=4)
        label_Pointb_Modular.grid(row=3, column=5)
        txt_Pointsb_Modular.grid(row=3, column=6)
        label_Pointc_Modular.grid(row=5, column=3)
        txt_Pointsc_Modular.grid(row=5, column=4)
        buttonCalc_Modular.grid(row=5, column=5, columnspan=2)

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

##################################################################################################################

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()