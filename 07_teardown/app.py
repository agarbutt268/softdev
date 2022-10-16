'''
Team CertifiedCoderBoys: Emerson Gelobter, Aden Garbutt
SoftDev
K07 -- teardown
2022-10-03
time spent: 0.5
'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
Q0: python vars??
Q1: URLs, file pathways
Q2: On webpage?
Q3: what ever value is assgined to "__name__"
Q4: On webpage? I dont!
Q5: Java, python


INVESTIGATIVE APPROACH:
 we will utilize the process of trial and error
 and expirmentation! Science!!
'''