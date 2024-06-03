from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

app.config["MONGO_URI"] = "mongodb://localhost:27017/todopal"
db = PyMongo(app).db

@app.route("/signup", methods=["POST"])
def insertDB():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    gender = data.get('gender')

    # Validation
    if not name or len(name) > 50:
        return jsonify({"error": "Name is required and must be less than 50 characters."}), 400
    if not email:
        return jsonify({"error": "Email is required."}), 400
    if not password or len(password) > 20:
        return jsonify({"error": "Password is required and must be less than 20 characters."}), 400
    if gender not in ["male", "female", "others"]:
        return jsonify({"error": "Gender must be 'male', 'female', or 'others'."}), 400

    user = {
        "name": name,
        "email": email,
        "password": password,
        "gender": gender
    }

    db.user_info.insert_one(user)
    return jsonify({"message": "done successfully"}), 201

@app.route("/signup", methods=["GET"])
def get_all_users():
    users = list(db.user_info.find({}, {"_id": 0}))
    return jsonify(users)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = db.user_info.find_one({"email": email, "password": password})
    if user:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401

# New route to save notes
@app.route("/notes", methods=["POST"])
def save_note():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return jsonify({"error": "Title and description are required."}), 400

    note = {
        "title": title,
        "description": description,
        "datecreated": datetime.datetime.utcnow()
    }

    db.note_data.insert_one(note)
    return jsonify({"message": "Note saved successfully"}), 201

# New route to get all notes
@app.route("/notes", methods=["GET"])
def get_notes():
    notes = list(db.note_data.find({}, {"_id": 1}))
    return jsonify(notes)

#deleteAll
@app.route("/notes/deleteall", methods=["DELETE"])
def delete_all_notes():
    result = db.note_data.delete_many({})
    if result.deleted_count > 0:
        return jsonify({"message": "All notes deleted successfully"}), 200
    else:
        return jsonify({"error": "No notes found to delete"}), 404
    

#deleteOne
@app.route("/notes/deleteone/<int:sno>", methods=["DELETE"])
def delete_one_note(sno):
    note = db.note_data.find_one({"sno": sno})
    if note:
        db.note_data.delete_one({"sno": sno})
        return jsonify({"message": f"Note with serial number {sno} deleted successfully"}), 200
    else:
        return jsonify({"error": f"No note found with serial number {sno}"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=1024)
