## Project Goals:
# 3 sections for tasks
# tasks assigned to a larger project
# time estimates
# time completions
# add tasks
# remove tasks/generate weekly report

import Tkinter as tk 

# Task
class toDoTask():
    def __init__(self, zone, task, timeallotted, duedate, finishdate=""):
        self.zone = zone 
        self.task = task
        self.timeallotted = timeallotted 
        self.duedate = duedate 
        self.finishdate = ""
    def getInfo(self):
        return [self.zone, self.timeallotted, self.duedate, self.finishdate]
    def changeZone(self, newzone):
        self.zone = newzone
    def changeFinishDate(self, date):
        self.finishdate = date 

#GUI
class tkinterGUI():
    def __init__(self, master):
        #Initial Frames
        self.master = master
        self.initial_framing()
        self.initial_task_column_framing()
        self.bottom_frame_buttons()
        self.label1 = tk.StringVar()
        self.label1.set("test")
        self.sectionLabel1 = tk.Label(self.frameTitles, textvariable=self.label1)
        self.sectionLabel1.pack()
    def initial_framing(self):
        self.frameTitles = tk.Frame(self.master, bg='white', width=900, height=100, padx=3, pady=3)
        self.frameTitles.pack()
        self.frameUpper = tk.Frame(self.master, bg='cyan', width=900, height=400)
        self.frameUpper.pack()
        self.frameLower = tk.Frame(self.master, bg='white', width=900, height=100, padx=3, pady=3)
        self.frameLower.pack()
    def initial_task_column_framing(self):
        self.frameStartList = tk.Frame(self.frameUpper, bg='light blue', width=300, height=400, padx=3, pady=3)
        self.frameStartList.pack(side=tk.LEFT)
        self.frameInProgress = tk.Frame(self.frameUpper, bg='dark salmon', width=300, height=400, padx=3, pady=3)
        self.frameInProgress.pack(side=tk.LEFT)
        self.frameFinished = tk.Frame(self.frameUpper, bg='dark sea green', width=300, height=400, padx=3, pady=3)
        self.frameFinished.pack(side=tk.LEFT)
    def bottom_frame_buttons(self):
        self.updateButton = tk.Button(self.frameLower, text = 'Update', width = 25, command = self.add_label_window)
        self.quitButton = tk.Button(self.frameLower, text = 'Quit', width = 25, command = self.close_windows)
        self.updateButton.pack()
        self.quitButton.pack()
    def add_label_window(self):
        self.addLW = tk.Toplevel(self.master)
        self.addLWFrame = tk.Frame(self.addLW)
        self.addLWFRow0 = tk.Frame(self.addLWFrame)
        self.addLWFRow1 = tk.Frame(self.addLWFrame)
        self.addLWFRow2 = tk.Frame(self.addLWFrame)
        self.addLWFRow3 = tk.Frame(self.addLWFrame)
        self.updateText0 = tk.StringVar()
        self.updateText1 = tk.StringVar()
        self.updateText2 = tk.StringVar()
        self.updateText3 = tk.StringVar()
        self.addLWLabel0 = tk.Label(self.addLWFRow0, text='Entry 0:', width=25, anchor='e')       
        self.addLWFEntry0 = tk.Entry(self.addLWFRow0, textvariable=self.updateText0)
        self.addLWLabel1 = tk.Label(self.addLWFRow1, text='Entry 0001:', )       
        self.addLWFEntry1 = tk.Entry(self.addLWFRow1, textvariable=self.updateText1)
        self.addLWLabel2 = tk.Label(self.addLWFRow2, text='Entry 02:', )       
        self.addLWFEntry2 = tk.Entry(self.addLWFRow2, textvariable=self.updateText2)
        self.addLWLabel3 = tk.Label(self.addLWFRow3, text='Entry 3:', )       
        self.addLWFEntry3 = tk.Entry(self.addLWFRow3, textvariable=self.updateText3)
        self.addLWUpdateB = tk.Button(self.addLWFrame, text = 'Save and Quit', width = 25, command = self.update_label)
        self.addLWLabel0.pack(side=tk.LEFT)
        self.addLWFEntry0.pack(side=tk.LEFT)
        self.addLWLabel1.pack(side=tk.LEFT)
        self.addLWFEntry1.pack(side=tk.LEFT)
        self.addLWLabel2.pack(side=tk.LEFT)
        self.addLWFEntry2.pack(side=tk.LEFT)
        self.addLWLabel3.pack(side=tk.LEFT)
        self.addLWFEntry3.pack(side=tk.LEFT)
        self.addLWFRow0.pack()
        self.addLWFRow1.pack()
        self.addLWFRow2.pack()
        self.addLWFRow3.pack()
        self.addLWUpdateB.pack()
        self.addLWFrame.pack()
    def update_label(self):
        newTask = toDoTask(self.updateText0.get(),self.updateText1.get(),self.updateText2.get(), self.updateText3.get())
        self.label1.set(newTask.getInfo()[0]+newTask.getInfo()[1]+newTask.getInfo()[2]+newTask.getInfo()[3])
        self.addLW.destroy()
    def close_windows(self):
        self.master.destroy()




# Running the GUI
def main(): 
    root = tk.Tk()
    app = tkinterGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
