import psycopg2
from datetime import datetime
import pytz # $ pip install pytz

def create_tables():


    cur.execute('''CREATE TABLE LOGINS
          (id           SERIAL PRIMARY KEY ,
          ip      VARCHAR ( 255 )   ,
          created_on     VARCHAR ( 100 )   ,
          city      VARCHAR ( 255 )   ,
          region         VARCHAR ( 255 )   ,
          country        VARCHAR ( 255 )   ,
          timezone         VARCHAR ( 100 ))  ;''')

    cur.execute('''CREATE TABLE STUDENT
          (id           SERIAL PRIMARY KEY     NOT NULL,
          name           VARCHAR ( 255 )     NOT NULL,
          login        SERIAL REFERENCES LOGINS (id),
          email          VARCHAR ( 255 )     NOT NULL,
          created_on     VARCHAR ( 100 )           NOT NULL,
          send_email      VARCHAR ( 1 )        NOT NULL
          );''')

    cur.execute('''CREATE TABLE COURSE
          (id               SERIAL PRIMARY KEY     NOT NULL,
          course_title      VARCHAR ( 255 )     NOT NULL,
          days              VARCHAR ( 255 )     NOT NULL,
          dates             VARCHAR ( 255 )     NOT NULL,
          class_time        VARCHAR ( 255 )     NOT NULL,
          created_on        VARCHAR ( 100 )           NOT NULL,
          price             INT                 NOT NULL,
          seats_available   INT                 NOT NULL,
          zoom_link         VARCHAR ( 255 )             ,
          ages              VARCHAR ( 255 )     NOT NULL,
          display           VARCHAR ( 1 )      NOT NULL,
          section           INT                NOT NULL);''')
          # class size
          # course session length

    cur.execute('''CREATE TABLE COURSETOSTUDENT
          (id               SERIAL PRIMARY KEY     NOT NULL,
          course            SERIAL REFERENCES COURSE (id),
          student           SERIAL REFERENCES STUDENT (id),
          seat_number        INT                 NOT NULL,
          created_on        VARCHAR ( 100 )           NOT NULL,
          amount_payed      INT           NOT NULL,
          amount_refunded     INT           ,
          refunded          VARCHAR ( 1 )       NOT NULL,
          refund_requested  VARCHAR ( 1 )          NOT NULL,
          confirmation_code  VARCHAR ( 17 )     NOT NULL);''')
    print ("Table created successfully\n")
    conn.commit()


def drop_tables():
        cur.execute('''DROP TABLE IF EXISTS COURSETOSTUDENT;''')
        cur.execute('''DROP TABLE IF EXISTS COURSE;''')
        cur.execute('''DROP TABLE IF EXISTS STUDENT;''')
        cur.execute('''DROP TABLE IF EXISTS LOGINS;''')
        print ("All Tables deleted \n")
        conn.commit()

def create_login(obj = None, cur = None,conn = None ):
     """
     id           SERIAL PRIMARY KEY,
     ip      VARCHAR ( 255 ),
     created_on     VARCHAR ( 100 ),
     region         VARCHAR ( 255 ),
     country        VARCHAR ( 255 ),
     timezone         VARCHAR ( 50 ))

     """
     if obj == None:
         obj = {
         "ip" : "me",
         "created_on": datetime.now(pytz.timezone("America/New_York")) ,
         "city": "phx",
         "region": "Az",
         "country": "USA",
         "timezone": "East/Coast"

         }
     obj["created_on"] = datetime.now(pytz.timezone("America/New_York"))

     insert_statement = f'INSERT INTO LOGINS ( ip, created_on, region, country, timezone, city) VALUES \
      ( \'{obj["ip"]}\',\'{obj["created_on"]}\',\'{obj["region"]}\',\'{obj["country"]}\',\'{obj["timezone"]}\',\'{obj["city"]}\')  RETURNING id;'
     print("\nstatment: ",insert_statement, '\n')
     cur.execute(insert_statement)
     id = cur.fetchone()[0]
     conn.commit()
     display_table_data('logins', '\nTable Logins \nid | ip | created_on | region | country | timezone, city \n', cur)
     return id

def create_student(obj = None, cur = None,conn = None):
     """
      id           SERIAL PRIMARY KEY     NOT NULL,
      name           VARCHAR ( 255 )     NOT NULL,
      login        SERIAL REFERENCES LOGINS (id),
      email          VARCHAR ( 255 )     NOT NULL,
      created_on     VARCHAR ( 100 )           NOT NULL)
      send_email      VARCHAR ( 1 )        NOT NULL,

     """
     if obj == None:
         obj = {
         "name" : "Gabriel Ogbonnaya",
         "created_on": datetime.now(pytz.timezone("America/New_York")) ,
         "email": "ogbonnaya83512@gmail.com",
         "login": 1,
         "send_email": 't'
         }


     obj["created_on"] = datetime.now(pytz.timezone("America/New_York"))
     insert_statement = f'INSERT INTO STUDENT ( name, login, email, created_on,send_email) VALUES \
      ( \'{obj["name"]}\',{obj["login"]},\'{obj["email"]}\',\'{obj["created_on"]}\',\'{obj["send_email"]}\') RETURNING id;'
     print("\nstatment: ",insert_statement, '\n')
     cur.execute(insert_statement)
     id = cur.fetchone()[0]
     conn.commit()
     display_table_data('STUDENT', '\nTable STUDENT \nname | login | region | email | created_on \n',cur)
     return id


def create_course(obj = None):
     """
      id               SERIAL PRIMARY KEY     NOT NULL,
      course_title      VARCHAR ( 255 )     NOT NULL,
      days              VARCHAR ( 255 )     NOT NULL,
      dates             VARCHAR ( 255 )     NOT NULL,
      class_time        VARCHAR ( 255 )     NOT NULL,
      created_on        VARCHAR ( 100 )           NOT NULL,
      price             INT                 NOT NULL,
      seats_available   INT                 NOT NULL,
      zoom_link         VARCHAR ( 255 )             ,
      ages              VARCHAR ( 50 )     NOT NULL),
      display           VARCHAR ( 1 )      NOT NULL,
      section           INT                NOT NULL

     """
     if obj == None:
         obj = {
         "course_title" : "Intro to Python",
         "days" : "M W F",
         "dates" : "12/16/2024 - 12/30/2024",
         "class_time" : "2:30 - 3:30pm EST",
         "created_on": datetime.now(pytz.timezone("America/New_York")) ,
         "price": 200,
         "seats_available": 12,
         "zoom_link": "google.com",
         "ages": "18+",
         "display": "t",
         "section": 1,
         }
     insert_statement = f'INSERT INTO COURSE ( course_title, days, dates, class_time, created_on, price, seats_available, zoom_link, ages, display, section) VALUES \
      ( \'{obj["course_title"]}\', \'{obj["days"]}\', \'{obj["dates"]}\', \'{obj["class_time"]}\', \'{obj["created_on"]}\', {obj["price"]}, {obj["seats_available"]}, \'{obj["zoom_link"]}\', \'{obj["ages"]}\',\'{obj["display"]}\',{obj["section"]});'
     cur.execute(insert_statement)
     conn.commit()

     print("\nstatment: ",insert_statement, '\n')
     display_table_data('COURSE', '\nCOURSE \ncourse_title| days | dates | class_time | created_on | price | seats_available | zoom_link | ages | display | section \n',cur)


def create_course_student(obj = None, cur = None,conn = None):
     """
      id               SERIAL PRIMARY KEY     NOT NULL,
      course            SERIAL REFERENCES COURSE (id),
      student           SERIAL REFERENCES STUDENT (id),
      seat_number        INT                 NOT NULL,
      created_on        VARCHAR ( 100 )           NOT NULL,
      amount_payed          INT           NOT NULL,
      amount_refunded      INT           ,
      refunded          VARCHAR ( 1 )       NOT NULL,
      refund_requested  VARCHAR ( 1 )          NOT NULL,
      confirmation_code  VARCHAR ( 14 )     NOT NULL);'''

     """
     if obj == None:
         obj = {
         "course" : 1,
         "student" : 1,
         "seat_number" : 2,
         "created_on": datetime.now(pytz.timezone("America/New_York")) ,
         "amount_payed" : 200,
         "amount_refunded" : 0,
         "refunded": 'f',
         "refund_requested": 'f',
         "confirmation_code": "Phostrino22",
         }
     obj["created_on"] = datetime.now(pytz.timezone("America/New_York"))
     insert_statement = f'INSERT INTO COURSETOSTUDENT (course, student, seat_number, created_on, amount_payed, amount_refunded, refunded, refund_requested, confirmation_code) VALUES \
      ({obj["course"]},{obj["student"]},{obj["seat_number"]},\'{obj["created_on"]}\',{obj["amount_payed"]},{obj["amount_refunded"]},\'{obj["refunded"]}\',\'{obj["refund_requested"]}\',\'{obj["confirmation_code"]}\') RETURNING id;;'
     print("\nstatment: ",insert_statement, '\n')
     cur.execute(insert_statement)
     id = cur.fetchone()[0]
     conn.commit()
     display_table_data('COURSETOSTUDENT', '\COURSETOSTUDENT \ncourse| student | seat_number | created_on | amount_payed | amount_refunded | refunded | refund_requested | confirmation_code  \n',cur)
     return id

def display_table_data(table_name,values,cur = None):
    cur.execute(f"SELECT *  from {table_name}")
    rows = cur.fetchall()
    print(values)
    for row in rows:
        print(row)
    print('\n')

def get_student_login():
    print("\nStudent Login Join\n")
    cur.execute(f"SELECT *  from student left join logins on student.login = logins.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print('\n')

def get_courses(title, cur):
    courses = []
    cur.execute(f"SELECT course_title,days,dates,class_time,created_on,price,seats_available,zoom_link,ages,id  from COURSE where course_title = '{title}' and display = 't' and seats_available > 0 ORDER BY id ASC ")
    rows = cur.fetchall()
    for row in rows:

        obj = {}
        obj["course_title"] = row[0]
        obj["days"] = row[1]
        obj["dates"] = row[2]
        obj["class_time"] = row[3]
        obj["created_on"] = row[4]
        obj["price"] = row[5]
        obj["seats_available"] = row[6]
        obj["zoom_link"] = row[7]
        obj["ages"] = row[8]
        obj["id"] = row[9]
        courses.append(obj)

    return courses

def subtract_seat(course_id, cur = None,conn = None):
    cur.execute(f"SELECT course_title,days,dates,class_time,created_on,price,seats_available,zoom_link,ages,id  from COURSE where id = '{course_id}' ")
    rows = cur.fetchall()

    for row in rows:
        course = row
    student_seat = course[6]
    cur.execute(f"UPDATE COURSE SET seats_available = {student_seat - 1} WHERE id = {course_id};")
    conn.commit()
    return student_seat

def unsubscribe(obj = None, cur = None,conn = None):
    cur.execute( f"""UPDATE STUDENT SET send_email = 'f' WHERE id = { obj["student_id"] } """);
    conn.commit()


def batch_create_courses():
    courses_to_create = [
              {
             "course_title" : "Intro to Python",
             "days" : "M W F",
             "dates" : "08/22/2022-09/12/2022",
             "class_time" : "5:30-6:30pm EST",
             "created_on": datetime.now(pytz.timezone("America/New_York")) ,
             "price": 200,
             "seats_available": 12,
             "zoom_link": "google.com",
             "ages": "14-17",
             "display": "t",
             "section": 1
             },
              {
              "course_title" : "Intro to Python",
              "days" : "M W F",
              "dates" : "08/22/2022-09/12/2022",
              "class_time" : "6:40-7:40pm EST",
              "created_on": datetime.now(pytz.timezone("America/New_York")) ,
              "price": 200,
              "seats_available": 12,
              "zoom_link": "google.com",
              "ages": "18+",
              "display": "t",
              "section": 1
              },

            {
            "course_title" : "Intro to Python",
            "days" : "M W F",
            "dates" : "08/22/2022-09/12/2022",
            "class_time" : "7:50-8:50pm EST",
            "created_on": datetime.now(pytz.timezone("America/New_York")) ,
            "price": 200,
            "seats_available": 12,
            "zoom_link": "google.com",
            "ages": "18+",
            "display": "t",
            "section": 1
            },

            {
            "course_title" : "Intro to Python",
            "days" : "T Th Sat",
            "dates" : "08/23/2022-09/13/2022",
            "class_time" : "5:30-6:30pm EST",
            "created_on": datetime.now(pytz.timezone("America/New_York")) ,
            "price": 200,
            "seats_available": 12,
            "zoom_link": "google.com",
            "ages": "14-17",
            "display": "t",
            "section": 1
            },

            {
            "course_title" : "Intro to Python",
            "days" : "T Th Sat",
            "dates" : "08/23/2022-09/13/2022",
            "class_time" : "6:40-7:40pm EST",
            "created_on": datetime.now(pytz.timezone("America/New_York")) ,
            "price": 200,
            "seats_available": 12,
            "zoom_link": "google.com",
            "ages": "18+",
            "display": "t",
            "section": 1
            },


            {
            "course_title" : "Intro to Python",
            "days" : "T Th Sat",
            "dates" : "08/23/2022-09/13/2022",
            "class_time" : "7:50-8:50pm EST",
            "created_on": datetime.now(pytz.timezone("America/New_York")) ,
            "price": 200,
            "seats_available": 12,
            "zoom_link": "google.com",
            "ages": "18+",
            "display": "t",
            "section": 1
            }
    ]

    for instance in courses_to_create:
        create_course(instance)




if __name__ == "__main__":
    conn = psycopg2.connect(database = "mydb",  host = "127.0.0.1", port = "5432")
    print("\nOpened database successfully \n")
    cur = conn.cursor()
    drop_tables()
    create_tables()

    # create_login(cur=cur, conn=conn)
    # create_student()
    # left join
    # get_student_login()
    # create_course()
    batch_create_courses()
    # create_course_student()
    conn.close()
