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
    def __init__(self, zone, timeallotted, duedate, finishdate=""):
        self.zone = zone 
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
        self.initialFraming()
        self.initialTaskColumnFraming()
        self.label1 = tk.StringVar()
        self.label1.set("test")
        self.sectionLabel1 = tk.Label(self.frameTitles, textvariable=self.label1)
        self.sectionLabel1.pack()
        self.updateButton = tk.Button(self.frameLower, text = 'Update', width = 25, command = self.updateLabel)
        self.updateButton.pack()
        self.quitButton = tk.Button(self.frameLower, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
    def initialFraming(self):
        self.frameTitles = tk.Frame(self.master, bg='white', width=900, height=100, padx=3, pady=3)
        self.frameTitles.pack()
        self.frameUpper = tk.Frame(self.master, bg='cyan', width=900, height=400)
        self.frameUpper.pack()
        self.frameLower = tk.Frame(self.master, bg='white', width=900, height=100, padx=3, pady=3)
        self.frameLower.pack()
    def initialTaskColumnFraming(self):
        self.frameStartList = tk.Frame(self.frameUpper, bg='light blue', width=300, height=400, padx=3, pady=3)
        self.frameStartList.pack(side=tk.LEFT)
        self.frameInProgress = tk.Frame(self.frameUpper, bg='dark salmon', width=300, height=400, padx=3, pady=3)
        self.frameInProgress.pack(side=tk.LEFT)
        self.frameFinished = tk.Frame(self.frameUpper, bg='dark sea green', width=300, height=400, padx=3, pady=3)
        self.frameFinished.pack(side=tk.LEFT)
    def updateLabel(self):
        self.label1.set("updated")
    def close_windows(self):
        self.master.destroy()


#testing = toDoTask('initial',30,'Jan 1')
#print testing.getInfo()

def main(): 
    root = tk.Tk()
    app = tkinterGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
