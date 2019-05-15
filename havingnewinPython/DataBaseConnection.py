import pymysql
host='localhost'
usename='root'
password=''
databasename='test'

conn=pymysql.connect(host,usename,password,databasename)

execute=conn.cursor()

if execute:
    print('database connection succesfull')
else:
    print('OPPS!!!!!database is not connection succesfull')