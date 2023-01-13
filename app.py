from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')    

@app.route("/about")
def about():
    return render_template('about.html', title= 'About Me!')
@app.route("/login")
def user_login():
    pass
@app.route("/register")
def user_signup():
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)