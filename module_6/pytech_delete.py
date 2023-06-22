from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.4sggwrz.mongodb.net/"

client = MongoClient(url)

db = client.pytech

students = db.students

#Insert student document 1010
print("-- INSERTING STUDENT DOCUMENT 1010 --")
print("")
student1010 = {
    "student_id": 1010,
    "first_name": "Jimmy",
    "last_name": "Cakes"
}
student1_id = students.insert_one(student1010).inserted_id

#Display the new student 1010
student = students.find_one({"student_id": 1010})

print("Student with student_id 1010:")
print("Student ID:", student["student_id"])
print("First Name:", student["first_name"])
print("Last Name:", student["last_name"])
print("")


#Delete Student Document 1010
print("-- DELETING STUDENT DOCUMENT 1010 --")
print("")
result = students.delete_one({"student_id": 1010})


# Display all documents in the collection
docs = students.find({})

print("-- DISPLAYING STUDENTS DOCUMENT FROM find() QUERY --")
for doc in docs:
    print("Student ID:", doc["student_id"])
    print("First Name:", doc["first_name"])
    print("Last Name:", doc["last_name"])
    print()