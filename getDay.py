from datetime import date
import calendar
def findDay():    
    today = date.today()
    # today = today.strftime("%m/%d/%Y")
    # currentDate = today.split("/")
    # currDate = " ".join(currentDate)
    return today.strftime("%A")
