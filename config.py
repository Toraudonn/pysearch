import os

# application settings
MONGO_URL = 'MONGO_URL'

# Generate a random secret key
SECRET_KEY = os.urandom(24)
CSRF_ENABLED = True
