from os import path
import json

contact_file = "contacts.txt"

if path.exists(contact_file):
    f = open(contact_file, "r")
    result = json.loads(f.read())
    print("I got your contact info! You are {0}, your number is {1}"
        .format(result['name'], result['number']))
else:
    f = open(contact_file, "w") # w for write
    name = input("I don't have anything on file for you. Enter your name: ")
    number = input("Enter your number: ")
    f.write(json.dumps({"name": name, "number": number}))
    f.close()
