
class Gear():
    def __init__(self, name='', piece='', skills={}, slots=0, rankreq=0, huntertype=''):
        self.name = name 
        self.piece = piece 
        self.skills =  skills 
        self.slots = slots 
        self.rankreq = rankreq 
        self.huntertype = huntertype
    
    def clone(self):
        return Gear(self.name, self.piece, self.skills, self.slots, self.rankreq, self.huntertype)

class GearSet():
    def __init__(self, head, body, arms, legs, feet):
        self.gshead = head.clone() 
        self.gsbody = body.clone() 
        self.gsarms = arms.clone() 
        self.gslegs = legs.clone() 
        self.gsfeet = feet.clone() 
        self.gsskills = self.setskills()

    def setskills(self):
        gsskills = {}
        for gobj in [self.gshead, self.gsbody, self.gsarms, self.gslegs, self.gsfeet]:
            for skill in gobj.skills:
                if skill in gsskills:
                    gsskills[skill] = gsskills[skill] + gobj.skills[skill]
                else:
                    gsskills[skill] = gobj.skills[skill]
        return gsskills

    def gsnames(self):
        return self.gshead.name + ' // ' + self.gsbody.name + ' // ' + self.gsarms.name + ' // ' + self.gslegs.name + ' // ' + self.gsfeet.name


class Gem():
    def __init__(self, name='', skills={}, slotsreq=0, rankreq=0):
        self.name = name 
        self.skills = skills 
        self.slotsreq = slotsreq 
        self.rankreq = rankreq

class Skill():
    def __init__(self, name='', threshold={}):
        self.name = name 
        self.threshold = threshold 

class Charm():
    def __init__(self, skills={}, slots=0):
        self.skills = skills 
        self.slots = slots 

#Test Set
gearlist = []
#Nargacuga
gearlist.append(Gear('Narg Head','Head',{'Evade Dist':3,'Expert':2},2,4,'Blademaster'))
gearlist.append(Gear('Narg Body','Body',{'Evade Dist':2,'Expert':2},1,4,'Blademaster'))
gearlist.append(Gear('Narg Arms','Arms',{'Evade Dist':1,'Expert':3},2,4,'Blademaster'))
gearlist.append(Gear('Narg Legs','Legs',{},3,4,'Blademaster'))
gearlist.append(Gear('Narg Feet','Feet',{'Evade Dist':4},1,4,'Blademaster'))
#Ceanataur
gearlist.append(Gear('Cean Head','Head',{'Sharpness':1,'Expert':5},1,4,'Blademaster'))
gearlist.append(Gear('Cean Body','Body',{'Sharpness':2,'Expert':2},0,4,'Blademaster'))
gearlist.append(Gear('Cean Arms','Arms',{'Sharpness':4},1,4,'Blademaster'))
gearlist.append(Gear('Cean Legs','Legs',{'Sharpness':2,'Expert':3},0,4,'Blademaster'))
gearlist.append(Gear('Cean Feet','Feet',{'Sharpness':1,'Expert':3},1,4,'Blademaster'))
#Jaggi
gearlist.append(Gear('Jaggi Head','Head',{'Attack':3,'Fire Atk':1},0,4,'Blademaster'))
gearlist.append(Gear('Jaggi Body','Body',{'Attack':3},0,4,'Blademaster'))
gearlist.append(Gear('Jaggi Arms','Arms',{'Expert':4},0,4,'Blademaster'))
gearlist.append(Gear('Jaggi Legs','Legs',{'Attack':4},1,4,'Blademaster'))
gearlist.append(Gear('Jaggi Feet','Feet',{'Expert':3},2,4,'Blademaster'))

gemlist = [] 
#Tier 1
gemlist.append(Gem('Expert 1',{'Expert':1},1,2))
gemlist.append(Gem('Sharpness 1',{'Sharpness':1},1,2))
gemlist.append(Gem('Evade Dist 1',{'Evade Dist':1},1,2))
#Tier 2
gemlist.append(Gem('Expert 2',{'Expert':3},2,6))
#Tier 3
gemlist.append(Gem('Expert 3',{'Expert':5},3,8))
gemlist.append(Gem('Sharpness 3',{'Sharpness':4},3,8))
gemlist.append(Gem('Evade Dist 1',{'Evade Dist':4},3,8))

skilllist = []
skilllist.append(Skill('Evade Dist', {'Lv1':10}))
skilllist.append(Skill('Sharpness', {'Lv1':10}))
skilllist.append(Skill('Expert', {'Lv1':10,'Lv2':15,'Lv3':20}))

#equippedcharm = Charm({'Expert':3},1)
equippedcharm = Charm({'Expert':4},0)


#State desired skills 
skilldes = {'Expert':'Lv1', 'Evade Dist':'Lv1'}

#Determine Rank Cutoff
rankcutoff = 6

#Determine available gems 
qualifiedgems = []
for gemitem in gemlist:
    if gemitem.rankreq <= rankcutoff:
        qualifiedgems.append(gemitem) 
    else:
        pass 

#Determine gem benefits
#Do this one later

#Determine necessary skill points needed (based on charm)
#desired skill will be something like {"Evade Dist":"Lv1"], "Sharpness":"Lv1", "Expert":"Lv1"}
spneeded = {}
for skill in skilldes:
    ii = 0
    while ii < len(skilllist):
        if skilllist[ii].name == skill:
            tierdic = skilllist[ii].threshold
            spneeded[skill] = tierdic[skilldes[skill]]
            break
        else:
            ii += 1

#Apply charm effects 
#no gems yet
for skill in equippedcharm.skills:
    spneeded[skill] = spneeded[skill]-equippedcharm.skills[skill]

#Determine qualifying gear
#no slots yet
qualifiedgearh = []
qualifiedgearb = []
qualifiedgeara = []
qualifiedgearl = []
qualifiedgearf = []
for gear in gearlist:
    includeflag = 0
    for skill in skilldes:
        if skill in gear.skills:
            includeflag = 1
        else:
            pass 
    if includeflag == 1:
        if gear.piece == 'Head':
            qualifiedgearh.append(gear)
        elif gear.piece == 'Body':
            qualifiedgearb.append(gear)
        elif gear.piece == 'Arms':
            qualifiedgeara.append(gear)
        elif gear.piece == 'Legs':
            qualifiedgearl.append(gear)
        elif gear.piece == 'Feet':
            qualifiedgearf.append(gear)
        else:
            pass

#Test all gearsets
viablegearsets = []
for hgear in qualifiedgearh:
    for bgear in qualifiedgearb:
        for agear in qualifiedgeara:
            for lgear in qualifiedgearl:
                for fgear in qualifiedgearf:
                    gearset = GearSet(hgear, bgear, agear, lgear, fgear)
                    addflag = 0
                    for skill in spneeded:
                        if skill in gearset.gsskills and gearset.gsskills[skill] >= spneeded[skill]:
                            addflag += 1
                        else:
                            pass 
                    if addflag == len(spneeded):
                        viablegearsets.append(gearset)
                    else:
                        pass 


for item in viablegearsets:
    print item.gsnames()
    print item.gsskills
# print gearset.gsskills
# print gearset
# print gearset.gshead.name 
# print gearset.gshead.skills 
# for item in qualifiedgearh:
#     print item.name
# for item in qualifiedgearb:
#     print item.name
# for item in qualifiedgeara:
#     print item.name
# for item in qualifiedgearl:
#     print item.name
# for item in qualifiedgearf:
#     print item.name
