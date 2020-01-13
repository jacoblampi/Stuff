# from Tkinter import *
# import Tkinter as ttk

# def calculate(*args):
#     try:
#         value = float(feet.get())
#         meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
#     except ValueError:
#         pass

# root = Tk()
# root.title("Feet to Meters")

# mainframe = ttk.Frame(root)
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# feet = StringVar()
# meters = StringVar()

# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))

# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind('<Return>', calculate)

# root.mainloop()


#####################
#####################


import Tkinter as tk

class Demo1:
    def __init__(self, master):
        self.master = master
        #self.frame = tk.Frame(self.master, bg='cyan', width=900, height=400)
        #self.frame2 = tk.Frame(self.master, bg='white', width=900, height=100, padx=3, pady=3)
        self.initialFraming()
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack(side=tk.LEFT)
        self.button2 = tk.Button(self.frame, text = 'New Window2', width = 25, command = self.new_window)
        self.button2.pack(side=tk.LEFT)
        self.quitButton = tk.Button(self.frame2, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        #self.frame.pack()
        #self.frame2.pack()
        self.label1 = tk.StringVar()
        self.label1.set("test")
        self.sectionLabel1 = tk.Label(self.frame, textvariable=self.label1)
        self.sectionLabel1.pack(side=tk.LEFT)
    def initialFraming(self):
        self.frame = tk.Frame(self.master, bg='cyan', width=900, height=400)
        self.frame2 = tk.Frame(self.master, bg='white', width=900, height=100, padx=3, pady=3)
        self.frame.pack()
        self.frame2.pack()
    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.frame_new_window = tk.Frame(self.newWindow)
        self.button1_2 = tk.Button(self.frame_new_window, text = 'Update Text', width = 25, command = self.update_text)
        self.button1_2.pack(side=tk.LEFT)
        self.quitButton_2 = tk.Button(self.frame_new_window, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton_2.pack()
        self.frame_new_window.pack()
    def update_text(self):
        self.label1.set("updated remotely")
    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
