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

for (First Name,Last Name,Patient ID,Gender,DOB,Telephone.no,Emergency Contact,Blood Type	Allergies	
) in cursor:
    pass


