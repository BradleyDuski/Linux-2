from flask import Flask

app = Flask(__name__)

@app.get("/")
def profile():
    out = {
        "fist_name": "Brad",
        "last_name": "Duski",
        "hobbies": "video games",
        "is_online": True
    }
    return out

@app.get("/greet/<name>")
def greeting(name):
    out = {
        "ok": True,
        "message": "Hello, %s! Welcome to our site." % name
    }
    return out

@app.get("/sum/<int:x>/<int:y>/")
def sum(x,y):
    out = {
        "ok": True,
        "result": x+y
    }
    return out