# Build the program like you'd use a visual interface

# Gear exists as individual pieces
class Gear():
    def __init__(self, name='', piece='', skills={}, slots=0, rankreq=0, huntertype=''):
        self.name = name 
        self.piece = piece 
        self.skills = skills
        self.slotsmax = slots
        self.slotsopen = slots
        self.slotsused = 0
        self.rankreq = rankreq 
        self.huntertype = huntertype


class GearSet():
    def __init__(self, head=Gear(), body=Gear(), arms=Gear(), legs=Gear(), feet=Gear()):
        self.gs = {'Head':head, 'Body':body, 'Arms':arms, 'Legs':legs, 'Feet':feet}
        self.gsslots = self.updateslots()
        self.gsskills = self.setskills()

    def addgear(self, gobj):
        self.gs[gobj.piece] = gobj 
        self.gsskills = self.setskills()

    def removegear(self, piece):
        self.gs[piece] = Gear()
        self.gsskills = self.setskills()

    def updateslots(self):
        slots = {}
        for key in self.gs:
            slots[self.gs[key].piece] = [self.gs[key].slotsmax, self.gs[key].slotsused, self.gs[key].slotsopen]
        return slots

    def setskills(self):
        gsskills = {}
        for gkey in self.gs:
            for skill in self.gs[gkey].skills:
                if skill in gsskills:
                    gsskills[skill] = gsskills[skill] + self.gs[gkey].skills[skill]
                else:
                    gsskills[skill] = self.gs[gkey].skills[skill]
        return gsskills





################################################################################
#### Testing Area ##############################################################
################################################################################
#Gear
gearlist = []
#Nargacuga
gearlist.append(Gear('Narg Head','Head',{'Evade Dist':3,'Expert':2},1,4,'Blademaster'))
gearlist.append(Gear('Narg Body','Body',{'Evade Dist':2,'Expert':3},1,4,'Blademaster'))
gearlist.append(Gear('Narg Arms','Arms',{'Evade Dist':1,'Expert':3},2,4,'Blademaster'))
gearlist.append(Gear('Narg Legs','Legs',{},3,4,'Blademaster'))
gearlist.append(Gear('Narg Feet','Feet',{'Evade Dist':4},1,4,'Blademaster'))
gearlist.append(Gear('Cean Body','Body',{'Sharpness':2,'Expert':2},0,4,'Blademaster'))

testgs2 = GearSet(gearlist[0], gearlist[1], gearlist[2], gearlist[3], gearlist[4])

print testgs2.gsskills
print testgs2.gsslots

