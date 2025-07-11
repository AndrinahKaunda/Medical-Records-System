import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="medical_db"
    )

def register_user(username, email, password):
    db = connect_db()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                       (username, email, password))
        db.commit()
        return True
    except mysql.connector.Error as err:
        print("Registration error:", err)
        return False
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
