from flask import Flask,render_template, request
import os
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'sql6.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql6510938'
app.config['MYSQL_PASSWORD'] = 'Ba2uihS6UE'
app.config['MYSQL_DB'] = 'sql6510938'
 
mysql = MySQL(app)


@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        try:
            name = request.form['name']
            dept = request.form['dept']
            email = request.form['email']
            rollno = request.form['rollno']
            cursor = mysql.connection.cursor()
            cursor.execute('''INSERT INTO `form_details` (`name`, `dept`, `email`, `rollno`)
                            VALUES (%s, %s, %s, %s);''',(name,dept,email,rollno))
            mysql.connection.commit()
            cursor.close()
            return render_template('success.html')
        except:
            cursor.close()
            return render_template('unsuccess.html')

@app.route('/success', methods = ['POST', 'GET'])
def search():
    return render_template('success.html')

@app.route('/unsuccess', methods = ['POST', 'GET'])
def callback():
    return render_template('unsuccess.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
 
 