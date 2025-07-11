import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",          # use your password if any
        database="127_0_0_1.sql"
    )

def register_user(username, email, password):
    db = connect_db()
    cursor = db.cursor()

    try:
        cursor.execute("""
            INSERT INTO users (username, email, password)
            from flask import Flask, render_template, request, redirect, jsonify
from db import register_user, login_user

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    success = register_user(data['username'], data['email'], data['passwd'])
    if success:
        return jsonify({"message": "Registration successful!"})
    else:
        return jsonify({"message": "Registration failed!"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    user = login_user(data['email'], data['passwd'])
    if user:
        return jsonify({"message": "Login successful!", "user": user})
    else:
        return jsonify({"message": "Invalid credentials!"}), 401

if __name__ == '__main__':
    app.run(debug=True)
VALUES (%s, %s, %s)
        """, (username, email, password))
        db.commit()
        print("User registered successfully.")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        cursor.close()
        db.close()

def login_user(email, password):
    db = connect_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()

    cursor.close()
    db.close()

    return user



