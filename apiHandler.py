import uuid
from datetime import datetime

class Appointment:
    def __init__(self, customerId:str, customerName:str, customerPhone:str,\
        orderId:str, status:str, dateAndTime:str):
            self.date_time = datetime.strptime(dateAndTime, '%m%d%y %H:%M')
            self.appontment = {
                "appId": str(uuid.uuid4()),
                "customerId": customerId,
                "customerName":customerName,
                "customerPhone": customerPhone,
                "orderId": orderId,
                "status": status,
                "date": dateAndTime.split(" ")[0],
                "time": dateAndTime.split(" ")[1]
            }

    def getDate(self) -> str:
        return self.appontment["date"]
    def getTime(self) -> str:
        return self.appontment["time"]
    def getId(self) -> str:
        return self.appontment["appId"]
    def setDateTime(self, newDateTime):
        self.appontment["date"] = newDateTime.split(" ")[0]
        self.appontment["time"] = newDateTime.split(" ")[1]
    def setStatus(self, newStatus):
        self.appontment["status"] = newStatus
    def setOrderId(self,newOrderId):
        self.appontment["orderId"] = newOrderId
    def getAppJson(self):
        return self.appontment
        
               
class DailySchedule:
    def __init__(self, date):
        self.date = date
        self.dailySchedule = self.__dailyScheduleFactory()
    def __dailyScheduleFactory(self):
        self.tempObj = {}
        hours = ["9", "10","11", "12", "13", "14", "15", "16", "17"]
        mins = ["00", "15", "30", "45"]
        for hour in hours:
            for min in mins:
                self.tempObj[hour+":"+min] = None
        return self.tempObj
    def setAppointment(self, appObj : Appointment):
        if appObj.getDate() == self.date and \
            appObj.getTime() in self.dailySchedule and \
                not self.dailySchedule[appObj.getTime()]:
            self.dailySchedule[appObj.getTime()] = appObj
            return True
        return False
    def getScheduleJson(self):
        self.tempDict={}
        for key in self.dailySchedule :
            if self.dailySchedule[key]:
                self.tempDict[key] = self.dailySchedule[key].getAppJson()
            else:
                self.tempDict[key] = None
        return self.tempDict
    def getAppByTime(self, time):
            return self.dailySchedule[time]
    def deleteApp(self, time):
        self.dailySchedule[time] = None


class AppContainer:
    container = {}
    def __init__(self, name):
        self.name = name
    def putDailySchedule(self, scheduleObj : DailySchedule):
        self.container[scheduleObj.date] = scheduleObj
    def keyExist(self, key : str):
        if(key in self.container):
            return True
        return False
    def getScheduleObj(self, date : str) -> DailySchedule:
        if self.keyExist(date):
            return self.container[date]

