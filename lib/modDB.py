from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

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
        cursor.close()
         

def login_query(cnx,fbID):
        """ this function needs a cnx connector to a database, and a facebook ID
        to check if the user is registered or not"""
        cursor1 = cnx.cursor()
        query1 = ("SELECT count(*) FROM profile where uid=" + str(fbID) + ";")
        cursor1.execute(query1)
        resultado = cursor1.fetchall()
       
        cursor1.close()
        return resultado

def request_query(cnx,city):
        """ this function needs a cnx connector to a database, and
        the name of a City. It returns a tuple with all request for help from seekers, and another info.
        This query is usually used by helpers"""
        
        cursor1 = cnx.cursor()
        query1 = ("SELECT profile.name, new_need.task_dt, gender.gender, city.city FROM new_need "
                  "JOIN city JOIN profile JOIN gender ON city.city='" + city + "' AND gender.uid=new_need.gender "
                  "AND city.uid=new_need.city AND profile.uid=new_need.uid ORDER BY new_need.task_dt desc;")
        cursor1.execute(query1)
        resultado = cursor1.fetchall()
        cursor1.close()
        return resultado

def offers_query(cnx,city):
        """ this function needs a cnx connector to a database, and
        the name of a City. It returns a tuple with all offers from helpers, and another info.
        This query is usually used by seekers"""

        cursor1 = cnx.cursor()
        query1 = ("SELECT profile.name, time_av.from_dt, time_av.to_dt, city.city FROM time_av JOIN city JOIN profile ON city.city='" + city + "' AND city.uid=time_av.city and profile.uid=time_av.uid;")
        cursor1.execute(query1)
        resultado = cursor1.fetchall()
        cursor1.close()
        return resultado



################ 
def post_need(cnx,uid,date,city,gender,place,comment):
        """ this function needs a cnx connector to a database, and an array with the info to save in the database.
        This query is usually used by seekers"""
        dateformated = datetime.datetime(2016,02,28)
        cursor1 = cnx.cursor()
        #query1 = ("INSERT INTO new_need (gender,city,uid,task_dt,place,comment) values "
        #          "((select uid from gender where gender='" + gender+ "'),"
        #          "(select uid from city where city='" + city + "')," +str(uid)+",'" + dateformated +"', "
        #          "(select id from places where place='" + place + "'), '" +comment+ "');")
        #cursor1.execute(query1)

        cursor1.execute("INSERT INTO new_need (gender,city,uid,task_dt,place,comment) values "
                  "((select uid from gender where gender='%s'),"
                        "(select uid from city where city='%s'), %s, %s, (select id from places where place= %s),%s)",(gender,city,uid,dateformated,place,comment))

        resultado = cnx.commit()
        cursor1.close()
        return resultado



###############
def post_help(cnx,uid,from_dt,to_dt,city,comment):
        """ this function needs a cnx connector to a database, and an array with the info to save in the database.
        This query is usually used by helpers, to post their availability"""
        from_dateformated = '2016-02-29 00:00:00.0'
        to_dateformated = '2016-03-1 23:00:00.0'
        cursor1 = cnx.cursor()
        query1 = ("INSERT INTO time_av (city,uid,from_dt,to_dt,comment) values "
                  "((select uid from city where city='" + city + "')," +str(uid)+",'" + from_dateformated +"','" +to_dateformated +"',"
                  "'" +comment+ "');")



        cursor1.execute(query1)
        resultado = cnx.commit()
        cursor1.close()
        return resultado

