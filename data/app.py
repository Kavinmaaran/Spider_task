from flask import Flask,render_template, request,redirect
import os
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        try:
            app.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
            app.config['MYSQL_USER'] = 'sql6510938'
            app.config['MYSQL_PASSWORD'] = 'Ba2uihS6UE'
            app.config['MYSQL_DB'] = 'sql6510938'
            mysql = MySQL(app)
            name = request.form['name']
            dept = request.form['dept']
            email = request.form['email']
            rollno = request.form['rollno']
            cursor = mysql.connection.cursor()
            cursor.execute('''INSERT INTO `form_details` (`name`, `dept`, `email`, `rollno`)
                            VALUES (%s, %s, %s, %s);''',(name,dept,email,rollno))
            mysql.connection.commit()
            cursor.close()
            return redirect("https://spider987.herokuapp.com/success")
        except:
            cursor.close()
            return redirect("https://spider987.herokuapp.com/unsuccess")

@app.route('/success', methods = ['POST', 'GET'])
def search():
    return render_template('success.html')

@app.route('/unsuccess', methods = ['POST', 'GET'])
def callback():
    return render_template('unsuccess.html')

@app.route('/table')
def table():
    app.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
    app.config['MYSQL_USER'] = 'sql6510938'
    app.config['MYSQL_PASSWORD'] = 'Ba2uihS6UE'
    app.config['MYSQL_DB'] = 'sql6510938'
    mysql = MySQL(app)
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM from_details")
    data = cursor.fetchall()
    return render_template('table.html', data=data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
 
 