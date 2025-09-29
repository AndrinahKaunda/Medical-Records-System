from flask import Flask, render_template, request, redirect, session, flash, url_for
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret"
#connect to database
db = mysql.connector.connect(
    host = "localhost",
    user = "root", 
    password = "",
    database ="medical_records",
)
#excute queries/talk to database
cursor = db.cursor()

@app.route("/")
def index():
    return render_template('index.html')

#user Register
@app.route("/register", methods=["POST", "GET"])
def register():
    #enter username
    if request.method == "POST":
        username =request.form['username']#use request.form to get fields from html form
        email = request.form['email']
        password = request.form['passwd']

        #validating fuction
        error = validate_user(username, email, password)
        if error:
            return error
        
        #hashed password
        hashed_pw = generate_password_hash(password)
        
        #check if email alresdy exist(%s-placehoder, (email)-tuple)
        cursor.execute("SELECT email FROM users WHERE email = %s ", (email,))
        #if it finds match
        if cursor.fetchone():
            cursor.close()
            return ("email already registered")
            
        else:
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, hashed_pw)
            )
            db.commit()  # Save changes to the database
            if cursor.rowcount > 0:
                return ("Successfully registered")
            else:
                return ("Registration failed")
            
            
@app.route('/login', methods=["GET","POST"])
def login():
    if request.method =="POST":   
        email =request.form['email']
        password = request.form['passwd']
         

        #Authentication
        cursor.execute("SELECT username, email, password FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user:
            username, email, stored_hash = user
            # Compare entered password with stored hash
            if check_password_hash(stored_hash, password):
                session['username'] = username
                session['email'] = email
               # message =flash("Successfully logged in")
                return render_template("dashboard.html")
            else:
                return ("INVALID Email OR PASSWORD")
        else:
            return "INVALID Email OR PASSWORD"
        

#dashboard route
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "username" not in session:
        flash("please login")
        return redirect(url_for("login"))
    return render_template("dashbord.html", username=session["username"])

@app.route("/patient-records", methods=["GET", "POST"])
def patient_records():
    return render_template("patient-records.html")

@app.route("/visit-record", methods=["GET", "POST"])
def visit_record():
    return render_template("visit-record.html")

#logging out 
@app.route("/logout")
def logout():
    session.clear()
    flash("you have been logged out")
    return redirect("/")


#register: validating imputs
def validate_user(username, email, password):
        if username == "" or email == "" or password == "":
            return "Please fill all fields."

        if "@" not in email or "." not in email:
            return "Please enter a valid email address."

        if len(password) < 8:
            return "Password must be at least 8 characters."
        





#close connection
#cursor.close()
#db.close()

#turn off during deployment
if __name__ == "__main__":
    app.run(debug=True)