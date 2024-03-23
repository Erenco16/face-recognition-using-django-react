import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth
import ast

def compare_face_encodings(target_encoding, reference_encodings, threshold=0.6):
    similarities = np.dot(reference_encodings, target_encoding.T)
    best_match_index = np.argmax(similarities)
    max_similarity = similarities[best_match_index]
    if max_similarity >= threshold:
        if(best_match_index >= 0):
            return True
    else:
        return None

def convert_data_into_numpy_array(str_face_encodings):
    # Remove unnecessary characters from the string representation
    str_face_encodings = str_face_encodings.replace("{'face_encodings': ", "").replace("}", "")
    # Extracting the list of lists from the string
    data_list = ast.literal_eval(str_face_encodings)
    # Convert the parsed data into a numpy array
    numpy_array = np.array(data_list)
    return numpy_array

def get_facial_encodings(userEmail):
    try:
        ref = db.reference("/face_encodings")
        all_face_encodings = []
        data = ref.get()
        for key in data:
            if(data[key]['title'] == userEmail):
                print("in the for loop")
                face_encodings = str(data[key]['face_encodings'])
                final_face_encodings = convert_data_into_numpy_array(face_encodings)
                all_face_encodings.append(final_face_encodings)
        return all_face_encodings
    except Exception as e:
        print(f"Error while getting database: {e}")

def get_email_index(userEmail):
    try:
        ref = db.reference("/face_encodings")
        all_face_encodings = []
        data = ref.get()
        index = 0
        for key in data:
            index = index + 1
            if(data[key]['title'] == userEmail):
                return index
    except Exception as e:
        print(f"Error while getting database: {e}")


def return_match_record(target_encodings, target_email):
    target_encoding = np.array(target_encodings['face_encodings'])
    reference_encodings = get_facial_encodings(target_email)
    if reference_encodings:  # Check if reference encodings are found
        if_same = compare_face_encodings(target_encoding, reference_encodings)
        match_index = get_email_index(target_email)
        if if_same:
            print(f"Match found with reference face at index {match_index}.")
            return match_index
        else:
            print("No match found.")
            return None
    else:
        print("No reference encodings found.")
        return None

def main():
    # Use a secure service account JSON file
    cred = credentials.Certificate("/Users/godfather/Desktop/Software/connect_django_to_react/backend/firebase_config/serviceAccount.json")

    app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://test-react-app-f5032-default-rtdb.firebaseio.com'})
    
    return_match_record()

if __name__ == "__main__":
    main()
