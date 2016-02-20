from modDB import *

cnx = opendb()
resultado = login_query(cnx,3)
print resultado
closedb(cnx)


