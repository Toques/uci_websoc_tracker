import requests

def main():
    r = requests.post('https://www.reg.uci.edu/perl/WebSoc', data =
                      {'Breadth':'ANY','CancelledCourse':'Exclude','ClassType':'ALL',
                       'CourseCodes':'36680','Dept':'ALL','Division':'ALL','FontSize':'100',
                       'FullCourses':'ANY', 'Submit':'Display Text Results', 'YearTerm':'2016-14'})
    text = r.text
    l = text.split('\n')
    info = l[24]
    info = info.split()
    length = len(info)
    courseCode = info[0]
    maxEnrolled = info[length-5-1]
    enrolled = info[length-4-1]
    waitlist = info[length-3-1]

    print(courseCode)
    print(maxEnrolled)
    print(enrolled)
    print(waitlist)
if __name__ == "__main__":
    main()
