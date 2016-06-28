import requests
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
    info = l[24]
    info = info.split()
    return info