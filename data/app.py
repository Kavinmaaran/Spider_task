import os
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    return render_template('./index.html')

@app.route('/success', methods = ['POST', 'GET'])
def search():
    return render_template('./success.html')

@app.route('/unsuccess', methods = ['POST', 'GET'])
def callback():
    return render_template('./unsuccess.html')
          
if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5000))
   app.run(host="0.0.0.0", port=port)