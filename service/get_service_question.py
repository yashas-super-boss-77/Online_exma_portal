#step 1 import the package to connect to google server
import pyrebase

def get_questions(email):
    dic = {}
    #step 2 connect to google server
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
    
    #step 3 start the server
    firebase = pyrebase.initialize_app(firebaseConfig)
    #create a database object
    database_obj = firebase.database()
    data = database_obj.child('project_01_data'+'/'+'personal_details').get()
    #print(data)
    
    #extract the data
    for each_data in data:
        #extract individual data
        email_db = each_data.val()['email']
        if(email == email_db):
            q1 = each_data.val()['What is your pet name?']
            q2 = each_data.val()['Where were you born?']
            q3 = each_data.val()['What is the name of your school?']
            q4 = each_data.val()['What is yur favorite food?']
            q5 = each_data.val()['What is your favorite color']
    
    dic = {'What is your pet name?' : q1,
           'Where were you born?' : q2,
           'What is the name of your school?' : q3,
           'What is yur favorite food?' : q4,
           'What is your favorite color' : q5   
        }
    return dic