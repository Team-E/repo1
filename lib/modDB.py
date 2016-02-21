from __future__ import print_function
from datetime import date, datetime, timedelta
#import mysql.connector

from mysql import connector


def opendb():
        config = {
          'user': 'test',
          'password': 'test',
          'host': '192.168.0.145',
          'database': 'angels',
          'raise_on_warnings': True,
        }
         
        try:
          cnx = mysql.connector.connect(**config)
         # cursor = cnx.cursor()
        except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
          else:
            print(err)
        else:
          print ("connection success")
          return cnx
          
         # add_profile = ("INSERT INTO profile (username, password, name, gender, post, city, email, phone, type) VALUES ('login2','pass3','name3','1','0','0','test3@test3','123456','0') ")
          
        #  data_profile = ('login2','pass3','name3','1','0','0','test3@test3','123456','0')
        #  cursor.execute(add_profile, data_profile)
          #cursor.execute(add_profile)
          #cnx.commit()
          
          #cursor.close()

def closedb(cnx):
            cnx.close()

def add_profile(cnx):
            
            cursor = cnx.cursor()
            add_profile = ("INSERT INTO profile (uid,username, password, name, gender, post, city, email, phone, type) VALUES ('99912345','login2','pass3','name3','1','0','0','test3@test3','123456','0') ")

            #data_profile = ('login2','pass3','name3','1','0','0','test3@test3','123456','0')
            #cursor.execute(add_profile, data_profile)
            cursor.execute(add_profile)
            cnx.commit()
            
            
