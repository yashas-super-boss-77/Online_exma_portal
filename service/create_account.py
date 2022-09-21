from tkinter import messagebox
#connect to OS path
import sys
sys.path.insert(0,'config')
from config import connection 
from firebase import firebase
import pyrebase

def Create(email, passw):
    r_status, value = connection.connect()
    if( r_status != True):
        return False
    else:
        try:
            #step 5 create an object
            authentication_obj = value.auth()
            authentication_obj.create_user_with_email_and_password(email, passw)
            print("done")
            return True
        except:
            print("something error create_account")
            return False
            
    
    
    