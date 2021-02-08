import requests
import datetime
import re

BASE = "http://127.0.0.1:5000"
def getDate():
    date = datetime.datetime.now()
    year = date.strftime("%y")
    month = date.strftime("%m")
    day = date.strftime("%d")
    hour = date.strftime("%I")
    minute = date.strftime("%M")
    AP = date.strftime("%p")
    string = "{0}%{1}%{2}%%{3}%{4}%{5}".format(year,month,day,hour,minute,AP)
    return  string


def parseDate(date):
    pattern = "%"
    string = re.sub("%", ' ', date)
    #print(string)
    string = string[3:5] + '/' + string[6:8]+ " " +string[10:12]+":"+string[13:]
    return string


"""def getURL(name,pts):
    user = name + 
    return BASE + user + str
"""
if True:
    str = getDate()
    #p = parseDate(str)
    response = requests.post(BASE + "/Dannon/300/" + str)
    str = getDate()
    p = parseDate(str)
    response = requests.post(BASE + "/Unilever/200/" + str)
    str = getDate()
    p = parseDate(str)
    response = requests.post(BASE + "/Dannon/-200/"  + str)
    str = getDate()
    p = parseDate(str)
    response = requests.post(BASE + "/Miller/10000/"  + str)
    str = getDate()
    p = parseDate(str)
    response = requests.post(BASE + "/Dannon/1000/"  + str)
    print(response.json())
    user_data = requests.get(BASE + "/")
    print(user_data.json())

if False:
    user_data = requests.get(BASE + "/")
    print("User Data")
    print(user_data.json())

if False:
    alltrs = requests.get(BASE + '/transactions')
    print("All Transactions")
    print(alltrs.json())

if False:
    deductions = requests.get(BASE + '/deductions')
    print("Deductions")
    print(deductions.json())

if False:
    for i in range(1):
        deduct_pts= requests.get(BASE + '/deduct/5000')
        #print("After Deduction")
        print(deduct_pts.json())

if False:
    user_data = requests.get(BASE + "/points")
    #print("User Data after Deductions")
    print(user_data.json())
