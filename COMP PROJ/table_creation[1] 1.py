import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='mysql',database='studentt')
if conn.is_connected():
      print('successfully connected')
c1=conn.cursor()

c1.execute('create table driver_details(d_ID varchar(5) primary key,d_name varchar(25) ,d_age int(3),d_route varchar(4),d_phono bigint)')
c1.execute('create table student_details(admno varchar(8) primary key,s_name varchar(25),s_class varchar(10),s_route varchar(4) ,s_phono bigint)')
c1.execute('create table worker_details(w_ID varchar(5) primary key,w_name varchar(25) ,w_age int,w_workname varchar(40),w_phono bigint)')
print('table created')

print("Enter 1, to add student details \n Enter 2, to add driver details \n Enter 3, to add worker details")
choice=int(input("ENTER YOUR CHOICE:"))

if choice==1:
  s_name=input('Enter Student Name:')
  s_rollno=int(input('Enter roll no:'))
  s_class=input('Enter Class:')
  s_route=input('Enter Route no:')
  s_phono=int(input('Enter Phone number of gaurdian:'))
  sql_insert="insert into student_details values('{}',{},'{}','{}',{})".format(s_name, s_rollno, s_class,s_route, s_phono)
  c1.execute(sql_insert)
  print('SUCCESSFULLY REGISTERED')
  conn.commit()  

if choice==2:
  d_name=input('Enter Driver Name:')
  d_age=int(input('Enter Age:'))
  d_route=input('Enter the Route no:')
  d_phono=int(input('Enter Phone number:'))
  sql_insert="insert into driver_details values('{}',{},'{}',{})".format(d_name, d_age, d_route, d_phono)
  c1.execute(sql_insert)
  print('ok')
  conn.commit()
          
if choice==3:
  w_name=input('Enter Worker Name:')
  w_age=int(input('Enter Age:'))
  w_workname=input('Enter type of work:')
  w_phono=int(input('Enter Phone number:'))
  sql_insert="insert into worker_details values('{}',{},'{}',{})".format(w_name, w_age, w_workname, w_phono)
  c1.execute(sql_insert)
  print('ok')
  conn.commit()                  
