#By using list comprehension, please write a program to print the list after
# removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].


list = [12,24,35,70,88,120,155]
newlist1 = []
for x in range(len(list)):
    if x not in (0,4,5):
        newlist1.append(list[x])
print(newlist1)