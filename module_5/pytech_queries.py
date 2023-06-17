from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.4sggwrz.mongodb.net/"

client = MongoClient(url)

db = client.pytech

students = db.students

docs = students.find({})

# Display all documents in the collection
docs = students.find({})

print("-- DISPLAYING STUDENTS DOCUMENT FROM find() QUERY --")
for doc in docs:
    print("Student ID:", doc["student_id"])
    print("First Name:", doc["first_name"])
    print("Last Name:", doc["last_name"])
    print()


    
# Single Student
print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
student = students.find_one({"student_id": 1007})

print("Student with student_id 1007:")
print("Student ID:", student["student_id"])
print("First Name:", student["first_name"])
print("Last Name:", student["last_name"])