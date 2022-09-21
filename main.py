import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import string
import random
#connect to OS path
import sys
sys.path.insert(0,'service')
from service import create_account, update_login_time
from tkinter import messagebox
sys.path.insert(0,'mapper')
from mapper import make_obj
sys.path.insert(0,'service')
from service import insert_data
sys.path.insert(0,'config')
from config import connection
from tkinter.filedialog import askopenfilename
sys.path.insert(0,'service')
from service import Security 
sys.path.insert(0,'config')
from config import connection 
import cv2
from PIL import Image, ImageTk
sys.path.insert(0,'service')
from service import retreive_data
sys.path.insert(0,'service')
from service import update_data
sys.path.insert(0,'service')
from service import get_service_question
from datetime import datetime
from fpdf import FPDF

q_no = -1
mcq_correct_ans = {}
marks = 0
marks1 = 0


def generate_result():
    def print_document():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        list_object_print = [email, l[0], str(l[4]), str(l[6]), current_time]
        #print(list_object_print)
        
        
        # save FPDF() class into a
        # variable pdf
        pdf = FPDF()
 
        # Add a page
        pdf.add_page()
        
        pdf.set_font("Arial", size = 10)
        
 
        pdf.cell(200, 10, "Generated time"+ " : "+ list_object_print[4],
        ln = 2, align = 'L')
        
        pdf.set_font("Arial", size = 30)
        
        # create a cell
        pdf.cell(200, 50, txt = "RESULT",
         ln = 1, align = 'C')
        
        pdf.set_font("Arial", size = 15)
        
        # add another cell
        pdf.cell(200, 10, txt = "Name"+ " : "+ list_object_print[1],
        ln = 2, align = 'C')
        
        pdf.cell(200, 10, txt = "MCQ marks"+ " : "+ list_object_print[2],
        ln = 2, align = 'C')
        
        pdf.cell(200, 10, "SBQ marks"+ " : "+ list_object_print[3],
        ln = 2, align = 'C')
        
        
 
        # save the pdf with name .pdf
        pdf.output("result/"+list_object_print[1]+".pdf")  
        
        messagebox.showinfo("info", "printed")
        try:
            update_data.update_generate_result_pdf(email)
        except:
            print("\n\n\nerror here\n\n\n")
        
        generate_result_frame.place_forget()
        dashboard(email)
    
    email = email_entry2.get()
    l = retreive_data.get_data(email)
    
    if(l[3] == 1):
        mcq_marks = str(l[4])
    else:
        mcq_marks = "Nill"
    if(l[5] == 1):
        sbq_marks = str(l[6])
    else:
        sbq_marks = "Nill"
    
    #print(mcq_marks, sbq_marks)
    
    dashboard_frame.place_forget()
    dashboard_background_frame.place_forget()
    
    generate_result_frame = Frame(w, relief = SUNKEN, bg = 'white')
    generate_result_frame.place(x = 400, y = 100, height = 500, width = 500)
    
    title_label = Label(generate_result_frame, text = "RESULT", bg = "blue", fg = "white", font = ('rockwell', 20))
    title_label.place(x = 200, y = 10)
    
    name_label = Label(generate_result_frame, text = "NAME", bg = "black", fg = "white", font = ('rockwell', 20))
    name_label.place(x = 30, y = 100)
    
    name_label = Label(generate_result_frame, text = l[0], bg = "pink", fg = "blue", font = ('rockwell', 20))
    name_label.place(x = 250, y = 100)
    
    name_label = Label(generate_result_frame, text = "MCQ", bg = "black", fg = "white", font = ('rockwell', 20))
    name_label.place(x = 30, y = 150)
    
    name_label = Label(generate_result_frame, text = mcq_marks, bg = "pink", fg = "blue", font = ('rockwell', 20))
    name_label.place(x = 250, y = 150)
    
    name_label = Label(generate_result_frame, text = "SBQ (plagarism)", bg = "black", fg = "white", font = ('rockwell', 20))
    name_label.place(x = 30, y = 200)
    
    name_label = Label(generate_result_frame, text = sbq_marks, bg = "pink", fg = "blue", font = ('rockwell', 20))
    name_label.place(x = 250, y = 200)
    
    print_button = Button(generate_result_frame, command = print_document, text = "Print", font = ("rockwell", 20), bg = "blue", fg = "white")
    print_button.place(x = 400, y = 400)
    
    
def exam_start_mcq():
    email = email_entry2.get()
    def exam_start():
        def finish_mcq():
            correct = 0
            wrong = 0
            not_answered = 0
            print(len(mcq_options), len(mcq_correct_ans), len(examinee_ans))
            for i in range(len(examinee_ans)):
                if(mcq_options[i][mcq_correct_ans[i]-1] == examinee_ans[i]):
                    correct += 1
                elif (examinee_ans == '0'):
                    not_answered += 1
                else:
                    wrong += 1
            
            mcq_result = {'correct':correct,
                          'wrong':wrong,
                          'not answered':not_answered}
            print(mcq_result)
            marks = (int(mcq_result['correct'])*4)+(int(mcq_result['wrong'])*(-1))
            
            print(marks)
            mcq_flag = 1
            mcq_marks = marks
            ls = [mcq_flag, mcq_marks]
                
            #update the database
            update_data.update_marks(email, ls)
            main_question_frame.place_forget()
            dashboard(email)
            print(email)
            obj = [email, marks]
            
            
            
        def next_question():
            def submit_answer():
                examinee_ans.append(answer.get())
                print(examinee_ans)
                if(q_no != 4):
                    next_button['state'] = NORMAL
                else:
                    next_button['state'] = DISABLED
                    finish_button['state'] = NORMAL
                    
                submit_button['state'] = DISABLED
                b[q_no].configure(bg = 'blue')
            
            global q_no
            
            next_button['state'] = DISABLED
            
            submit_button = Button(main_question_frame,command = submit_answer,  text = "SAVE", bg = 'blue', fg = 'yellow', font = ('rockwell', 20))
            submit_button.place(x = 200, y = 400)
            
            q_no = q_no + 1
            
            question_label = Label(main_question_frame, text = mcq_questions[q_no], bg = "blue", fg = "white", font = ('rockwell', 16))
            question_label.place(x = 10, y = 10)
            
            answer = StringVar()
            answer.set(False)
        
            option_01 = Radiobutton(main_question_frame,text = "a. "+mcq_options[q_no][0], font = ('rockwell', 20), variable = answer, val = mcq_options[q_no][0])
            option_01.place(x = 10, y = 50)
                    
            option_02 = Radiobutton(main_question_frame,text = "b. "+mcq_options[q_no][1], font = ('rockwell', 20), variable = answer, val = mcq_options[q_no][1])
            option_02.place(x = 10, y = 100)
                
            option_03 = Radiobutton(main_question_frame,text = "c. "+mcq_options[q_no][2], font = ('rockwell', 20), variable = answer, val = mcq_options[q_no][2])
            option_03.place(x = 10, y = 150)
                
            option_04 = Radiobutton(main_question_frame,text = "d. "+mcq_options[q_no][3], font = ('rockwell', 20), variable = answer, val = mcq_options[q_no][3])
            option_04.place(x = 10, y = 200)
            
        
        
        start_frame.place_forget()
        T.place_forget()
        
        mcq_questions = ['1.About how much area of Antarctica is covered with ice?',
                         '2.There are seven continents in the world. In terms of area, the largest continent is _____ and the smallest continent is _____',
                         '3.In terms of population, the largest continent is _____, and the smallest continent is_____. ',
                         '4.There are five oceans in the world. The largest ocean is _____, and the smallest ocean is_____.',
                         '5.United Nations was formed on 24 October _____ in the United States']
        
        mcq_options = [['94%','96%','98%','100%'],
                       [ 'Asia, Antarctica', 'Asia, Australia', 'Africa, Antarctica', 'Africa, Australia'],
                       ['Asia, Antarctica', 'Asia, Australia', 'Africa, Antarctica', 'Africa, Australia'],
                       ['Atlantic, Antarctic', 'Atlantic, Arctic', 'Pacific, Antarctic', 'Pacific, Arctic'],
                       ['1943', '1944', '1945', '1946']
                       ]
        mcq_correct_ans = [3, 2, 1, 4, 3]
        
        examinee_ans = []
        
        main_question_frame = Frame(w, relief = SUNKEN, bg = 'green')
        main_question_frame.place(x = 100, y = 10, height = 500, width = 1200)
        
        next_button = Button(main_question_frame,command = next_question,  text = "NEXT", bg = 'blue', fg = 'yellow', font = ('rockwell', 20))
        next_button.place(x = 100, y = 400)
        
        
        finish_button = Button(main_question_frame,command = finish_mcq,  text = "Finish", bg = 'blue', fg = 'yellow', font = ('rockwell', 20))
        finish_button.place(x = 400, y = 400)
        finish_button['state'] = DISABLED
        
        next_question()
        
        next_button['state'] = DISABLED
        
        side_question_list_frame = Frame(main_question_frame, relief = SUNKEN, bg = 'orange')
        side_question_list_frame.place(x = 800, y = 100, height = 400, width = 300)
        
        question_list_label = Label(side_question_list_frame, text = "Questions are", font = ('rockwell', 18))
        question_list_label.pack(side = TOP)
        
        question_info_label1 = Label(side_question_list_frame, text = "Q", bg = 'red', fg = 'black', font = ('rockwell', 14))
        question_info_label12 = Label(side_question_list_frame, text = "Not answered", bg = 'white', fg = 'red', font = ('rockwell', 14))
        question_info_label2 = Label(side_question_list_frame, text = "Q", bg = 'blue', fg = 'black', font = ('rockwell', 14))
        question_info_label21 = Label(side_question_list_frame, text = "answered", bg = 'white', fg = 'blue', font = ('rockwell', 14))
        
        question_info_label1.place(x = 100, y = 300)
        question_info_label12.place(x = 130, y = 300)
        question_info_label2.place(x = 100, y = 330)
        question_info_label21.place(x = 130, y = 330)
        
        x_co = 30
        y_co = 100
        three_multiple = []
        b = []
        for j in range(1, 100):
            three_multiple.append(j*3)
        for i in range(1, len(mcq_questions)+1):
            b.append(Button(side_question_list_frame, bg = "red", font = ('rockwell', 18), text = "Q"+str(i)))
        
        for i in range(0, len(mcq_questions)):
            b[i].place(x = x_co, y = y_co)
            x_co = x_co + 70
            if i in three_multiple:
                y_co = y_co + 50
                x_co = 30
        
    dashboard_background_frame.place_forget()
    #w.attributes('-fullscreen', True)
    
    
    T = Text(w, bg = 'white', fg = 'black', font = ('rockwell', 20), height = 50, width = 50)
    fact = '''         *****RULES*****
                1.Exam consists of 5 mcq question
                2.Each exam has timer of 20 sec
                3.Each question carries 4 marks and 1 negative 
                  marking
                4.malpractices are seriously taken
                5.Must get greater than 3 marks to go to next 
                  stage (sbq)'''
    T.insert(tk.END, fact)
    T.place(x = 200, y = 10)
    
    start_frame = Frame(w, bg = 'white')
    start_frame.place(x = 500, y = 500, height = 200, width = 200)
    
    start_button = Button(start_frame,command = exam_start,  text = "START", bg = 'blue', fg = 'yellow', font = ('rockwell', 50))
    start_button.pack(side = BOTTOM)
    
def exam_start_sbq():
    global q_no
    q_no = -1
    def exam_start():
        try:
            #consider sbq_marks has plagarism
            ls_sbq_ans =  retreive_data.get_sbq_ans_data()
        except:
            ls_sbq_ans = []
            print("first user")
            
        def finish_sbq():
            def check_plagarism():
                finish_button['state'] = DISABLED
                plagarism_counter = 0
                
                print(len(ls_sbq_ans), len(ls_sbq_ans[0]))
                
                for i in range(len(ls_sbq_ans)):
                    for j in range(len(ls_sbq_ans[i])):
                        if(sbq_answers[j] == ls_sbq_ans[i][j]):
                            plagarism_counter += 1
                        
                print("plagarism_counter ", plagarism_counter)
                
                plagarism_percent = (plagarism_counter/(len(ls_sbq_ans)*5))*100
                
                print("plagarism_percent ", plagarism_percent)
                
                l = [1, plagarism_percent]
                update_data.update_marks_sbq(email, l)
                
            if(len(ls_sbq_ans)>0):
                check_plagarism()
            
            obj = [email, sbq_answers]
            send_obj = make_obj.prepare_sbq_obj(obj)
            
            insert_data.insert_data(send_obj, "project_01_data/sbq_marks")
            
            
            main_question_frame.place_forget()
            dashboard(email)
            
        def next_question():
            def submit_answer():
                question_label.place_forget()
                ans = sbq_answer.get("1.0", "end-1c")
                sbq_answers.append(ans)
                
                if(q_no != 4):
                    next_button['state'] = NORMAL
                else:
                    next_button['state'] = DISABLED
                    finish_button['state'] = NORMAL
                    
                submit_button['state'] = DISABLED
                b[q_no].configure(bg = 'blue')
            global q_no
            
            
            next_button['state'] = DISABLED
            
            submit_button = Button(main_question_frame,command = submit_answer,  text = "SAVE", bg = 'blue', fg = 'yellow', font = ('rockwell', 20))
            submit_button.place(x = 200, y = 400)
            
            q_no = q_no + 1
            
            question_label = Label(main_question_frame, text = sbq_questions[q_no], bg = "blue", fg = "white", font = ('rockwell', 16))
            question_label.place(x = 10, y = 10)
            
            sbq_answer = Text(main_question_frame)
            sbq_answer.place(x = 10, y = 70, height = 300)
            
            sbq_answer.delete('1.0', 'end')
            
        email = email_entry2.get()
        start_frame.place_forget()
        T.place_forget()
        
        sbq_questions = ['1.What is the worst thing you did as a kid?',
                         '2.Who Was Your Favorite Teacher? Why?',
                         '3.If You Could Time Travel, When Would You Go? and what would you do there?',
                         '4.If You Had To Pick A New Name For Yourself, What Name Would You Pick? why?',
                         '5.What Accomplishment Are You Most Proud Of?']
        sbq_answers = []
         
        main_question_frame = Frame(w, relief = SUNKEN, bg = 'green')
        main_question_frame.place(x = 100, y = 10, height = 500, width = 1200)
        
        next_button = Button(main_question_frame,command = next_question,  text = "NEXT", bg = 'blue', fg = 'yellow', font = ('rockwell', 20))
        next_button.place(x = 100, y = 400)
        
        
        finish_button = Button(main_question_frame,command = finish_sbq,  text = "Finish", bg = 'blue', fg = 'yellow', font = ('rockwell', 20))
        finish_button.place(x = 400, y = 400)
        finish_button['state'] = DISABLED
        
        next_question()
        
        next_button['state'] = DISABLED
        
        side_question_list_frame = Frame(main_question_frame, relief = SUNKEN, bg = 'orange')
        side_question_list_frame.place(x = 800, y = 100, height = 400, width = 300)
        
        question_list_label = Label(side_question_list_frame, text = "Questions are", font = ('rockwell', 18))
        question_list_label.pack(side = TOP)
        
        question_info_label1 = Label(side_question_list_frame, text = "Q", bg = 'red', fg = 'black', font = ('rockwell', 14))
        question_info_label12 = Label(side_question_list_frame, text = "Not answered", bg = 'white', fg = 'red', font = ('rockwell', 14))
        question_info_label2 = Label(side_question_list_frame, text = "Q", bg = 'blue', fg = 'black', font = ('rockwell', 14))
        question_info_label21 = Label(side_question_list_frame, text = "answered", bg = 'white', fg = 'blue', font = ('rockwell', 14))
        
        question_info_label1.place(x = 100, y = 300)
        question_info_label12.place(x = 130, y = 300)
        question_info_label2.place(x = 100, y = 330)
        question_info_label21.place(x = 130, y = 330)
        
        x_co = 30
        y_co = 100
        three_multiple = []
        b = []
        for j in range(1, 100):
            three_multiple.append(j*3)
        for i in range(1, len(sbq_questions)+1):
            b.append(Button(side_question_list_frame, bg = "red", font = ('rockwell', 18), text = "Q"+str(i)))
        
        for i in range(0, len(sbq_questions)):
            b[i].place(x = x_co, y = y_co)
            x_co = x_co + 70
            if i in three_multiple:
                y_co = y_co + 50
                x_co = 30
         
        
        
    dashboard_background_frame.place_forget()
    T = Text(w, bg = 'white', fg = 'black', font = ('rockwell', 20), height = 50, width = 50)
    fact = '''         *****RULES*****
                1.Exam consists of 5 sbq question
                2.Each exam has timer of 10 min
                3.Each question carries 10 marks
                  marking
                4.malpractices are seriously taken
                5.plagarism machine is included so
                  avoid plagaism'''
    T.insert(tk.END, fact)
    T.place(x = 200, y = 10)
    
    start_frame = Frame(w, bg = 'white')
    start_frame.place(x = 500, y = 500, height = 200, width = 200)
    
    start_button = Button(start_frame,command = exam_start,  text = "START", bg = 'blue', fg = 'yellow', font = ('rockwell', 50))
    start_button.pack(side = BOTTOM)
    
    
def dashboard(email):
    def logout():
        dashboard_background_frame.place_forget()
        dashboard_frame.place_forget()
        login_frame.place(x = 300, y = 50, height = 500, width = 800)
        
    print("inside dash")
    def edit_mode():
        def verify():
            answer = Security_entry.get()
            if(answer == q_dict[question]):
                messagebox.showinfo("info", "verified")
                update_button['state'] = NORMAL
            else:
                messagebox.showinfo("info", "try again")
        def update_data1():
            name1 = name_entry1.get()
            dob1 = dob_entry2.get()
            nation1 = nation_entry2.get()
            ls_u = [name1, dob1, nation1]
            update_data.update(email, ls_u)
            #bringing back the dashboard
            edit_frame.place_forget()
            dashboard_frame.place_forget()
            dashboard()
            
            
        exram_frame.place_forget()
            
        edit_frame = Frame(dashboard_background_frame, bg = "green", relief = SUNKEN)
        edit_frame.place(x = 550, y = 50, height = 500, width = 800)
            
        name_label2 = Label(edit_frame,text = "name", font = 30)
        name_label2.place(x = 200, y = 150)
        name_entry1 = Entry(edit_frame)
        name_entry1.insert(0, ls[0])
        name_entry1.place(x = 300, y = 150)
            
        dob_label2 = Label(edit_frame,text = "dob", font = 30)
        dob_label2.place(x = 200, y = 200)
        dob_entry2 = Entry(edit_frame)
        dob_entry2.insert(0, ls[1])
        dob_entry2.place(x = 300, y = 200)
            
        nation_label2 = Label(edit_frame,text = "nationality", font = 30)
        nation_label2.place(x = 200, y = 250)
        nation_entry2 = Entry(edit_frame)
        nation_entry2.insert(0, ls[2])
        nation_entry2.place(x = 300, y = 250)
            
        update_button = Button(edit_frame, command = update_data1, relief = SUNKEN, text = "UPDATE", bg = "yellow", font = 25)
        update_button.place(x = 400, y = 400)
            
        update_button['state'] = DISABLED
            
        q_dict = get_service_question.get_questions(email)
        #print(q_dict)
            
        question = random.choice(list(q_dict.keys()))
        Security_question_label = Label(edit_frame, text = question, font = 30)
        Security_question_label.place(x = 200, y =10)
            
        Security_entry = Entry(edit_frame)
        Security_entry.place(x = 500, y = 10)
            
        Verify_button = Button(edit_frame, command = verify, text = "Verify",relief = SUNKEN, bg = "yellow", font = 25)
        Verify_button.place(x = 500, y = 30)
        
        
            
    def open_cam():
        #step1 create an camera object
        cam_obj = cv2.VideoCapture(0) #0 represents the first (default) camera
        #step2 capture the image
        obj, frame = cam_obj.read()
        #step3 display the pic
        cv2.imshow('img', frame)
        path = "media/"+email+".jpg"
        cv2.imwrite(path, frame)
    
    singup_frame.place_forget()
    login_frame.place_forget()
    dashboard_background_frame.place(x = 0, y = 0, height = 1250, width = 2000)
    dashboard_frame.place(x = 10, y = 50, height = 500, width = 500)
    email_label = Label(dashboard_frame, text = "welcome "+email, bg = 'black', fg = 'white', font = ('arial', 16))
    email_label.place(x = 200, y = 10)
    
    logout_button = Button(dashboard_background_frame, text = "LOGOUT", font = ("rockwell", 15), command = logout, bg = "red", fg = "white");
    logout_button.place(x = 1150, y = 0)
    
    
    '''img = Image.open("media/"+email+".jpg")
    img = img.resize((150, 150))
    #img.show()

    
    #create a label
    img_label = Label(dashboard_frame, relief = SUNKEN)
    default_photo = ImageTk.PhotoImage(img)
    img_label.configure(image = default_photo)
    img_label1 = Label(dashboard_frame,  image = default_photo)
    img_label.place(x = 200, y = 40)
    img_label1.place(x = 200, y = 40)'''
    
    
    
    
    
    capture_dp = Button(dashboard_frame, text = "capture", command = open_cam)
    capture_dp.place(x = 200, y = 200)
    
    
    ls = retreive_data.get_data(email)
    
    
    print(ls)
        
    name_label1 = Label(dashboard_frame, font = 30)
    name_label1.configure(text = "name : " + ls[0])
    name_label1.place(x = 200, y = 300)
        
    dob_label1 = Label(dashboard_frame, font = 30)
    dob_label1.configure(text = "DOB : " + ls[1])
    dob_label1.place(x = 200, y = 330)
        
    nation_label1 = Label(dashboard_frame, font = 30)
    nation_label1.configure(text = "Nationality : " + ls[2])
    nation_label1.place(x = 200, y = 360)
        
    edit_button = Button(dashboard_frame, relief = SUNKEN, text = "EDIT", bg = "yellow", font = 25, command = edit_mode)
    edit_button.place(x = 400, y = 400)
        
    exram_frame.place(x = 600, y = 50, height = 600, width = 750)
    
    mcq_flag = ls[3]
    #mcq frame
    if(mcq_flag == 0):
        mcq_marks = 0
    else:
        mcq_marks = ls[4]
    
    sbq_flag = ls[5]
    if(sbq_flag == 0):
        marks1 = 0
    else:
        marks1 = ls[6]
        
    mcq_status_frame.place(x = 50, y = 50, height = 300, width = 250)
        
        
    mcq_label = Label(mcq_status_frame,  text = 'MCQ',font = ('rockwell',25), bg = 'blue', fg = 'white')
    mcq_label.place(x = 80, y = 10)
        
    start_button = Button(mcq_status_frame,text = "START", bg = 'blue', fg = 'yellow', font = ('rockwell', 25),command = exam_start_mcq)
    start_button.place(x = 50, y = 100)
    start_button['state'] = DISABLED
    
    if(mcq_flag == 0):
        start_button['state'] = NORMAL
        
    total_marks_label = Label(mcq_status_frame,  text = 'Total marks : '+str(mcq_marks),font = ('rockwell',20), bg = 'blue', fg = 'white')
    total_marks_label.place(x = 20, y = 200)
        
    sbq_status_frame.place(x = 450, y = 50, height = 300, width = 250)
        
    sbq_label = Label(sbq_status_frame, font = ('rockwell',25), text = 'SBQ', bg = 'blue', fg = 'white')
    sbq_label.place(x = 100, y = 10)
        
    start_button1 = Button(sbq_status_frame,text = "START", bg = 'blue', fg = 'yellow', font = ('rockwell', 25),command = exam_start_sbq)
    start_button1.place(x = 50, y = 100)
    start_button1['state'] = DISABLED
        
    total_marks_label1 = Label(sbq_status_frame,  text = 'Total marks : '+str(marks1),font = ('rockwell',20), bg = 'blue', fg = 'white')
    total_marks_label1.place(x = 20, y = 200)
        
    generate_result_button = Button(exram_frame,text = "Generate Result", command = generate_result, bg = 'blue', fg = 'yellow', font = ('rockwell', 30))
    generate_result_button.place(x = 200, y = 400)
    
    if(ls[7] == 1):
        view_pdf_button = Button(exram_frame, text = "View result", bg = 'blue', fg = 'yellow', font = ('rockwell', 30))
        view_pdf_button.place(x = 200, y = 500)
        
    if(int(mcq_marks) > 3 and sbq_flag == 0):
        start_button1['state'] = NORMAL
        
    
    path = "media/"+email+".jpg"
    photo = PhotoImage(file=path)
    photo_label = Label(image = photo)
    photo_label.place(x = 200, y = 40)
    
def captcha():
    def validate():
        rhsvalue = rhs.get()
        lhsvalue = lhs.get()
        opvalue = opr.get()

        print(lhsvalue, opvalue, rhsvalue)
        result = 9999
    
        if opvalue == '+':
            result = int(lhsvalue) + int(rhsvalue)
        elif opvalue == '-':
            result = int(lhsvalue) - int(rhsvalue)
        else:
            result =    int(lhsvalue) * int(rhsvalue)
    
        user_entry = int(entry.get())
    
        if (user_entry == result):
            messagebox.showinfo("Captcha entered :", " valid :>")
            login_button['state'] = NORMAL
        else:
            messagebox.showinfo("Captcha entered :", " invalid :>")
    def refresh():
        lhs.set(str(random.randint(1, 10)))
        rhs.set(str(random.randint(1, 10)))
        op = random.choice('+-*')
        opr.set(op)
        expression = lhs.get() + opr.get() + rhs.get()
        label1.configure(text = expression)
    label1 = Label(login_frame, font = ('arial', 16), bd = 10, bg = "black", fg = "white")
    label1.place(x = 200, y = 250)
    #generate random number
    #random1 = str(random.randint(1000, 9999))
    lhs = StringVar()
    lhs.set(str(random.randint(1, 10)))
    rhs = StringVar()
    rhs.set(str(random.randint(1, 10)))

    opr = StringVar()
    op = random.choice('+-*')
    opr.set(op)
    expression = lhs.get() + opr.get() + rhs.get()

    label1.configure(text = expression)
    refbutton = Button(login_frame,text = "refresh",relief = SUNKEN, bg = "yellow", fg = "blue", font = ("rockwell", 16), command = refresh)
    #bg=background; fg=foreground ;arial is font family name
    refbutton.place(x=300,y=300)#if we want the button to be visible#width to specify the width of the button

    entry = Entry(login_frame)#show is used for print any symbol for password
    entry.place(x=350,y=250)

    validate_b = Button(login_frame, text = "Validate",  relief = SUNKEN, bg = "yellow", fg = "blue", font = ("rockwell", 16), command = validate)
    validate_b.place(x = 420,y = 300)
def check_credentials():
    email = email_entry2.get()
    passw = pass_entry.get()
    
    r_status, value = connection.connect()
    if( r_status != True):
        messagebox.showwarning("Eror", "Connection to database")
    else:
        try:
            #step 5 create an object
            authentication_obj = value.auth()
            authentication_obj.sign_in_with_email_and_password(email, passw)
            messagebox.showinfo("info", "login done")
            login_frame.place_forget()
            singup_frame.place_forget()
            update_login_time.f_log(email)
            dashboard(email)
            
        except:
            messagebox.showerror("error","invalid email or password")
            login_frame.place_forget()
            singup_frame.place_forget()
            #update_login_time.f_log(email)
            dashboard(email)
    
    
def activate_singup():
    login_frame.place_forget()
    singup_frame.place(x = 300, y = 50, height = 500, width = 800)
    
def security():
    def security_list_adder():
        global security_qa
        security_qa = {s_combobox.get() : Entry_01.get(),
                       s_combobox1.get() : Entry_02.get(),
                       s_combobox2.get() : Entry_03.get(),
                       s_combobox3.get() : Entry_04.get(),
                       s_combobox4.get() : Entry_05.get()
            }
        print(security_qa)
        
        #hide the security and enable singup frame
        security_frame.place_forget()
        singup_frame.place(x = 300, y = 50, height = 500, width = 800)
        
    #verify if email is entered or not
    email = email_entry.get()
    if(email == ""):
        messagebox.showerror("error", "email not entered")
    else:
        singup_frame.place_forget()
        security_frame = Frame(w, bg = 'green', relief = SUNKEN)
        security_frame.place(x = 300, y = 50, height = 500, width = 800)
        
        security_label = Label(security_frame, text = "Security", bg = 'yellow', fg = 'black', font = ('arial', 20))
        security_label.place(x = 50, y = 50)
        
        #create 5 combobox
        s_combobox = ttk.Combobox(security_frame)#to select multivalues
        s_combobox['value']=('What is your pet name?', 'Where were you born?','What is the name of your school?','What is yur favorite food?', 'What is your favorite color')#enter options to be displayed
        s_combobox.current(0)#to select the value defaultly
        s_combobox.place(x=200,y=150, width = 180)
        
        Entry_01 = Entry(security_frame)
        Entry_01.place(x = 400, y = 150)
        
        s_combobox1 = ttk.Combobox(security_frame)#to select multivalues
        s_combobox1['value']=('What is your pet name?', 'Where were you born?','What is the name of your school?','What is yur favorite food?', 'What is your favorite color')#enter options to be displayed
        s_combobox1.current(1)#to select the value defaultly
        s_combobox1.place(x=200,y=200, width = 180)
        
        Entry_02 = Entry(security_frame)
        Entry_02.place(x = 400, y = 200)
        
        s_combobox2 = ttk.Combobox(security_frame)#to select multivalues
        s_combobox2['value']=('What is your pet name?', 'Where were you born?','What is the name of your school?','What is yur favorite food?', 'What is your favorite color')#enter options to be displayed
        s_combobox2.current(2)#to select the value defaultly
        s_combobox2.place(x=200,y=250, width = 180)
        
        Entry_03 = Entry(security_frame)
        Entry_03.place(x = 400, y = 250)
        
        s_combobox3 = ttk.Combobox(security_frame)#to select multivalues
        s_combobox3['value']=('What is your pet name?', 'Where were you born?','What is the name of your school?','What is yur favorite food?', 'What is your favorite color')#enter options to be displayed
        s_combobox3.current(3)#to select the value defaultly
        s_combobox3.place(x=200,y=300, width = 180)
        
        Entry_04 = Entry(security_frame)
        Entry_04.place(x = 400, y = 300)
        
        s_combobox4 = ttk.Combobox(security_frame)#to select multivalues
        s_combobox4['value']=('What is your pet name?', 'Where were you born?','What is the name of your school?','What is yur favorite food?', 'What is your favorite color')#enter options to be displayed
        s_combobox4.current(4)#to select the value defaultly
        s_combobox4.place(x=200,y=350, width = 180)
        
        Entry_05 = Entry(security_frame)
        Entry_05.place(x = 400, y = 350)
        
        submit_button1 = Button(security_frame, command = security_list_adder, text = "Submit", relief = SUNKEN, bg = "yellow", fg = "blue", font = ("rockwell", 20))
        submit_button1.place(x = 350, y = 420)
        
        submit_button['state'] = NORMAL
        
        Security.secure()
    

def upload():
    r_status, value = connection.connect()
    if(r_status):
        email = email_entry.get()
        img_selected = askopenfilename(initialdir = "",
                                       filetype = (('imgfile','*.jpg'), ('allfile', '*.*')),
                                       title = "choose the image") 
        
        
        upload_button['state'] = DISABLED
        
        img = Image.open(img_selected)
        img.save("media/"+email+".jpg")
        
        image_path.set(img_selected)
        #create an storage object
        store_obj = value.storage()
        
        #inserting the image into database
        store_obj.child(img_selected).put(img_selected)
        print("Image inserted")
    else:
        print("connection to storage failed")
def read_data():
    
    try:
        #password generation
        ## characters to generate password from
        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        
        length = 10
    
    	## shuffling the characters
        random.shuffle(characters)
    	
    	## picking random characters from the list
        password = []
        for i in range(length):
            password.append(random.choice(characters))
    
    	## shuffling the resultant password
        random.shuffle(password)
    
    	## converting the list to string
    	## printing the list
        passw = "".join(password)
    
        print(passw)
        
        #Fetch all the derails 
        
        email = email_entry.get()
        name = name_entry.get()
        nationality = combobox.get()
        dob = date.get()
        mcq_flag = 0
        mcq_marks = 0
        sbq_flag = 0
        sbq_marks = 0
        generate_result_flag = 0
        
        #image_path.set(email+".jpg")
        obj = [email, name, nationality, dob, mcq_flag, mcq_marks, sbq_flag, sbq_marks, generate_result_flag]
        
        #step3 call create acoount function(userid,password)
        if(create_account.Create(email, passw) == True):
            messagebox.showinfo("info", "account created")
            
            #insert data into database
            #prepare the object
            obtained_data = make_obj.prepare_obj(obj)
            obtained_data.update(security_qa)
            
            if(insert_data.insert_data(obtained_data, "project_01_data/personal_details")):
                print("data inserted")
                r_status, value = connection.connect()
                if(r_status):
                    singup_frame.place_forget()
                    login_frame.place(x = 300, y = 50, height = 500, width = 800)
                     
                else:
                    print("Connection not done")
            else:
                print("data not inserted")
            
            
    except Exception as e:
        print(e)
        messagebox.showerror("error", "account not created : ")
        
        
w = Tk()
w.geometry('1024x1024')
w.state('zoomed')
#w.attributes('-fullscreen', True) #disables all buttons
w.configure(background = 'dark green')

singup_frame = Frame(w, bg = 'green', relief = SUNKEN)
singup_frame.place(x = 300, y = 50, height = 500, width = 800)

singup_label = Label(singup_frame, text = "Singup", bg = 'yellow', fg = 'black', font = ('arial', 20))
singup_label.place(x = 300, y = 0)

email_label = Label(singup_frame, text = "Email", bg = 'black', fg = 'white', font = ('arial', 16))
email_label.place(x = 200, y = 150)

email_entry = Entry(singup_frame)
email_entry.place(x = 350, y = 150)

name_label = Label(singup_frame, text = "Name", bg = 'black', fg = 'white', font = ('arial', 16))
name_label.place(x = 200, y = 200)

name_entry = Entry(singup_frame)
name_entry.place(x = 350, y = 200)

nation_label = Label(singup_frame, text = "Nationality", bg = 'black', fg = 'white', font = ('arial', 16))
nation_label.place(x = 200, y = 250)

c_msg = "Indian"
#create a combobox
combobox = ttk.Combobox(singup_frame, textvar = c_msg)#to select multivalues
combobox['value']=('Indian', 'Chinise','Japanese','USA')#enter options to be displayed
combobox.current(0)#to select the value defaultly
combobox.place(x=350,y=250)

dob_label = Label(singup_frame, text = "DOB", bg = 'black', fg = 'white', font = ('arial', 16))
dob_label.place(x = 200, y = 300)
date = DateEntry(singup_frame)
date.place(x = 350, y = 300)

upload_label = Label(singup_frame,  text = "Upload image", bg = 'black', fg = 'white', font = ('arial', 16))
upload_label.place(x = 200, y = 350)
upload_button = Button(singup_frame, command =upload,text = "Upload", relief = SUNKEN, bg = "yellow", fg = "black", font = ("rockwell", 16))
upload_button.place(x = 350, y = 350)

submit_button = Button(singup_frame,command = read_data, text = "Submit", relief = SUNKEN, bg = "yellow", fg = "blue", font = ("rockwell", 20))
submit_button.place(x = 350, y = 400)
submit_button['state'] = DISABLED

security_button = Button(singup_frame,command = security, text = "Security", relief = SUNKEN, bg = "yellow", fg = "blue", font = ("rockwell", 20))
security_button.place(x = 350, y = 450)

image_path = StringVar()

singup_frame.place_forget()

#Login frame
login_frame = Frame(w, bg = 'green', relief = SUNKEN)
login_frame.place(x = 300, y = 50, height = 500, width = 800)

email_label = Label(login_frame, text = "Email", bg = 'black', fg = 'white', font = ('arial', 16))
email_label.place(x = 200, y = 150)

email_entry2 = Entry(login_frame)
email_entry2.place(x = 350, y = 150)

pass_label = Label(login_frame, text = "Password", bg = 'black', fg = 'white', font = ('arial', 16))
pass_label.place(x = 200, y = 200)

pass_entry = Entry(login_frame)
pass_entry.place(x = 350, y = 200)

login_button = Button(login_frame,command = check_credentials, text = "Login", relief = SUNKEN, bg = "yellow", fg = "blue", font = ("rockwell", 20))
login_button.place(x = 200, y = 400)

#login_button['state'] = DISABLED
#captcha
captcha()

new_user_button = Button(login_frame, command = activate_singup, text = "New User", relief = SUNKEN, bg = "yellow", fg = "blue", font = ("rockwell", 20))
new_user_button.place(x = 350, y = 400)

dashboard_background_frame = Frame(w, bg = 'black')
dashboard_background_frame.place(x = 0, y = 0, height = 1250, width = 2000)
dashboard_frame = Frame(dashboard_background_frame, bg = 'green', relief = SUNKEN)
dashboard_frame.place(x = 10, y = 50, height = 500, width = 500)

dashboard_background_frame.place_forget()
dashboard_frame.place_forget()

#Exam frame
exram_frame = Frame(dashboard_background_frame, bg = 'green', relief = SUNKEN)
exram_frame.place(x = 200, y = 50, height = 500, width = 800)
exram_frame.place_forget()

sbq_status_frame = Frame(exram_frame, bg = 'blue', relief = SUNKEN)
sbq_status_frame.place(x = 450, y = 50, height = 300, width = 250)
sbq_status_frame.place_forget()

mcq_status_frame = Frame(exram_frame, bg = 'blue', relief = SUNKEN)
mcq_status_frame.place(x = 50, y = 50, height = 300, width = 250)
mcq_status_frame.place_forget()

user_id = StringVar()

w.mainloop()