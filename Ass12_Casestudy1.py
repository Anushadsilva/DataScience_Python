#Please write a program which count and print the numbers of each character in a string input by console.
# Example: If the following string is given as input to the program:abcdefgabc
# Then, the output of the program should be:a,2c,2b,2e,1d,1g,1f,1


from collections import Counter
inp = input(" Enter the string ")
col = Counter(inp)
print(col)