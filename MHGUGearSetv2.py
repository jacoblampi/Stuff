# Build the program like you'd use a visual interface

# Gear exists as individual pieces 
# Beginning with no gems, 
class Gear():
    def __init__(self, name='', piece='', skills={}, slotsmax=0, rankreq=0, huntertype=''):
        self.name = name 
        self.piece = piece 
        self.skills =  skills 
        self.slotsmax = slotsmax 
        self.slotsused = 0
        self.slotsopen = slotsmax
        self.rankreq = rankreq 
        self.huntertype = huntertype
        self.gems = []

    def addgem(self, gem):
        self.gems.append(gem)
        for key in gem.skills:
            if key in self.skills:
                self.skills[key] += gem.skills[key]
            else:
                self.skills[key] = gem.skills[key]
        self.slotsused += gem.slotsreq 
        self.slotsopen = self.slotsmax - self.slotsused
    
    def removegems(self):
        for gem in self.gems:
            for key in gem.skills:
                self.skills[key] -= gem.skills[key]
        newskilldict = {}
        for key in self.skills:
            if self.skills[key] != 0:
                newskilldict[key] = self.skills[key]
            else:
                pass
        self.skills = newskilldict
        self.gems = []
        self.slotsused = 0
        self.slotsopen = self.slotsmax


class Gem():
    def __init__(self, name='', skills={}, slotsreq=0, rankreq=0):
        self.name = name 
        self.skills = skills 
        self.slotsreq = slotsreq 
        self.rankreq = rankreq


class GearSet():
    def __init__(self, head=Gear(), body=Gear(), arms=Gear(), legs=Gear(), feet=Gear()):
        self.gs = {'Head':head, 'Body':body, 'Arms':arms, 'Legs':legs, 'Feet':feet}
        self.gsslots = self.determineslots()
        self.gsslotsopen = self.determineopenslots()
        self.gsskills = self.setskills()
        
    def addgear(self, gobj):
        self.gs[gobj.piece] = gobj 
        self.gsskills = self.setskills()

    def removegear(self, piece):
        self.gs[piece] = Gear()
        self.gsskills = self.setskills()
    
    def determineslots(self):
        gsslots = {}
        for gkey in self.gs:
            gsslots[gkey] = [self.gs[gkey].slotsused, self.gs[gkey].slotsopen, self.gs[gkey].slotsmax]
        return gsslots

    def determineopenslots(self):
        openslots = {0:0, 1:0, 2:0, 3:0}
        for key in self.gsslots:
            openslots[self.gsslots[key][1]] += 1
        return openslots

    def setskills(self):
        gsskills = {}
        for gkey in self.gs:
            for skill in self.gs[gkey].skills:
                if skill in gsskills:
                    gsskills[skill] = gsskills[skill] + self.gs[gkey].skills[skill]
                else:
                    gsskills[skill] = self.gs[gkey].skills[skill]
        return gsskills

    def addgem(self, gem, piecekey):
        self.gs[piecekey].addgem(gem)
        self.gsskills = self.setskills()
    
    def removegems(self, piecekey):
        self.gs[piecekey].removegems()
        self.gsskills = self.setskills()







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
# print testgs2.gsslots
# print testgs2.gsslotsopen
# for key in testgs.gs:
#     print testgs.gs[key].skills

gemlist = [] 
#Tier 1
gemlist.append(Gem('Sharpness 1',{'Sharpness':1},1,2))
gemlist.append(Gem('Expert 1',{'Expert':1},1,2))

testgear = gearlist[0]
testgem = gemlist[0]

testgs2.addgem(testgem, 'Head')
print testgs2.gsskills

testgs2.removegems('Head')
print testgs2.gsskills
