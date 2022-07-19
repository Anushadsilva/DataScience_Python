#4.Write a program that accepts a sentence and calculate the number of letters and digits.Suppose if the entered
# string is: Python0325 Then the output will be:LETTERS: 6DIGITS:4Hint: Use built-in functions of string


x = input("Enter the sentence")
j = {"DIGITS": 0 , "LETTERS": 0 }
for i in x:
    if i.isdigit():
        j["DIGITS"] += 1
    elif i.isalpha():
        j["LETTERS"] += 1
    else:
        pass
print("LETTERS", j["LETTERS"])
print("DIGITS",j["DIGITS"])