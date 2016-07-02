import requests
import re
from .models import Course
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
def request_websoc(course_code, **kwargs):
    data = {'Breadth': 'ANY', 'CancelledCourse': 'Exclude', 'ClassType': 'ALL',
            'CourseCodes': course_code, 'Dept': 'ALL', 'Division': 'ALL', 'FontSize': '100',
            'FullCourses': 'ANY', 'Submit': 'Display Text Results', 'YearTerm': '2016-14'}
    for key,value in kwargs.items():
        data[key] = value
    r = requests.post('https://www.reg.uci.edu/perl/WebSoc',
                      data= data)
    text = r.text
    l = text.split('\n')
    header = l[23].strip()
    data = l[24].strip()

    info = {}
    p = re.compile('\w+\s*')
    header_list = p.findall(header)

    data_index = 0
    for header in header_list:
        header_len = len(header)

        column_data = data[data_index:data_index+header_len]
        data_index+= header_len
        #print(column_data)
        info[header.strip()] = column_data.strip()
    return info

def save_course_data(course, info):
    # length = len(info)
    # max_enroll = int(info[length - 4 - 1])
    # enrolled = int(info[length - 3 - 1])
    # waitlist = info[length - 2 - 1]
    # restr = info[length - 1 - 1]
    # status = info[length - 1]

    course.max_enrollment = int(info.get('Max','0'))
    course.current_enrollment = int(info.get('Enr','0'))
    course.wait_list = int(info.get('Wl','0'))
    course.restrictions = info.get('Restr','')
    course.status = info.get('Status','')

    course.save()

def notify(userProfile, msg):
    ACCOUNT_SID = "AC8563bbddc734434f3f0598d90f7c23c6"
    AUTH_TOKEN = "ead2b8568678dda16eb0380f80cdf7fa"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    try:
        sms = client.messages.create(to=userProfile.phone_number,
                                    from_="+15622000373",
                                    body=msg)
    except(TwilioRestException):
        pass
