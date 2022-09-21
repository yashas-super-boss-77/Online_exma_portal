#import the special package
from firebase import firebase

def insert_data(obj, path):
    try:
        #prepare the database object
        firebase1 = firebase.FirebaseApplication('https://firstapp-d694c-default-rtdb.firebaseio.com')
        #insert the data
        firebase1.post(path,obj)
        print("insert data done")
        return True
    except:
        return False
