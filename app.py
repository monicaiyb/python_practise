from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['Get'])
def hello_world():
    return render_template home.html

@app.route("/login", methods=['Get'])
def login():
    return "<h3>Hello, Monica !</h3>"

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')