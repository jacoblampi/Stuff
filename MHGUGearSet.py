import csv 

class Gear():
    def __init__(self, name='', piece='', skills={}, slots=0, rankreq=0, huntertype='', gembenefits={}):
        self.name = name 
        self.piece = piece 
        self.skills =  skills 
        self.slots = slots 
        self.rankreq = rankreq 
        self.huntertype = huntertype
        self.gembenefits = gembenefits
    
    def clone(self):
        return Gear(self.name, self.piece, self.skills, self.slots, self.rankreq, self.huntertype)
    
    def addgems(self, gembenefits):
        newskills = {}
        for skill in gembenefits:
            if skill in self.skills:
                newskills[skill] = self.skills[skill] + gembenefits[skill]
            else:
                newskills[skill] = gembenefits[skill]
        for skill in self.skills:
            if skill in gembenefits:
                pass 
            else:
                newskills[skill] = self.skills[skill]
        return Gear(self.name, self.piece, newskills, self.slots, self.rankreq, self.huntertype, gembenefits)



class GearSet():
    def __init__(self, head, body, arms, legs, feet, gembenefits):
        self.gshead = head.clone() 
        self.gsbody = body.clone() 
        self.gsarms = arms.clone() 
        self.gslegs = legs.clone() 
        self.gsfeet = feet.clone() 
        self.gembenefits = gembenefits
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

    def printgembenefits(self):
        gembstr = ''
        for gben in self.gembenefits:
            gembstr = gembstr + gben + ' ' + str(self.gembenefits[gben]) + ' '
        return gembstr
    
    def printskills(self):
        skillstr = ''
        for skill in self.gsskills:
            skillstr = skillstr + skill + ' ' + str(self.gsskills[skill]) + ' '
        return skillstr


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


def combinedict(dict1, dict2):
    combodict = {}
    for key1 in dict1:
        if key1 in dict2:
            combodict[key1] = dict1[key1]+dict2[key1]
        else:
            combodict[key1] = dict1[key1]
    for key2 in dict2:
        if key2 in combodict:
            pass 
        else:
            combodict[key2] = dict2[key2]
    return combodict


##Test Set
#Gear
gearlist = []
#Nargacuga
gearlist.append(Gear('Narg Head','Head',{'Evade Dist':3,'Expert':2},1,4,'Blademaster'))
gearlist.append(Gear('Narg Body','Body',{'Evade Dist':2,'Expert':3},1,4,'Blademaster'))
gearlist.append(Gear('Narg Arms','Arms',{'Evade Dist':1,'Expert':3},2,4,'Blademaster'))
gearlist.append(Gear('Narg Legs','Legs',{},3,4,'Blademaster'))
gearlist.append(Gear('Narg Feet','Feet',{'Evade Dist':4},1,4,'Blademaster'))
#Ceanataur/HR
# gearlist.append(Gear('Cean Head','Head',{'Sharpness':1,'Expert':5},1,4,'Blademaster'))
gearlist.append(Gear('Cean Head S','Head',{'Sharpness':1,'Expert':6},1,4,'Blademaster'))
# gearlist.append(Gear('Cean Body','Body',{'Sharpness':2,'Expert':2},0,4,'Blademaster'))
gearlist.append(Gear('Cean Body S','Body',{'Sharpness':2,'Expert':3},0,4,'Blademaster'))
# gearlist.append(Gear('Cean Arms','Arms',{'Sharpness':4},1,4,'Blademaster'))
gearlist.append(Gear('Cean Arms S','Arms',{'Sharpness':4,'Expert':1},1,4,'Blademaster'))
# gearlist.append(Gear('Cean Legs','Legs',{'Sharpness':2,'Expert':3},0,4,'Blademaster'))
gearlist.append(Gear('Cean Legs S','Legs',{'Sharpness':2,'Expert':4},0,4,'Blademaster'))
# gearlist.append(Gear('Cean Feet','Feet',{'Sharpness':1,'Expert':3},1,4,'Blademaster'))
gearlist.append(Gear('Cean Feet S','Feet',{'Sharpness':1,'Expert':4},1,4,'Blademaster'))
#Chaos/HR
gearlist.append(Gear('Chaoshroom','Head',{'Status':3},1,4,'Blademaster'))
gearlist.append(Gear('Chaos Plate','Body',{'Status':2},2,6,'Blademaster'))
gearlist.append(Gear('Chaos Archbun','Head',{'Status':4},1,6,'Blademaster'))
gearlist.append(Gear('Chaos Archplate','Body',{'Status':2},3,6,'Blademaster'))
#Nerscylla
gearlist.append(Gear('Nerscylla Helm','Head',{'Status':2},1,6,'Blademaster'))
gearlist.append(Gear('Nerscylla Mail','Body',{'Status':1},0,6,'Blademaster'))
gearlist.append(Gear('Nerscylla Guards','Arms',{'Status':3},1,6,'Blademaster'))
gearlist.append(Gear('Nerscylla Greaves','Feet',{'Status':3},1,6,'Blademaster'))
#Insects
gearlist.append(Gear('Bnahabra Suit S','Body',{'Status':3,'Sharpness':1},0,6,'Blademaster'))
gearlist.append(Gear('Bnahabra Coil S','Legs',{'Status':4},1,6,'Blademaster'))
gearlist.append(Gear('Vespoid Greaves S','Feet',{'Status':3},2,6,'Blademaster'))
gearlist.append(Gear('Jaggi Gauntlets S','Arms',{'Expert':6},0,6,'Blademaster'))
gearlist.append(Gear('Jaggi Boots S','Feet',{'Expert':4},2,6,'Blademaster'))

#Gems
gemlist = [] 
#Tier 1
gemlist.append(Gem('Expert 1',{'Expert':1},1,2))
gemlist.append(Gem('Sharpness 1',{'Sharpness':1},1,2))
gemlist.append(Gem('Evade Dist 1',{'Evade Dist':1},1,2))
gemlist.append(Gem('Status 1',{'Status':1},1,2))
#Tier 2
gemlist.append(Gem('Expert 2',{'Expert':3},2,6))
gemlist.append(Gem('Status 2',{'Status':3},2,6))
#Tier 3
gemlist.append(Gem('Expert 3',{'Expert':5},3,8))
gemlist.append(Gem('Sharpness 3',{'Sharpness':4},3,8))
gemlist.append(Gem('Evade Dist 1',{'Evade Dist':4},3,8))
#Skills
skilllist = []
skilllist.append(Skill('Evade Dist', {'Lv1':10}))
skilllist.append(Skill('Sharpness', {'Lv1':10}))
skilllist.append(Skill('Expert', {'Lv1':10,'Lv2':15,'Lv3':20}))
skilllist.append(Skill('Status',{'Lv1':10,'Lv2':15}))
#Charm
#equippedcharm = Charm({'Expert':3},1)
equippedcharm = Charm({'Expert':3,'Status':4},0)


#State desired skills 
# skilldes = {'Expert':'Lv1','Sharpness':'Lv1','Evade Dist':'Lv1'}
skilldes = {'Evade Dist':'Lv1','Status':'Lv2','Expert':'Lv3'}

#Determine Rank Cutoff
rankcutoff = 6

#Determine available gems 
qualifiedgems1 = []
qualifiedgems2 = [] 
qualifiedgems3 = []
for gemitem in gemlist:
    if gemitem.rankreq <= rankcutoff:
        if gemitem.slotsreq == 1:
            qualifiedgems1.append(gemitem) 
        elif gemitem.slotsreq == 2:
            qualifiedgems2.append(gemitem)
        else:
            qualifiedgems3.append(gemitem)
    else:
        pass 

#Determine gem benefits
possible1slotbenefits = []
possible2slotbenefits = []
possible3slotbenefits = []
for gemitemA in qualifiedgems1:
    #1--
    possible1slotbenefits.append(gemitemA.skills)
    for gemitemB in qualifiedgems1:
        #11-
        possible2slotbenefits.append(combinedict(gemitemA.skills, gemitemB.skills))
        for gemitemC in qualifiedgems1:
            #111
            possible3slotbenefits.append(combinedict(combinedict(gemitemA.skills, gemitemB.skills),gemitemC.skills))
    for gemitemB in qualifiedgems2:
        #12
        possible3slotbenefits.append(combinedict(gemitemA.skills, gemitemB.skills))
for gemitemA in qualifiedgems2:
    #2-
    possible2slotbenefits.append(gemitemA.skills)
for gemitemA in qualifiedgems3:
    #3
    possible3slotbenefits.append(gemitemA.skills)

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
        elif gear.slots > 0:
            includeflag = 1
        else:
            pass 
    if includeflag == 1:
        if gear.piece == 'Head':
            if gear.slots == 1:
                for benefits in possible1slotbenefits:
                    qualifiedgearh.append(gear.addgems(benefits))
            elif gear.slots == 2:
                for benefits in possible2slotbenefits:
                    qualifiedgearh.append(gear.addgems(benefits))
            elif gear.slots == 3:
                for benefits in possible3slotbenefits:
                    qualifiedgearh.append(gear.addgems(benefits))
            else:
                qualifiedgearh.append(gear)
        elif gear.piece == 'Body':
            if gear.slots == 1:
                for benefits in possible1slotbenefits:
                    qualifiedgearb.append(gear.addgems(benefits))
            elif gear.slots == 2:
                for benefits in possible2slotbenefits:
                    qualifiedgearb.append(gear.addgems(benefits))
            elif gear.slots == 3:
                for benefits in possible3slotbenefits:
                    qualifiedgearb.append(gear.addgems(benefits))
            else:
                qualifiedgearb.append(gear)
        elif gear.piece == 'Arms':
            if gear.slots == 1:
                for benefits in possible1slotbenefits:
                    qualifiedgeara.append(gear.addgems(benefits))
            elif gear.slots == 2:
                for benefits in possible2slotbenefits:
                    qualifiedgeara.append(gear.addgems(benefits))
            elif gear.slots == 3:
                for benefits in possible3slotbenefits:
                    qualifiedgeara.append(gear.addgems(benefits))
            else:
                qualifiedgeara.append(gear)
        elif gear.piece == 'Legs':
            if gear.slots == 1:
                for benefits in possible1slotbenefits:
                    qualifiedgearl.append(gear.addgems(benefits))
            elif gear.slots == 2:
                for benefits in possible2slotbenefits:
                    qualifiedgearl.append(gear.addgems(benefits))
            elif gear.slots == 3:
                for benefits in possible3slotbenefits:
                    qualifiedgearl.append(gear.addgems(benefits))
            else:
                qualifiedgearl.append(gear)
        elif gear.piece == 'Feet':
            if gear.slots == 1:
                for benefits in possible1slotbenefits:
                    qualifiedgearf.append(gear.addgems(benefits))
            elif gear.slots == 2:
                for benefits in possible2slotbenefits:
                    qualifiedgearf.append(gear.addgems(benefits))
            elif gear.slots == 3:
                for benefits in possible3slotbenefits:
                    qualifiedgearf.append(gear.addgems(benefits))
            else:
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
                    totalgembenefits = combinedict(hgear.gembenefits,combinedict(bgear.gembenefits,combinedict(agear.gembenefits,combinedict(lgear.gembenefits,fgear.gembenefits))))
                    gearset = GearSet(hgear, bgear, agear, lgear, fgear, totalgembenefits)
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


with open('sets.csv', 'wb') as csvfile:
    gswriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    gswriter.writerow(['GS','Head','Body','Arms','Legs','Feet','Gems','Skills'])
    gsid = 0
    for gearset in viablegearsets:
        gswriter.writerow([str(gsid), gearset.gshead.name, gearset.gsbody.name, gearset.gsarms.name, gearset.gslegs.name, gearset.gsfeet.name, gearset.printgembenefits(), gearset.printskills()])
        gsid += 1

# for item in viablegearsets:
#     print ''
#     print item.gsnames()
#     print item.gsskills
#     print item.gembenefits
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
