from flask import *
app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, 
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
    }

@app.route("/")
def main():
    return ("Welcome to the Flask API!")


@app.route("/status")
def status():
    return ("OK")

@app.route("/data")
def data():
    return (jsonify(list(users.keys())))

@app.route("/users/<username>")
def usernames(username):
    user = users.get(username)
    if user:
        return (jsonify(user))
    else:
        return (jsonify({"error": "User not found"})), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if("username" not in data):
        return jsonify({"error": "Username is required"}), 400
    else:
        usernames = data['username']
        if usernames in users:
            return jsonify({"error": "User already exists"}), 400
        
        users[usernames] = {
                        "username": data["username"],
                        "name": data.get("name", ""),
                        "age": data.get("age", 0),
                        "city": data.get("city", "")
                        }
        return jsonify({
        "message": "User added",
        "user": users[usernames]
    }), 201
        
@app.route("/delete_user/<username>", methods=["DELETE"])
def delete_user(username):
    # Kullanıcı var mı kontrol et
    if username in users:
        # Kullanıcıyı sil
        del users[username]
        return jsonify({"message": f"User '{username}' has been deleted"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

        
if __name__ == "__main__":
    app.run(debug=True)