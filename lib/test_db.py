from modDB import *

cnx = opendb()
resultado = offers_query(cnx,'Osnabrueck')
for i in resultado:
    print i[1]

#print resultado
closedb(cnx)



