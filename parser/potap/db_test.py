import psycopg2

con = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="",
    host="127.0.0.1",
    port="5432"
)

print("Database opened successfully")


# cur = con.cursor()
# cur.execute("DELETE from STUDENT where ADMISSION=3420;")
# con.commit()
#
# print("Total deleted rows:", cur.rowcount)
# cur.execute("SELECT admission, name, age, course, department from STUDENT")
#
# rows = cur.fetchall()
# for row in rows:
#     print("ADMISSION =", row[0])
#     print("NAME =", row[1])
#     print("AGE =", row[2])
#     print("COURSE =", row[3])
#     print("DEPARTMENT =", row[4], "\n")
#
# print("Deletion successful")
# con.close()

# cur = con.cursor()
# cur.execute("UPDATE STUDENT set AGE = 20 where ADMISSION = 3420")
# con.commit()
#
# print("Total updated rows:", cur.rowcount)
# cur.execute("SELECT admission, age, name, course, department from STUDENT")
#
# rows = cur.fetchall()
# for row in rows:
#     print("ADMISSION =", row[0])
#     print("NAME =", row[1])
#     print("AGE =", row[2])
#     print("COURSE =", row[2])
#     print("DEPARTMENT =", row[3], "\n")
#
# print("Operation done successfully")
# con.close()

# cur = con.cursor()
# cur.execute("SELECT admission, name, age, course, department from STUDENT")
#
# rows = cur.fetchall()
# for row in rows:
#     print("ADMISSION =", row[0])
#     print("NAME =", row[1])
#     print("AGE =", row[2])
#     print("COURSE =", row[3])
#     print("DEPARTMENT =", row[4], "\n")
#
# print("Operation done successfully")
# con.close()

# cur = con.cursor()
# cur.execute(
#     "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3419, 'Abel', 17, 'Computer Science', 'ICT')"
# )
# cur.execute(
#     "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3421, 'Joel', 17, 'Computer Science', 'ICT')"
# )
# cur.execute(
#     "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3422, 'Antony', 19, 'Electrical Engineering', 'Engineering')"
# )
# cur.execute(
#     "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3423, 'Alice', 18, 'Information Technology', 'ICT')"
# )
#
# con.commit()
# print("Records inserted successfully")
#
# con.close()

cur = con.cursor()
cur.execute('''CREATE TABLE Sites
     (ADMISSION INT PRIMARY KEY NOT NULL,
     NAME TEXT NOT NULL,
     AGE INT NOT NULL,
     COURSE CHAR(50),
     DEPARTMENT CHAR(50));''')

print("Table created successfully")
con.commit()
con.close()

# cur = con.cursor()
# cur.execute(
#     "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')"
# )
#
# con.commit()
# print("Record inserted successfully")
#
# con.close()
