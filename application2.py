
import os
import datetime
from datetime import timedelta
from flask import Flask, render_template, request

SXWK1 = datetime.date.today() - timedelta(days=7 )
SXWK2 = datetime.date.today() - timedelta(days=14 )
SXWK3 = datetime.date.today() - timedelta(days=21 )
SXWK4 = datetime.date.today() - timedelta(days=35 )
SXWK5 = datetime.date.today() - timedelta(days=42 )
SXWK6 = datetime.date.today() - timedelta(days=49 )
SXWK7 = datetime.date.today() - timedelta(days=56 )
SXWK8 = datetime.date.today() - timedelta(days=63 )
SXWK9 = datetime.date.today() - timedelta(days=70)
SXWK10 = datetime.date.today() - timedelta(days=77 )
SXWK11 = datetime.date.today() - timedelta(days=84 )
SXWK12 = datetime.date.today() - timedelta(days=91 )
WK1_6_ET12 = ( 'Splint:  Mallet finger splint Therapeutic exercices:   AAROM of MP/PIP. Precautions:   Daily skin check whil maintaining DIP. No active DIP motion. Other: ' ' If swan-neck deformity develops, splint PIP at 30 to 45 flexion via dorsal block splint.'
'Casting is an option, and may have better outcomes via constant circumferential positionin')
WK7_8_ET12 = ( 'Splint:  Remove splint for exercise, otherwise splint is worn continuously. Therapeutic exercices:   AROM of DIP flex/ext, 10 reps hourly.  Start at 10 degrees flexion, progress in 10-20 degree increments per week, if no extensor lag develops Precautions:   If extensor lag develops > 10 degrees, resume continuous splinting (no ROM) for 1- 2 weeks and reassess. Other: ' 'Prehension and coordination exercise should supplement ROM program.'
'None')
WK9_10_ET12 = ( 'Splint:  Gradually wean from splint during day.Continue splint at night. Therapeutic exercices:   Can introduce AAROM as needed. Precautions:  None Other: ' ' Prehension and coordination exercise should supplement ROM program.')
WK11_12_ET12 = ( 'Splint:  D/C splint. Therapeutic exercices:   PROM/PREs. Precautions:  None Other: ' ' None.')
    #to add new protocol must change 1. Key at end of plan of care to match above, 2. SXWK6 to however many weeks in segment of protocol, 3. Surgery and MD if different

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    daysago = int(name)
    t1 = datetime.date.today() - timedelta(days= daysago)
    dx=request.form.get("dx")
    if (SXWK6 <= t1) and ( dx == 'ETZ12'):
        return render_template("hello.html", name=t1, dx= WK1_6_ET12)
    elif SXWK8 <= t1 and ( dx == 'ETZ12'):
        return render_template("hello.html", name=t1, dx= WK7_8_ET12)
    elif SXWK10 <= t1 and ( dx == 'ETZ12'):
        return render_template("hello.html", name=t1, dx= WK9_10_ET12)
    elif SXWK12 <= t1 and ( dx == any):
        return render_template("hello.html", name=t1, dx= WK11_12_ET12)
    return render_template("hello.html", name=t1, dx=dx)

# app = Flask(__name__)
#
# @app.route("/")
# def index():
#     return render_template("index.html")
#
# @app.route("/hello", methods=["POST"])
# def dx():
#     dx = request.form.get("dx")
#     return render_template("hello.html", name=dx)
