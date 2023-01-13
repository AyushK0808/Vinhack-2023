import mysql.connector as ms
import urllib3
import requests


base = ms.connect(user='root', password='euroschool',host='localhost', database='HACKATHON')
cursor = base.cursor(buffered=True)   # Pointer


# All functions
def new_reg(l1):
    query = ("UPDATE MAIN"
             "SET NAME = %s, GENDER = %s, PHONE_NO = %s "
             "WHERE REG_NO = %s ")
    cursor.execute(query, (l1[1], l1[2], l1[3], l1[0]))
def update_reg(l1):
    query = ("INSERT INTO MAIN VALUES"
             "(%s, %s, %s, %s )")
    cursor.execute(query, (l1[0], l1[1], l1[2], l1[3]))
def check_slots(l1):
    query = ("SELECT COUNT(*) FROM MAIN "
             "WHERE REG_NO = %s")
    a = cursor.execute(query, (l1[0]))
    if a is None:
        pass


# Putting results into a list
result = cursor.fetchall()  # Fetch data from HTML table
credentials = []
for row in result:
    a = "%s" % row[0]
    credentials.append(a)
    b = "%s" % row[1]
    credentials.append(b)
    c = "%s" % row[2]
    credentials.append(c)
    d = "%s" % row[3]
    credentials.append(d)
contents = " "
filename = 'Sports_Registration.html'
def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

# End of MySQL link with Python
for i in cursor:
    print(i)
base.commit()
cursor.close()
base.close()
