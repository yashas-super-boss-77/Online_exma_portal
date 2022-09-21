def prepare_obj(obj):
    data = {'email': obj[0],
            'name': obj[1],
            'nationality': obj[2],
            'dob': obj[3],
            'mcq_flag': obj[4],
            'mcq_marks': obj[5],
            'sbq_flag': obj[6],
            'sbq_marks': obj[7],
            'generate_result_flag': obj[8]
            }
    print(data)
    return data
def prepare_flog_obj(obj):
    data = {'email':obj[0],
            'login_time': obj[1],
            'login_date': obj[2]
            }
    return data
def prepare_sbq_obj(obj):
    data = {'email':obj[0],
            'answers':obj[1]}
    return data
