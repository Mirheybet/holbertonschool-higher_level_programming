from flask import *
from flask_httpauth import *
from flask_jwt_extended import *
from werkzeug.security import *

app = Flask(__name__)


app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)
auth = HTTPBasicAuth()


users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

#role uzre tesdiqlenmeni burda edirem
@auth.verify_password
def verify_password(username, password):
    #useri cek
    user = users.get(username)
    #eger username+parol duzdurse adini return ele
    if user and check_password_hash(user['password'], password):
        return username

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

#jwt ile role tesdiqlenmesi
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    #passwordu al ve check ele DB(bizim json datasetimiz) ile
    username = data.get("username")
    password = data.get("password")
    
    user = users.get(username)
    
    #yoxla ve token yarat
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={"username": username, "role": user['role']})
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401


#token ucun access-lik yoxlayir
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

#burda ancaq adminler ucun access vermisik , eger user admin role olmasa onda eror verecek
@app.route("/admin-only")
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

#diger xetalar olarsa 
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    app.run(debug=True)
