## Goal is to pull up notes on the 6 mons in your team so you know who to prioritize and what to watch for
## Maybe identify the top weaknesses 

import json


#####
## Examples for json 
# some JSON:
#x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
#y = json.loads(x)
# the result is a Python dictionary:
#print(y["age"])
######
# a Python object (dict):
#x = {
#  "name": "John",
#  "age": 30,
#  "city": "New York"
#}
# convert into JSON:
#y = json.dumps(x)
# the result is a JSON string:
#print(y)
#####



class Pokemon():
    def __init__(self, name, notes):
        self.name = name 
        self.notes = notes 

    def addNotes(self, newnotes):
        self.notes = newnotes 

    def expandNotes(self, newnotes):
        self.notes = self.notes + '\n' + newnotes 


x = '{"name":"Bulbasaur","notes":"Da Bestest Mon"}'
y = json.loads(x)
z = Pokemon(y["name"],y["notes"])
print z.name 
print z.notes
z.expandNotes('Def #1')
print z.notes 

a = {
    "notes": z.notes,
    "name": z.name
}
b = json.dumps(a) 
print (b)


