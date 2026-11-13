from sys import exit 
import mysql.connector 
conn= mysql.connector.connect(host='localhost',user='root',passwd='mysql',database='studentt')
if conn.is_connected():
  print('successfully connected')
c1=conn.cursor()
print('---------------------------------------------')
print("SCHOOL BUS MANAGEMENT SYSTEM")
print('---------------------------------------------')
print('"TRAVELLING IS A BLISS"')
print("1.LOGIN")
print("2.EXIT")
choice=int(input("ENTER YOUR CHOICE:"))
if choice==1:
  u1=input("enter user name:")
  pwd1=input("enter the password:")
  while u1=='abc'and pwd1=='abc':
    print('connected')
  
    print("WELCOME TO BUSES")
    print("successfully connected")
    print('1.Registering students details')
    print('2.Registering bus driver details')
    print('3.Registering workers details')
    print("4.Displaying total student details(of a particular bus route)")
    print("5.Displaying total bus driver details")
    print("6.Displaying total worker details")
    print('7.Search Students detail')
    print('8.Search Bus driver detail')
    print('9.Search Worker detail')
    print('10.Exit')
    choice=int(input('ENTER YOUR CHOICE:'))
    if choice==1:
      admno=input('Enter Admission number: ')
      s_name=input('Enter Student Name: ')
      s_class=input('Enter Class: ')
      s_route=input('Enter Route no: ')
      s_phono=int(input('Enter Phone number of guardian: '))
      if len(str(s_phono))==10:
        sql_insert="insert into student_details values('{}','{}','{}','{}',{})".format(admno,s_name, s_class,s_route, s_phono)
        c1.execute(sql_insert)
        print('SUCCESSFULLY REGISTERED')
        conn.commit()
      else:
        print("NOT REGISTERED STUDENT DETAILS SINCE THE PHONE NO. IS INVALID!")
      
    elif choice==2:
      d_ID=input('Enter driver employee ID: ')
      d_name=input('Enter Driver Name: ')
      d_age=int(input('Enter age: '))
      d_route=input('Enter the Route no: ')
      d_phono=int(input('Enter Phone number: '))
      if len(str(d_phono))==10:
        sql_insert="insert into driver_details values('{}','{}',{},'{}',{})".format(d_ID,d_name, d_age, d_route, d_phono)
        c1.execute(sql_insert)
        print('SUCCESSFULLY REGISTERED!')
        conn.commit()
      else:
        print("NOT REGISTERED DRIVER DETAILS SINCE THE PHONE NUMBER ENTERED IS INVALID!")
      
    elif choice==3:
      w_ID=input('Enter Worker Employee ID: ')
      w_name=input('Enter Worker Name: ')
      w_age=int(input('Enter Age: '))
      w_workname=input('Enter type of work(fees, conductor): ')
      w_phono=int(input('Enter Phone number: '))
      if w_workname.upper() in ('FEES', 'CONDUCTOR') and len(str(w_phono))==10:
        sql_insert="insert into worker_details values('{}','{}',{},'{}',{})".format(w_ID,w_name, w_age, w_workname, w_phono)
        c1.execute(sql_insert)
        print('SUCCESSFULLY REGISTERED!')
        conn.commit()
      else:
        print("NOT REGISTERED WORKER DETAIL SINCE WORK/PHONE NO. IS NOT VALID!")
      
    elif choice==4:
      r=input('Enter bus route number: ')
      sql_w="select * from student_details where s_route='{}'".format(r)
      c1.execute(sql_w)
      r = c1.fetchall()
      print("ADMNO.\t NAME \t CLASS \t PHONENO.")
      for i in r :
        print(i[0],'\t', i[1],'\t', i[2],'\t', i[4])
        
    elif choice==5:
      sql_x="select*from driver_details"
      c1.execute(sql_x)
      s=c1.fetchall()
      print("D_ID \t NAME \t AGE \t ROUTE \t PHONENO.")
      for i in s:
        print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4])
        
    elif choice==6:
      sql_y="select*from worker_details"
      c1.execute(sql_y)
      t=c1.fetchall()
      print("W_ID \t NAME \t AGE \t WORK \t PHONENO.")
      for i in t:
        print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4])
        
    elif choice==7:
      h=input("Enter the admno. : ")
      sql_w='select*from student_details where admno=("{}")'.format(h)
      c1.execute(sql_w)
      u = c1.fetchall()
      if u != []:
        print("STUDENT FOUND!")
        print("ADMNO.\t NAME \t CLASS \t ROUTE \t PHONENO.")
        for i in u:
          print(i[0],'\t', i[1],'\t', i[2],'\t',i[3],'\t', i[4])
      else:
        print("STUDENT NOT FOUND!")
        
    elif choice==8:
      d=input("Enter the driver ID: ")
      sql_d='select*from driver_details where d_ID=("{}")'.format(d)
      c1.execute(sql_d)
      v=c1.fetchall()
      if v != []:
        print("DRIVER FOUND!")
        print("D_ID \t NAME \t AGE \t ROUTE \t PHONENO.")
        for i in v:
          print(i[0],'\t', i[1],'\t', i[2],'\t',i[3],'\t', i[4])
      else:
        print("DRIVER NOT FOUND!")
        
    elif choice==9:
      f=input("Enter the Worker ID : ")
      sql_f='select*from worker_details where w_ID=("{}")'.format(f)
      c1.execute(sql_f)
      w=c1.fetchall()
      if w!=[]:
        print("WORKER FOUND!")
        print("W_ID \t NAME \t AGE \t WORK \t PHONENO.")
        for i in w:
          print(i[0],'\t', i[1],'\t', i[2],'\t',i[3],'\t', i[4])
      else:
        print("WORKER NOT FOUND!")
    elif choice==10:
      exit()
      break
    else:
      print("Invalid choice!")
    
  else:
    print('wrong username & password')
if choice==2:
  exit()
