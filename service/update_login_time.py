from datetime import datetime
import  sys
sys.path.insert(0,'mapper')
from mapper import make_obj
sys.path.insert(0, 'service')
from service import insert_data

def f_log(email):
    #login time and date  
    path = "project_01_data/f_log"
    now = datetime.now()
    login_time = now.strftime("%H:%M:%S")
    login_date = now.strftime("%d:%m:%y")
    print("login details\n", login_time, login_date)
    obj = [email, login_time, login_date]
    
    obtained_data = make_obj.prepare_flog_obj(obj)
    
    if(insert_data.insert_data(obtained_data, path)):
        print("login and date entered")
    else:
        print("login and date could not be entered")
    