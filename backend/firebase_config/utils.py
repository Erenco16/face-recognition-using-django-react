import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth

def initialize_app():
    # Use a secure service account JSON file
    cred = credentials.Certificate("/Users/godfather/Desktop/Software/connect_django_to_react/backend/firebase_config/serviceAccount.json")

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

def write_face_encodings_to_db(auth, app, request, user_email, user_uid, face_encodings):
    key = request.COOKIES.get('userUid')

    

    ref_face = db.reference("/face_encodings")
    ref_face.push().set({
            "title": f"{user_email}",
            "face_encodings": f"{face_encodings}",
            "user_uid": f"{user_uid}"
        })

def write_to_db(request, user_email, user_uid, face_encodings):
    app = initialize_app()
    write_face_encodings_to_db(auth, app, request, user_email, user_uid, face_encodings)