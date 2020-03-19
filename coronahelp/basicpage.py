from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/request/')
def request():
    return render_template('request.html')

@app.route('/deliver/')
def deliver():
    return render_template('deliver.html')

if __name__ == '__main__':
    app.run(debug=True)
