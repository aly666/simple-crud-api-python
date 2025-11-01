from flask import Flask, request, jsonify

app = Flask(__name__)

# Data dummy disimpan dalam list
users = []
counter = 1  # auto-increment id manual


# CREATE
@app.route("/users", methods=["POST"])
def create_user():
    global counter
    data = request.json
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"message": "name & email required"}), 400

    user = {
        "id": counter,
        "name": name,
        "email": email
    }
    users.append(user)
    counter += 1
    return jsonify({"message": "User created", "user": user}), 201


# READ ALL
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


# READ ONE
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404


# UPDATE
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    name = data.get("name")
    email = data.get("email")

    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"message": "User not found"}), 404

    if name:
        user["name"] = name
    if email:
        user["email"] = email

    return jsonify({"message": "User updated", "user": user}), 200


# DELETE
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    new_users = [u for u in users if u["id"] != user_id]

    if len(new_users) == len(users):
        return jsonify({"message": "User not found"}), 404

    users = new_users
    return jsonify({"message": "User deleted"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

