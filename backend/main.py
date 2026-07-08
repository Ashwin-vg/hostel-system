from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pymongo import MongoClient
import random

app = FastAPI()

# ================= DB =================
client = MongoClient("mongodb://localhost:27017/")
db = client["hostel"]

students_col = db["students"]
rooms_col = db["rooms"]
alloc_col = db["allocations"]

# ================= STATIC =================
app.mount("/static", StaticFiles(directory="../static"), name="static")

# ================= CORS =================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================= HOME =================
@app.get("/")
def home():
    return FileResponse("../static/login.html")

# ================= LOGIN =================
@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username.strip() == "admin" and password.strip() == "1234":
        return {"msg": "success"}
    return {"msg": "fail"}

# ================= DEMO DATA =================
@app.get("/demo")
def demo():
    students_col.delete_many({})
    rooms_col.delete_many({})
    alloc_col.delete_many({})

    male_names = ["Rahul","Arjun","Vishnu","Kiran","Akhil","Sandeep","Adarsh","Hari","Anand","Rohit"]
    female_names = ["Anu","Meera","Sneha","Nithya","Divya","Gayathri","Lakshmi","Pooja","Aparna","Neha"]

    depts = ["CSE","ECE","EEE","ME"]

    students = []
    sid = 1

    # 50 students
    for i in range(25):
        students.append({
            "id": sid,
            "name": male_names[i % 10] + str(i),
            "dept": random.choice(depts),
            "gender": "Male",
            "dues": random.choice([0,0,200,500])
        })
        sid += 1

    for i in range(25):
        students.append({
            "id": sid,
            "name": female_names[i % 10] + str(i),
            "dept": random.choice(depts),
            "gender": "Female",
            "dues": random.choice([0,0,300])
        })
        sid += 1

    students_col.insert_many(students)

    # ROOMS
    rooms = []
    rid = 101

    for i in range(5):
        rooms.append({"id": rid, "type": f"AC-M{i}", "capacity": 5, "gender": "Male"})
        rid += 1

    for i in range(5):
        rooms.append({"id": rid, "type": f"AC-F{i}", "capacity": 5, "gender": "Female"})
        rid += 1

    rooms_col.insert_many(rooms)

    # 🔥 PARTIAL ALLOCATION (leave beds free)
    for s in students:
        if random.choice([True, False]):  # only allocate some students
            for r in rooms:
                if s["gender"] == r["gender"]:
                    count = alloc_col.count_documents({"room_id": r["id"]})

                    if count < r["capacity"]:
                        alloc_col.insert_one({
                            "student_id": s["id"],
                            "room_id": r["id"]
                        })
                        break

    return {"msg": "Demo inserted (partial allocation)"}

# ================= STUDENTS =================
@app.get("/students/all")
def get_students():
    return list(students_col.find({}, {"_id": 0}))

@app.post("/students")
def add_student(name: str = Form(...), dept: str = Form(...), gender: str = Form(...)):
    last = students_col.find_one(sort=[("id", -1)])
    new_id = 1 if not last else last["id"] + 1

    students_col.insert_one({
        "id": new_id,
        "name": name.strip(),
        "dept": dept,
        "gender": gender,
        "dues": 0
    })

    return {"msg": "Student added"}

# 🔥 DELETE STUDENT
@app.post("/students/delete")
def delete_student(student_id: int = Form(...)):
    students_col.delete_one({"id": student_id})
    alloc_col.delete_many({"student_id": student_id})
    return {"msg": "Deleted"}

# ================= ROOMS =================
@app.get("/rooms/all")
def get_rooms():
    rooms = list(rooms_col.find({}, {"_id": 0}))

    for r in rooms:
        allocs = list(alloc_col.find({"room_id": r["id"]}))
        members = []

        for a in allocs:
            s = students_col.find_one({"id": a["student_id"]})
            if s:
                members.append(f"{s['name']} (ID:{s['id']})")

        r["members"] = members
        r["available"] = r["capacity"] - len(members)

    return rooms

# ================= ALLOCATION =================
@app.post("/allocate")
def allocate(student_id: int = Form(...), room_id: int = Form(...)):

    if alloc_col.find_one({"student_id": student_id}):
        return {"msg": "Already allocated"}

    student = students_col.find_one({"id": student_id})
    room = rooms_col.find_one({"id": room_id})

    if not student or not room:
        return {"msg": "Invalid ID"}

    if student["gender"] != room["gender"]:
        return {"msg": "Gender mismatch"}

    count = alloc_col.count_documents({"room_id": room_id})

    if count >= room["capacity"]:
        return {"msg": "Room full"}

    alloc_col.insert_one({
        "student_id": student_id,
        "room_id": room_id
    })

    return {"msg": "Allocated"}

# ================= DEALLOCATE =================
@app.post("/deallocate")
def deallocate(student_id: int = Form(...)):
    alloc_col.delete_one({"student_id": student_id})
    return {"msg": "Removed"}

# ================= DUES =================
@app.get("/dues/all")
def get_dues():
    return list(students_col.find({"dues": {"$gt": 0}}, {"_id": 0}))

@app.post("/dues/pay")
def pay_dues(student_id: int = Form(...)):
    students_col.update_one({"id": student_id}, {"$set": {"dues": 0}})
    return {"msg": "Paid"}

# ================= STATS =================
@app.get("/stats")
def stats():
    students = students_col.count_documents({})
    rooms = list(rooms_col.find({}))

    total_beds = sum(r["capacity"] for r in rooms)
    occupied = alloc_col.count_documents({})
    available = total_beds - occupied

    dues = students_col.count_documents({"dues": {"$gt": 0}})

    return {
        "students": students,
        "available_beds": available,
        "dues": dues,
        "rooms": len(rooms)   # 🔥 NEW
    }