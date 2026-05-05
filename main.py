#8-misol
from flask import Flask
app = Flask(__name__)

@app.route('/weather')
def weather():
    return f"Bugun quyoshli"

@app.route('/temperature')
def temperature():
    return f"Harorat 25"
