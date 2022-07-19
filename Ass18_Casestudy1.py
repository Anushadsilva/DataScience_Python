#Domain –Telecomfocus –OptimizationBusiness challenge/requirementLifeTel
# Telecomis the latest entrant in the highly competitive Telecom market of Singapore.
# It issues SIM to the verified users.  Till now verification was manual through the photocopy of approved id card document.
# However,government has recently introduced Social ID called Reference ID which is mapped to
# fingerprint of user.LifeTel should now verify user against the fingerprint and
# Reference IDKey issuesBuild a system where when user enters Reference ID it is encrypted,
# so that hackers cannot view the mapping of Reference ID and finger printConsiderationsSystem should be
# secureData volume-NAAdditional information-NABusiness benefitsCompany will be able to quickly issue SIM to user
# and expected gain in volume is approximately 10 times as the manual process of verification is replaced with
# secure automated system
# Approach to Solve
# You have to use fundamentals of Python taught in module
# 11.Read the input from command line –Reference ID2.Check for validity –it should be 12 digits and
# allows on number andalphabet
#3.Encrypt the Reference ID and print it for referenceEnhancements for code
# You can try these enhancements in code1.Allow some special characters in ReferenceID2.
# Give the option for decryption to user


import re
from cryptography.fernet import Fernet

message = input("Enter the referenceid ")

if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{12}', message):
    ende = input("Enter if message to be encrypted, type E : ")
    key = Fernet.generate_key()
    fernet = Fernet(key)
    if ende == 'E':
        encMessage = fernet.encrypt(message.encode())
        print("original string: ", message)
        print("encrypted string: ", encMessage)
        dec = input("Enter if message to be decrypted, type D : ")
        if dec == 'D':
            decMessage = fernet.decrypt(encMessage).decode()
            print("decrypted string: ", decMessage)
        else:
            print("The message is still encrypted")
else:
    print("Reference id is not of 12 characters")

