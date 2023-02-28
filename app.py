from flask import Flask, redirect, render_template, request, session, url_for
from flask_session import Session
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from chat import bot

app = Flask(__name__)
# Add Database/MySQl
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:IdlP#bxj59@localhost/conversations'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:IdlP#bxj59@localhost/our_users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Secret Key
app.config['SECRET_KEY'] = "No one knows what it is"

# Initialize the Database
db = SQLAlchemy(app)

# Create a Model
# class Conversations(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     email = db.Column(db.String(255), nullable=False)
#     date_added = db.Column(db.DateTime, default=datetime.utcnow)
#
#     # Create A String
#     def __init__(self, name, email, date_added):
#         self.name = name
#         self.email = email
#         self.date_added = date_added


# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.run()