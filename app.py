from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson import ObjectId  # Import ObjectId for converting string to ObjectId
import datetime

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://to-do-pal.vercel.app"]}})  # Allow requests from your Vue app's origin

app.config["MONGO_URI"] = "mongodb://localhost:27017/todopal"
db = PyMongo(app).db

# createSignup
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
    return jsonify({"message": "Signup successful"}), 201

# Login
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = db.user_info.find_one({"email": email})
    if user and user['password'] == password:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401

# Post Notes
@app.route("/notes", methods=["POST"])
def save_note():
    data = request.get_json()
    id = data.get('_id')
    title = data.get('title')
    description = data.get('description')

    if not title or not description:
        return jsonify({"error": "Title and description are required."}), 400

    note = {
        "_id": id,
        "title": title,
        "description": description,
        "datecreated": datetime.datetime.utcnow()
    }

    db.note_data.insert_one(note)
    return jsonify({"message": "Note saved successfully"}), 201

# Get Notes
@app.route("/notes", methods=["GET"])
def get_notes():
    notes = list(db.note_data.find({}, {"_id": 1, "title": 1, "description": 1, "datecreated": 1}))
    for note in notes:
        note["_id"] = str(note["_id"])
    return jsonify(notes)

# Delete All Notes
@app.route("/notes/deleteall", methods=["DELETE"])
def delete_all_notes():
    result = db.note_data.delete_many({})
    if result.deleted_count > 0:
        return jsonify({"message": "All notes deleted successfully"}), 200
    else:
        return jsonify({"error": "No notes found to delete"}), 404

# Delete One Note
@app.route("/notes/deleteone/<string:sno>", methods=["DELETE"])
def delete_one_note(sno):
    note = db.note_data.find_one({"_id": sno})
    if note:
        db.note_data.delete_one({"_id": sno})
        return jsonify({"message": f"Note with ID {sno} deleted successfully"}), 200
    else:
        return jsonify({"error": f"No note found with ID {sno}"}), 404

# Update One Note
@app.route("/notes/update/<string:sno>", methods=["PATCH"])
def update_one_note(sno):
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    # Validation
    if not title or not description:
        return jsonify({"error": "Title and description are required."}), 400

    # Find the note by _id and update it
    result = db.note_data.update_one(
        {"_id": sno},
        {"$set": {"title": title, "description": description, "dateupdated": datetime.datetime.utcnow()}}
    )

    if result.matched_count > 0:
        return jsonify({"message": f"Note with ID {sno} updated successfully"}), 200
    else:
        return jsonify({"error": f"No note found with ID {sno}"}), 404

# Get All Users
@app.route("/alluser", methods=["GET"])
def get_all_users():
    try:
        users = list(db.user_info.find({}, {"_id": 1, "name": 1, "email": 1}))
        for user in users:
            user["_id"] = str(user["_id"])
        return jsonify(users)
    except Exception as e:
        print(f"Error fetching users: {str(e)}")  # Log the error to the server console
        return jsonify({"error": "An error occurred while fetching users."}), 500

# Delete User
@app.route("/deleteUser/<string:sno>", methods=["DELETE"])
def delete_user(sno):
    try:
        user_id = ObjectId(sno)
    except Exception:
        return jsonify({"error": "Invalid user ID"}), 400

    user_to_delete = db.user_info.find_one({"_id": user_id})

    if user_to_delete:
        db.user_info.delete_one({"_id": user_id})
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=1024)
