
import os
from flask import Flask, session, redirect, url_for, escape, request, render_template, Response, send_from_directory
from lib import app
import json
from flask.ext.classy import FlaskView,route
from pymongo import MongoClient, ASCENDING, DESCENDING



client = MongoClient('mongodb://localhost:27017')

db = client.team_E

user = db.userInfo

mainInfo = db.mainInfo



@app.route('/')
def route_display():
    return render_template('index.html')


class HelloView(FlaskView):
    def __init__(self):
        self.PIKA = HI(10)
    @route('/search', methods=['GET','POST'])
    def hii(self):

        city = request.form['city']
        date = request.form['date']
        role = request.form['role']

        if role == 0:
            elor = 1
        else:
            elor = 0
        
        asked_info = mainInfo.find({city:'city',date:'date',elor:"role"})
        
        print city,date,role
        print asked_info
        
        return "searched"

    
    @route('/insert', methods=['GET','POST'])
    def data_input(self):

        
        city = request.form['city']
        date = request.form['date']
        role = request.form['role']
        
        mainInfo.insert({'city':city,'date':date,'role':role})
        
        
        print city,date,role,"inserted!!"
        

        
        return "requested"

    
    @route('/post_offer', methods=['GET','POST'])
    def p_offer(self):

                
        return "offerred"

class HI:
  xx = 5
  def __init__(self,x=3):
    print ("hi")
    self.x = x
    print(self.x)
    #print (xx)
  def kimi(self):
    self.x += 2
    self.xx += 2
    print(HI().xx)
    print(self.x)

HelloView.register(app)
