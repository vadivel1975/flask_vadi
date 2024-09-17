from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "sugu", "age": 25, "score": 85},
    {"id": 2, "name": "mani", "age": 30, "score": 90},
    {"id": 3, "name": "vijay", "age": 22, "score": 78},
    {"id": 4, "name": "uva", "age": 28, "score": 92}
]

# Helper function to find a user by ID
def find_user(user_id):
    return next((user for user in users if user['id'] == user_id), None)

# GET: Retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# POST: Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    users.append(new_user)
    return jsonify({"message": "User added successfully", "user": new_user}), 201

# PUT: Update an existing user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = find_user(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404
    
    data = request.json
    user.update(data)  # Update the user with the new data
    return jsonify({"message": "User updated successfully", "user": user})

# DELETE: Delete a user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = find_user(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404
    
    users.remove(user)
    return jsonify({"message": "User deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
