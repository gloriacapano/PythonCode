from flask import Flask
from flask import request, jsonify, Response
from flask_httpauth import HTTPTokenAuth
import bcrypt

app = Flask(__name__)
auth = HTTPTokenAuth()


# Security Layer
#pw_hash = bcrypt.hashpw('ArthurConanDoyle'.encode('utf-8'), bcrypt.gensalt(14))
token_hash = b'$2b$14$4BhyNJEbpyXP5P/4GsPVAueKc0PrWuYrPs6xSwBalyttgVxyBne0W'
#bcrypt.checkpw(pw_hash, 'ArthurConanDoyle') # returns True


@auth.verify_token
def verify_token(token):
    token = token.encode('utf-8')
    return bcrypt.checkpw(token, token_hash)

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

