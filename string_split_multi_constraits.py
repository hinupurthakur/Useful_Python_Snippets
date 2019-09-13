import re
string="1.Nupur Thakur,Jagrati/Jaggu"
names=re.split(',|[0-9].|/',string)
print(names)
while "" in names :
    names.remove("")
print(names) 
