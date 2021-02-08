"""widget_aux.py: Clases de widget auxiliares para la interfaz gráfica"""
__author__ = "Ana María Manso Rodríguez"
__credits__ = ["Ana María Manso Rodríguez"]
__version__ = "1.0"
__status__ = "Development"

from tkinter import ttk
import tkinter as tk


class Desplegable(ttk.Frame):

    def __init__(self, valores, parent):
        super().__init__(parent)

        self.combo = ttk.Combobox(self, width=100)
        self.combo.grid(row=2, column=1)
        self.combo["values"] = valores
        self.combo.bind("<<ComboboxSelected>>")


class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.hourstr = tk.StringVar(self, '10')
        self.hour = tk.Spinbox(self, from_=0, to=23, wrap=True, textvariable=self.hourstr, width=2, state="readonly")
        self.minstr = tk.StringVar(self, '30')
        self.minstr.trace("w", self.trace_var)
        self.last_value = ""
        self.min = tk.Spinbox(self, from_=0, to=59, wrap=True, textvariable=self.minstr, width=2, state="readonly")
        self.hour.grid()
        self.min.grid(row=0, column=1)

    def trace_var(self, *args):
        if self.last_value == "59" and self.minstr.get() == "0":
            self.hourstr.set(int(self.hourstr.get()) + 1 if self.hourstr.get() != "23" else 0)
        self.last_value = self.minstr.get()
