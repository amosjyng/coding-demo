from os import path
import json
from flask import Flask

contact_file = "contacts.json"

app = Flask(__name__)

def backend():
    f = open(contact_file, "r")
    result = json.loads(f.read())
    return result['name'], result['number']

@app.route('/')
def hello_world():
    name, number = backend()
    return("""
        <html>
            <body>
                <h1>Hello {0}</h1>
                <p>Your number is {1}</p>
            </body>
        </html>
    """.format(name, number))
