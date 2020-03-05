import random 
#PullSim 
class PullAttempt():
    def __init__(self):
        self.urchance = .05 

    def pull(self):
        if random.random() < self.urchance:
            return True
        else:
            return False 

class SingleRun():
    def __init__(self):
        self.pulled = False 
        self.gemsused = 0

avgattemptlist = {50:[],60:[],70:[],75:[],80:[],85:[],90:[],95:[]}
for jj in range(0,100):
    attemptlist = []
    for ii in range(0,1000):
        thisrun = SingleRun()
        while thisrun.pulled == False:
            if PullAttempt().pull() :
                thisrun.gemsused += 50
                if random.random() < .5: #50-50 of correct ur
                    thisrun.pulled = True
                else:
                    pass
            else:
                thisrun.gemsused += 50
        attemptlist.append(thisrun.gemsused)

    attemptlist.sort() 
    avgattemptlist[50].append(attemptlist[500])
    avgattemptlist[60].append(attemptlist[600])
    avgattemptlist[70].append(attemptlist[700])
    avgattemptlist[75].append(attemptlist[750])
    avgattemptlist[80].append(attemptlist[800])
    avgattemptlist[85].append(attemptlist[850])
    avgattemptlist[90].append(attemptlist[900])
    avgattemptlist[95].append(attemptlist[950])

print sum(avgattemptlist[50])/len(avgattemptlist[50])
print sum(avgattemptlist[60])/len(avgattemptlist[60])
print sum(avgattemptlist[70])/len(avgattemptlist[70])
print sum(avgattemptlist[75])/len(avgattemptlist[75])
print sum(avgattemptlist[80])/len(avgattemptlist[80])
print sum(avgattemptlist[85])/len(avgattemptlist[85])
print sum(avgattemptlist[90])/len(avgattemptlist[90])
print sum(avgattemptlist[95])/len(avgattemptlist[95])
