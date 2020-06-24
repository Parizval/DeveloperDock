from flask import Flask, render_template, request, redirect, url_for, session
import mongo

import NormalModel
import KubeModel

import NormalFormat
import KubeFormat


app = Flask(__name__, static_url_path='/static')

app.debug = True
app.secret_key = "Nothing"

@app.route("/")
def index():
    if "name" in session:
        return redirect("/dashboard")
    return render_template("index.html")

@app.route("/login")
def LoginPage():
    if "name" in session:
        return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard")
def DashBoardPage():
    if "name" in session:
        StatData,TableData =  mongo.ProjectStats(session['email'])
        return render_template("/Dashboard/light/index.html",name=session['name'],email=session['email'],StatData=StatData,TableData=TableData)
    return redirect("/")

@app.route("/logout")
def LogOut():
    session.clear()
    return redirect("/")

@app.route("/strategy")
def Strategy():
    if "name" in session:
        return render_template("/Dashboard/light/strategy.html",name=session['name'],email=session['email'])
    return redirect("/")

@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


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

@app.route('/strategy_action',methods=['POST'])
def StrategyAction():

    ProjectName = request.form['ProjectName']
    LineCode = request.form['LineCode']
    Language = request.form['Language']
    Cloud = request.form['Cloud']
   
    Function = request.form['Function']
   
    print(ProjectName,LineCode,Language,Cloud,Function)
    
    result = KubeModel.KubePrediction(Language,Function,LineCode)
    print(result)
    Format = KubeFormat.Formatting(result)
    mongo.Project(ProjectName,LineCode,Language,Cloud,Function,result,session['email'])
    
    data = {}
    data['check'] = True
    data['output'] = result
    data['Format'] = Format
    return data  

@app.route('/strategy_normal',methods=['POST'])
def NormalStrategy():
    ProjectName = request.form['ProjectName']
    LineCode = request.form['LineCode']
    Language = request.form['Language']
    Function = request.form['Function']

    result = NormalModel.NormalPrediction(Language,Function,LineCode)
    Format = NormalFormat.Formatting(result)
    
    mongo.NormalProject(ProjectName,LineCode,Language,Function,result,session['email'])
    data = {}
    data['check'] = True 
    data['output'] = result
    data['Format'] = Format
    return data
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
