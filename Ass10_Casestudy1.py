#Please   write   a   program   which accepts  a   string   from   console
#and   print   the characters that have even indexes.Example:
#If the following string is given as input to the program:H1e2l3l4o5w6o7r8l9d
#Then, the output of the program should be:Helloworld

x = input(" Enter the string")
newitem = ""
for item in range(len(x)):
#    print(item)
    if item % 2 == 0:
        newitem = newitem + x[item]
print(newitem)