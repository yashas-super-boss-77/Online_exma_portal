#step 1 import the package to connect to google server
import pyrebase
from tkinter import messagebox

def update(email_id, ls):
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
    
    database_obj = firebase.database()
    data = database_obj.child('project_01_data/personal_details').get()
    
    
    flag = 0
    for each_data in data:
        db_email_id = each_data.val()['email']
        if(db_email_id == email_id):
            flag = 1
            #update the name of the individual
            database_obj.child('project_01_data/personal_details').child(each_data.key()).update({'name':ls[0]})
            database_obj.child('project_01_data/personal_details').child(each_data.key()).update({'dob':ls[1]})
            database_obj.child('project_01_data/personal_details').child(each_data.key()).update({'nationality':ls[2]})
    if (flag == 1):
        messagebox.showinfo("info", "data updated")
    else:
        messagebox.showerror("info", "data not updated")     
def update_marks(email_id, ls):
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
    
    database_obj = firebase.database()
    data = database_obj.child('project_01_data/personal_details').get()
    
    
    flag = 0
    for each_data in data:
        db_email_id = each_data.val()['email']
        if(db_email_id == email_id):
            flag = 1
            #update the name of the individual
            database_obj.child('project_01_data/personal_details').child(each_data.key()).update({'mcq_flag':ls[0]})
            database_obj.child('project_01_data/personal_details').child(each_data.key()).update({'mcq_marks':ls[1]})
    if (flag == 1):
        print("info", "marks data updated")
    else:
        print("info", "marks data not updated") 
def update_marks_sbq(email_id, ls):
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
    
    database_obj = firebase.database()
    data = database_obj.child('project_01_data/personal_details').get()
    flag = 0
    for each_data in data:
        db_email_id = each_data.val()['email']
        if(db_email_id == email_id):
            flag = 1
            #update the name of the individual
            database_obj.child('project_01_data/personal_details').child(each_data.key()).update({'sbq_flag':ls[0]})
            database_obj.child('project_01_data/personal_details').child(each_data.key()).update({'sbq_marks':ls[1]})
    if (flag == 1):
        print("info", "marks data updated")
    else:
        print("info", "marks data not updated") 
        
        
def update_generate_result_pdf(email):
    pass