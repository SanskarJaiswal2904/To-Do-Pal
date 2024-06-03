from flask_pymongo import PyMongo
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS
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

if __name__ == "__main__":
    app.run(debug=True, port=1024)
