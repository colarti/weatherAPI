from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('tutorial.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

app.run(debug=True)