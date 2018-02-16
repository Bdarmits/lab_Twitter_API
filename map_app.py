'''
simple flask app with locations of twitter friends and names
'''
from flask import  Flask, render_template

app = Flask(__name__)

@app.route("/")
def prod():
    return  render_template("friends_locaion.html")

if __name__ == "__main__":
    app.run(debug = True)