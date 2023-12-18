from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('tutorial.html')


app.run()