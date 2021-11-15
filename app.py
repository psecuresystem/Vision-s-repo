from flask import Flask,render_template,request
from datetime import datetime, time
from mongoengine import *
from mongoengine.connection import connect
from mongoengine.document import Document
from mongoengine.errors import NotUniqueError
from mongoengine.fields import DateTimeField, IntField, StringField
from werkzeug.utils import redirect
app = Flask(__name__)

database = connect(host = 'mongodb+srv://prosper:danz1234@cluster0.f0a5l.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

class User(Document):
    name = StringField(required=True)
    phone = IntField(min_value=7000000000,max_value=9999999999)
    time = DateTimeField()
    meta = {
        'collection':'Worship'
    }
    def strtime(self):
        return self.time.strftime('%H:%M')

@app.route('/',methods = ['GET'])
def home():
    return render_template('index.html')

@app.route('/',methods = ['POST'])
def getworshiphour():
    name = request.form.get('name')
    time = request.form.get('time')
    phone = int(request.form.get('phone'))
    time_values = time.split(':')
    time_formatted=datetime(2021,11,11,int(time_values[0]),int(time_values[1]))
    user = User()
    user.name = name
    user.phone = phone
    user.time = time_formatted
    try:
        user.save()
    except NotUniqueError:
         return render_template('index.html',error = 'You are already registered')
    return render_template('index.html',success=True)

app.run()