from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success', methods = ['POST', 'GET'])
def search():
    return render_template('success.html')

@app.route('/unsuccess', methods = ['POST', 'GET'])
def callback():
    return render_template('unsuccess.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)