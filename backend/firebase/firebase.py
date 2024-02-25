import firebase_admin
from firebase_admin import credentials

# Use a secure service account JSON file
cred = credentials.Certificate("serviceAccount.json")

# Initialize Firebase app
firebase_admin.initialize_app(cred)