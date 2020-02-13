#GUI Testing

import Tkinter as tk 

################################################################################
## GUI
################################################################################
class GearGUI():
    def __init__(self, master):
        # Initial Frames
        self.master = master
        self.initial_framing()
        self.gear_buttons()
        self.gear_labels()
        self.bottom_frame_buttons()


    def initial_framing(self):
        self.frameTitles = tk.Frame(self.master, bg='white', width=650, height=100)
        self.frameTitles.pack()
        self.frameUpper = tk.Frame(self.master, bg='cyan', width=650, height=50)
        self.frameUpper.pack()
        self.frameLower = tk.Frame(self.master, bg='white', width=650, height=100)
        self.frameLower.pack()

    def gear_buttons(self):
        self.hbuttonim = tk.PhotoImage(file='helmim.gif')
        self.hbutton = tk.Button(self.frameUpper, image=self.hbuttonim, width=50, height=50, pady=25, command=self.addgearh)
        self.bbutton = tk.Button(self.frameUpper, image=self.hbuttonim, width=50, height=50, pady=25, command=self.addgearb)
        self.abutton = tk.Button(self.frameUpper, image=self.hbuttonim, width=50, height=50, pady=25, command=self.close_windows)
        self.lbutton = tk.Button(self.frameUpper, image=self.hbuttonim, width=50, height=50, pady=25, command=self.close_windows)
        self.fbutton = tk.Button(self.frameUpper, image=self.hbuttonim, width=50, height=50, pady=25, command=self.close_windows)
        self.hbutton.grid(row=0, column=0)
        self.bbutton.grid(row=1, column=0)
        self.abutton.grid(row=2, column=0)
        self.lbutton.grid(row=3, column=0)
        self.fbutton.grid(row=4, column=0)

    def gear_labels(self):
        self.hlabelstr = tk.StringVar()
        self.hlabelstr.set('None')
        self.blabelstr = tk.StringVar()
        self.blabelstr.set('None')
        self.alabelstr = tk.StringVar()
        self.alabelstr.set('None')
        self.llabelstr = tk.StringVar()
        self.llabelstr.set('None')
        self.flabelstr = tk.StringVar()
        self.flabelstr.set('None')
        self.hlabel = tk.Label(self.frameUpper, textvariable=self.hlabelstr, width=25)
        self.blabel = tk.Label(self.frameUpper, textvariable=self.blabelstr, width=25)
        self.alabel = tk.Label(self.frameUpper, textvariable=self.alabelstr, width=25)
        self.llabel = tk.Label(self.frameUpper, textvariable=self.llabelstr, width=25)
        self.flabel = tk.Label(self.frameUpper, textvariable=self.flabelstr, width=25)
        self.hlabel.grid(row=0, column=1)
        self.blabel.grid(row=1, column=1)
        self.alabel.grid(row=2, column=1)
        self.llabel.grid(row=3, column=1)
        self.flabel.grid(row=4, column=1)

    def addgearh(self):
        self.hstring = 'Head' + '\n' + 'Head2' + '\n' + 'Head3'
        self.hlabelstr.set(self.hstring)

    def addgearb(self):
        self.blabelstr.set('Body')

    def bottom_frame_buttons(self):
        self.quitButton = tk.Button(self.frameLower, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack()

    def close_windows(self):
        self.master.destroy()

class TestClass():
    def __init__(self):
        self.teststr = 'test'
# root=Tk()
# b=Button(root,justify = LEFT)
# photo=PhotoImage(file="mine32.gif")
# b.config(image=photo,width="10",height="10")
# b.pack(side=LEFT)
# root.mainloop()


# Running the GUI
def main():
    root = tk.Tk()
    app = GearGUI(root)
    root.mainloop()



if __name__ == '__main__':
    main()