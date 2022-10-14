'''
Team Whole Lotta Coding: Prattay Dey, Emerson Gelobter, Aden Garbutt
SoftDev
K09 -- static
2022-10-11
time spent: 0.5 hr
'''

# DEMO 
# basics of /static folder

from flask import Flask
app = Flask(__name__) 

@app.route("/")       
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo hello!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
