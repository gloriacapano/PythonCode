import bcrypt

password = "EdgarAllanPoe"
password = password.encode('utf-8')

# In Flask it would be
#password = request.form.get("password").encode('utf-8')

# Hashing the password with salt
hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

# Check if password and hashed_pw are equivalent or not
check = bcrypt.checkpw(password, hashed_pw)

if check:
    print("Match")
else:
    print("Do not match")

# Adjustable rounds in salt (default=12). 
# However, time to hash increases
import time
def hash_time(round):
    t0 = time.time()
    hashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds=round))
    return (time.time() - t0)

htime = []
for r in range(12, 20):
    print(r)
    htime.append(hash_time(r))

print(htime)
```
[0.30292367935180664, 
 0.6008026599884033, 
 1.2109003067016602, 
 2.3889319896698, 
 4.780720949172974, 
 9.863308668136597, 
 19.866438627243042, 
 39.572778940200806]
```

# Very long password (more than 72 characters)

import base64
import hashlib


password = password * 10
hashed_pw = bcrypt.hashpw(
    base64.b64encode(hashlib.sha256(password).digest()),
    bcrypt.gensalt()
    )