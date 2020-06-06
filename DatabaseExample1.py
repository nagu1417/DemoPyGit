
import  mysql.connector;

mydb=mysql.connector.connect(host="localhost",user="nagesh",passwd="1234",database="employeeinfo")

mycursor=mydb.cursor();
mycursor.execute("select * from employee")
for i in mycursor:
    print(i)
