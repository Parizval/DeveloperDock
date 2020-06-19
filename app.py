from flask import Flask, render_template, request, redirect, url_for, session
import mongo


app = Flask(__name__, static_url_path='/static')

app.debug = True
app.secret_key = "Nothing"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def LoginPage():
    return render_template("login.html")

@app.route("/dashboard")
def DashBoardPage():
    return render_template("index.html")

# Ajax Function 
@app.route('/login_action', methods=['POST'])
def login_action():

    email = request.form['email']
    password = request.form['password']
    print(email, password)
    data = {}
    result = mongo.Login(email,password)
    if result['check']:
        session['email'] = email 
        session['name'] = result['name'] 

        data['check'] = True 
        data['link'] = "/dashboard"
    
    return data

@app.route('/sign_action', methods=['POST'])
def sign_action():

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
   
    print(name,email,password)
    data = {}
    if mongo.Register(email,name,password):
        session['email'] = email 
        session['name'] = name 
        data['check'] = True 
        data['link'] = '/dashboard'
  
   

    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
