from flask import Flask
from flask import request, jsonify, Response
from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
bcrypt = Bcrypt(app)
auth = HTTPBasicAuth()


# Security Layer
user = "sherlock"
#pw_hash = bcrypt.generate_password_hash('ArthurConanDoyle')
pw_hash = b'$2b$12$p57K.BF0n2vg6qcgo25LIe7TZOlM4tCreFObRatGNeIZxxeotYSLu'
#bcrypt.check_password_hash(pw_hash, 'ArthurConanDoyle') # returns True

@auth.verify_password
def verify_password(username, password):
    if username != user:
        return False
    return bcrypt.check_password_hash(pw_hash, password)



###
# Caesar Cipher
def caesar_encryption(message, step):
    result = "" 
    # traverse message
    for i in range(len(message)): 
        char = message[i] 
        # Encrypt uppercase characters 
        if (char.isupper()): 
            result += chr((ord(char) + step -65) % 26 + 65) 
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + step - 97) % 26 + 97) 
    return result 


# APIs
@app.route("/welcome", methods=["GET"])
@auth.login_required
def welcome():
    return 'Welcome Mr. Sherlock Holmes'


@app.route("/encrypt", methods=["POST"])
@auth.login_required
def encrypt():
    if 'message' in request.json:
        message = request.json["message"]
    else:
        return ("No message has been given")
    if "step" in request.json:
        message = request.json["step"]
    else:
        step = 3
    
    message = caesar_encryption(message, step)
    return jsonify(message)





if __name__ == "__main__":
    app.run(debug=True)

