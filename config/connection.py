import pyrebase

def connect():
    print("connection started")
    
    #step 2 connect to google server
    try:
        firebaseConfig = {
            'apiKey': "AIzaSyCmkOmKHIrGoRNiamsj3GgM7zSH9iItkwc",
            'authDomain': "firstapp-d694c.firebaseapp.com",
            'databaseURL': "https://firstapp-d694c-default-rtdb.firebaseio.com",
            'projectId': "firstapp-d694c",
            'storageBucket': "firstapp-d694c.appspot.com",
            'messagingSenderId': "411792344978",
            'appId': "1:411792344978:web:b2be36b906278f3aede34b",
            'measurementId': "G-JB2L6404E8"
            }
        print("done connection.....")
        
    
        #step 3 start the server
        firebase = pyrebase.initialize_app(firebaseConfig)
        return True, firebase

    except :
        print("error connection")
        return False, "null"