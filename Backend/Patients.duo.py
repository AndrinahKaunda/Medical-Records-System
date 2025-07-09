import mysql.connector

#Connect to my sql database in XAMPP
db = mysql.connector.connect(
    user="root",
    password="root",
    host="127.0.0.1",
    database="medical_records"
)
cursor = db.cursor()
query = "SELECT * FROM 'patient records'"

cursor.execute(query)

for (firstName,	lastName,	patientID,	gender,	dob, telephoneNO, emergency_Contact, bloodType, allergies) in cursor:
    print(firstName,	lastName,	patientID,	gender,	dob, telephoneNO, emergency_Contact, bloodType, allergies)


