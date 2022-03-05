from flask import Flask, render_template, request, flash

app = Flask(__name__) #to intialize our application, takes in our main module represented by "__name__". This creates a class for our app
app.config['SECRET_KEY'] = 'super secret key' 


@app.route("/hello") #"/hello" represents the last part of the url, meaning www.myurl.com/hello . This is a decorator of a function, so it requires a function.
def index():
    flash("what's your name yowo?")
    return render_template("index.html") 

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " +str(request.form['name_input']) + ", great to see you") 
    return render_template("index.html")

