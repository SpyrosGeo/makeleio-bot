from datetime import date
import calendar
def findDay():
    today = date.today()
    # today = today.strftime("%m/%d/%Y")
    # currentDate = today.split("/")
    # currDate = " ".join(currentDate)
    return today.strftime("%A")
def getDate():
    today = date.today()
    todayDate = today.strftime("%Y%m%d")
    return todayDate[2:]


