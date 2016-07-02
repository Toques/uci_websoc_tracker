import requests
import re
from twilio.rest import TwilioRestClient

def main():
    
    r = requests.post('https://www.reg.uci.edu/perl/WebSoc', data ={'Breadth':'ANY','CancelledCourse':'Exclude','ClassType':'ALL',
                        'CourseCodes':'36680','Dept':'ALL','Division':'ALL','FontSize':'100',
                       'FullCourses':'ANY', 'Submit':'Display Text Results', 'YearTerm':'2016-14'})

    text = r.text
    l = text.split('\n')
    header = l[23].strip()
    data = l[24].strip()
    #print(header)
    #print(data)
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
    print(info)
    # info = info.split()
    # length = len(info)
    # courseCode = int(info[0])
    # maxEnrolled = int(info[length-5-1])
    # enrolled = int(info[length-4-1])
    # waitlist = info[length-3-1]
    # print(info)
    # print(courseCode)
    # print(maxEnrolled)
    # print(enrolled)
    # print(waitlist)
    # ACCOUNT_SID = "AC8563bbddc734434f3f0598d90f7c23c6"
    # AUTH_TOKEN = "ead2b8568678dda16eb0380f80cdf7fa"
    #
    # client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    #
    # if (enrolled<maxEnrolled):
    #     sms = client.messages.create(to = "+14158302607",
    #                            from_="+15622000373",
    #                         body = "Alert: Course enrolled < maxium enrollment:\n"+
    #                                  str(enrolled) + " : " + str(maxEnrolled))
    # print(sms.sid)
if __name__ == "__main__":
    main()
