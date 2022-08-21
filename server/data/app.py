from flask import Flask,render_template, request
import os
from flask_mysqldb import MySQL
import hashlib

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'example'
app.config['MYSQL_DB'] = 'form'

mysql = MySQL(app)

# @app.route('/', methods = ['POST', 'GET'])
# def home():
#     if request.method == 'GET':
#         return render_template('index.html')
#     if request.method == 'POST':
#         try:
#             name = request.form['name']
#             dept = request.form['dept']
#             email = request.form['email']
#             rollno = request.form['rollno']
#             cursor = mysql.connection.cursor()
#             cursor.execute('''INSERT INTO `form_details` (`name`, `dept`, `email`, `rollno`)
#                             VALUES (%s, %s, %s, %s);''',(name,dept,email,rollno))
#             mysql.connection.commit()
#             cursor.close()
#             return render_template('success.html')
#         except:
#             cursor.close()
#             return render_template('unsuccess.html')

# @app.route('/success', methods = ['POST', 'GET'])
# def search():
#     return render_template('success.html')

@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    if request.method == 'POST':
        try:
            email = request.form['usr_email']
            passwd = request.form['passwd']
            name = request.form['username']
            phone = request.form['phone']
            password = hashlib.md5(passwd.encode())
            password=password.hexdigest()
            cursor = mysql.connection.cursor()
            cursor.execute('''INSERT INTO `signup` (`username`, `password`, `email`, `phone`)
                            VALUES (%s, %s, %s, %s);''',(name,password,email,phone))
            mysql.connection.commit()
            cursor.close()
            return render_template('login.html')
        except:
            cursor.close()
            return render_template('unsuccess.html')
# @app.route('/unsuccess', methods = ['POST', 'GET'])
# def callback():
#     return render_template('unsuccess.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        # name = request.form['username']
        # passwd = request.form['password']
        try:
            name = request.form['username']
            passwd = request.form['password']
            password = hashlib.md5(passwd.encode())
            password=password.hexdigest()
            cursor = mysql.connection.cursor()
            cursor.execute('''SELECT `password` FROM signup WHERE `username` = %s ;''',(name,))
            data = cursor.fetchall()
            mysql.connection.commit()
            cursor.close()
            if (data[0][0]==password):    
                return render_template('index.html', data=name)
            else:
                return render_template('login.html')
        except:
            cursor.close()
            return render_template('unsuccess.html')    

# @app.route('/viewResponse', methods = ['POST', 'GET'])
# def viewResponse():
#     if request.method == 'GET':
#         return render_template('viewResponse.html')
#     if request.method == 'POST':
#         try:
#             email = request.form['email']
#             cursor = mysql.connection.cursor()
#             cursor.execute('''SELECT `name`,`dept`,`rollno` FROM `form_details` WHERE `email` = %s ;''',(email,))
#             data = cursor.fetchall()
#             data = list(data)
#             data.insert(0,["Name","Department","Roll No."])
#             mysql.connection.commit()
#             cursor.close()
#             return render_template('table.html', data=data)
#         except:
#             cursor.close()
#             return render_template('unsuccess.html')

# @app.route('/table')
# def table():
#     cursor = mysql.connection.cursor()
#     cursor.execute('''SELECT `name`,`dept`,`rollno` FROM form_details''')
#     data = cursor.fetchall()
#     data = list(data)
#     data.insert(0,["Name","Department","Roll No."])
#     cursor.close()
#     return render_template('table.html', data=data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)