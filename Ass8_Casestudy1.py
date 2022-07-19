#A website requires a user to input username and password to register.
# Write a program to check the validity of password given by user.
# Following are the criteria for checking password:
# At least 1 letter between [a-z]2. At least 1 number between [0-9]
# At least 1 letter between [A-Z]3.
# At least 1 character from [$#@]4. Minimum length of transaction password: 65.
# Maximum length of transaction password: 12#
# Importing the regular expression
import re
x = []
password = [item for item in input().split(',')]
for passwd in password:
    if len(passwd)<6 or len(passwd)>12:
        continue
    else:
        passwd
    if not re.search("[a-z]",passwd):
        print(passwd)
        continue
    elif not re.search("[0-9]",passwd):
        continue
    elif not re.search("[A-Z]",passwd):
        continue
    elif not re.search("[$#@]",passwd):
        continue
    elif re.search("\s",passwd):
        continue
    else:
        passwd
    x.append(passwd)
print(",".join(x))