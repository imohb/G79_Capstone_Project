from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Create object of ChatBot class
bot = ChatBot('Karty')

# Create object of ChatBot class with Storage Adapter
bot = ChatBot(
    'Karty',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    # database = 'mysql+pymysql://root:IdlP#bxj59@localhost/conversations',
    # database_uri='mysql+pymysql://root:IdlP#bxj59@localhost/conversations'
)
# Add Database/MySQl
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:IdlP#bxj59@localhost/conversations'
# Secret Key
app.config['SECRET_KEY'] = "No one knows what it is"

# Initialize the Database
db = SQLAlchemy(app)


# Create a Model
class Conversations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bot_text = db.Column(db.String(200), nullable=False)
    human_text = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

# Create object of ChatBot class with Logic Adapter
bot = ChatBot(
    'Karty',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
)

trainer = ListTrainer(bot)
trainer.train([
'Hi',
'Hello',
'I need your assistance regarding my order',
'Please, Provide me with your order id',
'I have a complaint.',
'Please elaborate, your concern',
'How long it will take to receive an order ?',
'An order takes 3-5 Business days to get delivered.',
'Okay Thanks',
'No Problem! Have a Good Day!'
])

# Get a response to the input text 'I would like to book a flight.'
response = bot.get_response('I have a complaint.')
print("Bot Response:", response)


# Configure app
app = Flask(__name__)

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