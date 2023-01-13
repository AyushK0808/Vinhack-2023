import mysql.connector as ms
import flask as f
from flask import redirect, render_template
import requests

base = ms.connect(user='root', password='euroschool',host='localhost', database='HACKATHON')
cursor = base.cursor(buffered=True)   # Pointer

x = requests.get("http://localhost:63342/Vinhack-2023/FINAL/login%20att3.html")
data = x.json
print(data)

# Flask routes
app = f.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    from flask import request
    if request.method == 'POST':
        # get the login details from the form
        login_user = request.form['loginUser']
        login_password = request.form['loginPassword']

        # Check the login details against the database
        # Connect to MySQL and verify the user
        # If the user is verified, redirect to the home page
        return redirect('/home')
    return render_template('login.html')
print(login())
@app.route('/register', methods=['POST'])
def register():
    reg_no = f.request.form['reg_no']
    name = f.request.form['name']
    gender = f.request.form['gender']
    phone_no = f.request.form['phone_no']
    l1 = [reg_no, name, gender, phone_no]
    update_reg(l1)
    base.commit()
    return 'Successfully registered!'

@app.route('/update', methods=['POST'])
def update():
    reg_no = f.request.form['reg_no']
    name = f.request.form['name']
    gender = f.request.form['gender']
    phone_no = f.request.form['phone_no']
    l1 = [reg_no, name, gender, phone_no]
    new_reg(l1)
    base.commit()
    return 'Successfully updated!'

@app.route('/check', methods=['POST'])
def check():
    reg_no = f.request.form['reg_no']
    l1 = [reg_no]
    slots = check_slots(l1)
    if slots > 0:
        return 'Slots available!'
    else:
        return 'No slots available!'

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


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)

# End of MySQL link with Python
cursor.close()
base.close()
