import os
from flask import Flask, session, redirect, url_for, escape, request, render_template, Response, send_from_directory
from lib import app
import json
from flask.ext.classy import FlaskView,route

@app.route('/')
def route_display():
    return render_template('index.html')


class HelloView(FlaskView):
    def __init__(self):
        self.PIKA = HI(10)
    @route('/init', methods=['GET','POST'])
    def hii(self):
        self.PIKA = HI(20)
        return "hi"
    @route('/hoge', methods=['GET','POST'])
    def index(self):
        HI().kimi()
        self.PIKA.kimi()
        return "hello world"

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