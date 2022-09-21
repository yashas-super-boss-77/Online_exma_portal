#step 1 import the package to connect to google server
import pyrebase

def get_data(email):
    ls = []
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
    name = ''
    dob = ''
    nation = ''
    mcq_flag = 0
    sbq_flag = 0
    mcq_marks = 0
    sbq_marks = 0
    generate_result_flag = 0
    for each_data in data:
        #extract individual data
        email_db = each_data.val()['email']
        if(email == email_db):
            name = each_data.val()['name']
            dob = each_data.val()['dob']
            nation = each_data.val()['nationality']
            mcq_marks = each_data.val()['mcq_marks']
            mcq_flag = each_data.val()['mcq_flag']
            sbq_flag = each_data.val()['sbq_flag']
            sbq_marks = each_data.val()['sbq_marks']
            generate_result_flag = each_data.val()['generate_result_flag']
            
            
    ls = [name, dob, nation,mcq_flag,mcq_marks,sbq_flag,sbq_marks,generate_result_flag]
    return ls
def get_sbq_ans_data():
    ls = []
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
    firebase = pyrebase.initialize_app(firebaseConfig)
    #create a database object
    database_obj = firebase.database()
    data = database_obj.child('project_01_data'+'/'+'sbq_marks').get()
    
    for each_data in data:
        #extract individual data
        ls.append(each_data.val()['answers'])
        
    return ls
        
    
     
    