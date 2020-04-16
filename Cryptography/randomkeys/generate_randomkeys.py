# Use secrets (python >= 3.6)
import secrets
key = secrets.token_urlsafe(16)

# Use os
import os
os.urandom(12).hex()
