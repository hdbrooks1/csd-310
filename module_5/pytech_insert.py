from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.4sggwrz.mongodb.net/"

client = MongoClient(url)

db = client.pytech

students = db.students

student1 = {
    "student_id": 1007,
    "first_name": "Johnny",
    "last_name": "Rockets"
}

student2 = {
    "student_id": 1008,
    "first_name": "Joe",
    "last_name": "Smith"
}

student3 = {
    "student_id": 1009,
    "first_name": "Michael",
    "last_name": "Jackson"
} 

student1_id = students.insert_one(student1).inserted_id
student2_id = students.insert_one(student2).inserted_id
student3_id = students.insert_one(student3).inserted_id

print(student1_id)
print(student2_id)
print(student3_id)

print("-- INSERT STATEMENTS --")
print("Inserted student record Johnny Rockets into students collection with document id :", student1_id)
print("Inserted student record Joe Smith into students collection with document id :", student2_id)
print("Inserted student record Micheal Jackson into students collection with document id :", student3_id)