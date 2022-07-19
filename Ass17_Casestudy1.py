#Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0).Example:
#If the following n is given as input to the
#program:5Then, the output of the program should be:3.55


x = int(input("Enter the number: "))
cal=0
for j in range(1,x+1):
    cal=cal+(j/(j+1))
print("Sum of series calculated is: ",round(cal,2))