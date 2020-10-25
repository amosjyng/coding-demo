from os import path

contact_file = "contacts.txt"

if path.exists(contact_file):
    f = open(contact_file, "r")
    name, number = f.read().split("\t")
    print("I got your contact info! You are {0}, your number is {1}"
        .format(name, number))
else:
    f = open(contact_file, "w")
    name = input("I don't have anything on file for you. Enter your name: ")
    number = input("Enter your number: ")
    f.write("""{0}\t{1}""".format(name, number))
    f.close()
