import csv
# import pypyodbc as odbc
# import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="1230", database="csv")
mycurser = mydb.cursor()

with open(r'C:\Users\rgak2\Downloads\book (1).csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
# ============= state = TN =order= name,pan,state,dob,income,tax,fnyear == 0,1,3,4,5,6,2
        if(line[2]=="TN"):
            print(line)
            sql = "insert into new_table(name, pan, dob, income, tax, fnyear, state)values('{}','{}','{}','{}','{}','{}','{}')".format(line[0], line[1], line[3], line[4], line[5], line[6] ,line[2])
            mycurser.execute(sql)
            mydb.commit()
# ============= state = AP =order= pan,state,name,fnyear,dob,income,tax == 2,0,4,5,6,3,1
        if(line[1]=="AP"):
            print(line)
            sql = "insert into new_table(name, pan, dob, income, tax, fnyear, state)values('{}','{}','{}','{}','{}','{}','{}')".format(line[2], line[0], line[4], line[5], line[6], line[3], line[1])
            mycurser.execute(sql)
            mydb.commit()
# ============= state = MH =order= state,dob,fnyear,income,tax,name,pan == 5,6,1,3,4,2,0
        if (line[0] == "MH"):
            print(line)
            sql = "insert into new_table(name, pan, dob, income, tax, fnyear, state)values('{}','{}','{}','{}','{}','{}','{}')".format(line[5], line[6], line[1], line[3], line[4], line[2], line[0])
            mycurser.execute(sql)
            mydb.commit()
# ============= state = HP =order= income,tax,fnyear,dob,name,pan,state == 4,5,3,0,1,2,6
        if (line[6] == "HP"):
            print(line)
            sql = "insert into new_table(name, pan, dob, income, tax, fnyear, state)values('{}','{}','{}','{}','{}','{}','{}')".format(line[4], line[5], line[3], line[0], line[1], line[2], line[6])
            mycurser.execute(sql)
            mydb.commit()
# ============= state = UP =order= dob,fnyear,pan,state,income,tax,name == 6,2,0,4,5,1,3
        if (line[3] == "UP"):
            print(line)
            sql = "insert into new_table(name, pan, dob, income, tax, fnyear, state)values('{}','{}','{}','{}','{}','{}','{}')".format(line[6], line[2], line[0], line[4], line[5], line[1], line[3])
            mycurser.execute(sql)
            mydb.commit()

