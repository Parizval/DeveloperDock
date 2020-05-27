from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, static_url_path='/static')

app.debug = True
app.secret_key = "Nothing"

@app.route("/")
def index():
    return render_template("index.html")



    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
