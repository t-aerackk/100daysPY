#Day 3 its going good lets try spilit and strip functions
a=" Anjali"

print(a) #outputs space Anjal
print(a.strip('i')) #outputs Anjal without i

name=str(input("Enter your Name:"))
print(name.strip()) #strip removes whitespace 


#split functions as a splitter 
a="anjal, thapa, is good guy"
print(a.split(','))
print(a)