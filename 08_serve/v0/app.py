'''
Team WholeLotOfCoding: Aden Garbutt, Emerson Gelobter, Prattay Dey
SoftDev
08_serve
2022-10-06
time spent: 
DISCO:
- 
QCC:
-
OPS SUMMARY:
-
'''


from flask import Flask
app = Flask(__name__) # _name- 

@app.route("/") # 
def hello_world():
    print(__name__) # ...
    return "No hablo queso!"  #displays "No hablo queso!" on the screen

app.run()  # ...
                