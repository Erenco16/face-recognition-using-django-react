import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

def initialize_app():
    # Use a secure service account JSON file
    cred = credentials.Certificate("serviceAccount.json")

    app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://test-react-app-f5032-default-rtdb.firebaseio.com'})
    return app

def get_user_uids():
    try:
        ref = db.reference("/users")
        user_uids = []
        data = ref.get()
        for key in data:
            user_uids.append(data[key]['user_uid'])
        return user_uids
    except Exception as e:
        print(f"Error while getting database: {e}")

def write_face_encodings_to_db():
    ref_face = db.reference("/face_encodings")
    ref_face.push().set({
        "username": "Eren test username",
        "face_encodings": "face encodings will sit here",
        "user_uid": "user uid foreign key column"
    })

def main():
    app = initialize_app()
    
    print(get_user_uids())

    write_face_encodings_to_db()

if __name__ == "__main__":
    main()