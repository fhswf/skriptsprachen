import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


class PlotApp(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True, fill=tk.BOTH)

        self.text = tk.StringVar()
        self.text.set('np.sin(x)')

        grid = tk.Frame(self)
        grid.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        label = tk.Label(grid, text="Function to plot")
        label.grid(column=0, row=0)
        entry = tk.Entry(grid, width=50, textvariable=self.text)
        entry.grid(column=1, row=0, sticky='W')
        entry.bind('<Key-Return>', self.update_plot)

        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.plot = self.fig.add_subplot()

        # A tk.DrawingArea.
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.update_plot(None)

        button = tk.Button(master=root, text="Quit", command=self.quit)
        button.pack(side=tk.BOTTOM)

    def quit(self):
        self.master.quit()     # stops mainloop
        self.master.destroy()  # this is necessary on Windows to prevent
        # Fatal Python Error: PyEval_RestoreThread: NULL tstate

    def update_plot(self, event):
        print(self.text.get())
        x = np.linspace(0, np.pi, 100)
        y = eval(self.text.get())
        #print(f"{x} {y}")
        self.plot.plot(x, y)
        self.canvas.draw()


root = tk.Tk()
root.wm_title("Embedding in Tk")
app = PlotApp(master=root)
app.mainloop()
