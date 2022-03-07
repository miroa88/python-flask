
# import math
# from flask import Flask
# app = Flask(__name__)
# @app.route('/hello/', methods=['GET', 'POST'])
# def welcome():
#     return "Hello World!"

# @app.route('/<int:number>')
# def getArea(number):
#     return "The circle area is " + str(number * number * math.pi)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

# name = 0
# def func():
    # name = input("enter your name?")
    # print("hello world")
    # global name
    # name = "miro"
    # print("hello " , name)


# if __name__ == '__main__':
#     func()

# func()
# print("hello " , name)

# del name
# print(name)
# def power(num, x=1):
#     result = 1
#     for i in range(x):
#         result = result * num
#     return result

# print(power(2))
# print(power(2,3))
# print(power(x=5, num=2))

# def multi_add(*args):
#     result = 0
#     for arg in args:
#         result = result + arg
#     return result

# print(multi_add(1,2,3,4,5))


# if (False):
#     a=1
# elif(False):
#     a=2
# else:
#     a=3

# # num = "it is positive" if (a < 0) else "x is negative"
# while (a<5):
#     print(a)
#     a = a + 1

# for x in range(5, 10):
#     print(x)

# arr = [1,22,3,4,6,73,3]
# for num in arr:
#     print(num)

# for i,num in enumerate(arr):
#     print(str(i) + " " + str(num))

# class myClass():
#     def meth1(self):
#         print("method 1")
#     def meth2(self, num):
#         print("from method 2", num)

# def main():
#     c = myClass()
#     c.meth1()
#     c.meth2("mirro")
#     c2=anotherClass()
#     c2.meth1()
#     c2.meth2("anet")

# class anotherClass(myClass):
#     def meth1(self):
#         myClass.meth1(self)
#         print("method one from another class")

#     def meth2(self, num):
#         print("from anothe class method 2", num)

# if __name__ == '__main__':
#     main()


# class Simple():
#     def Add(self, x, y):
#         return x+y

# class Advanced(Simple):
#   def Inverse(self,x,y):
#     return (1/Simple.Add(self,x,y))


# s = Simple()
# print(s.Add(1,4))

# s2 = Advanced()
# print(s2.Inverse(1,4))

# def inc(a,b=1):
#     return(a+b)
# a=inc(1)
# a=inc(a,a)
# print(a)

# class Person():
#   def __initialize__(self, name, age, sex):
#     self.name = name
#     self.age = age
#     self.sex = sex   

# p = Person()
# p.__initialize__('Miro', 33, "male")
# print(p.name)
# print(p.age)
# print(p.sex)

#--------------------------------------------------------------------------------------
# from datetime import *
# today = date.today() #datetime.date(datetime.now())

# print(today)
# print("todays date: ", today.day,today.month, today.year)

# print(today.weekday())

# today = datetime.now()
# print(today)
# t = datetime.time(today)
# print(t)


# now = datetime.now()
# print(now.strftime("weekday, day of mmonth, month, year: %a, %d %B, %y"))

#local
# print(now.strftime("local date: %c"))
# print(now.strftime("local date: %x"))
# print(now.strftime("local time: %X"))

# print(now.strftime("day-str, month-str, day-int, year-int: %A %B %d, %Y"))

# print(now.strftime("current time: %I:%M:%S %p"))
# print(now.strftime("24-hours: %H:%M"))
# from datetime import date, datetime
# from datetime import timedelta

# print(timedelta(days=370, hours=5, minutes=1))

# now = datetime.now()

# print("one years from now: " + str(now + timedelta(days=365)))

# today = date.today()
# miro = date(today.year, 5, 25)

# if miro < today:
#     print("Miro's birthday already went by %d days this year" %(today - miro).days)
#     miro = miro.replace(year = today.year + 1 )

# time_left = miro - today
# print("%d days to Miro's birthday" %time_left.days)

#--------------------------------------------------------------------------------------
# import calendar
# c = calendar.TextCalendar(calendar.SUNDAY)
# st = c.formatmonth(2022, 5, 0, 0)
# print(st)
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2022, 5)
# print(st)

# for i in c.itermonthdays(2022, 5):
#     print(i)

# for name in calendar.month_abbr:
#     print(name)

# for day in calendar.day_name:
#     print(day)

# for m in range(1, 13):
#     month = calendar.monthcalendar(2022, m)
#     weekone = month[0] #first week of month
#     weektwo = month[1] #second week of month

#     if weekone[calendar.SUNDAY] != 0:
#         day = weekone[calendar.SUNDAY]
#     else:
#         day = weektwo[calendar.SUNDAY]

#     print(" first Sunday of the month %9s is on %2d" %(calendar.month_name[m], day))

# today = date.today()
# print(today.weekday())

# from datetime import datetime
# # now=datetime.now()
# # print(now.strftime("%d-%b-%Y %h:%m:%S")) #06-Mar-2022 Mar:03:55

# now=datetime.now()
# print(now.strftime("%d-%b-%Y %H:%M:%S")) #06-Mar-2022 21:17:15

# from datetime import *
# now = datetime.now()
# print(now + timedelta(days=1)) #2022-03-06 21:23:30.310738


# today=date.today()
# print(today + timedelta(days=1)) #2022-03-06

#-------------------------------------------------------------------------
# f = open('textfile.txt', 'w+') # + means if it doesn't exist create it

# for i in range(10):
#     f.write(str(i) + ") this is cool!\n")

# f.close()

# f = open('textfile.txt', 'a') # + means if it doesn't exist create it

# for i in range(10):
#     f.write(str(i) + ") this is cool!\n")

# f.close()

# f = open('textfile.txt', 'r') # + means if it doesn't exist create it

# if f.mode == 'r':
#     contents = f.read()
# print(contents)

# if f.mode == 'r':
#     fl = f.readlines()
#     for x in fl:
#         print(x)
    
#-------------------------------------------------------------------------------
# import os #operating system
# from os import path
# import datetime
# from datetime import date, time, timedelta
# import time

# print(os.name)
# print("Item exists: " + str(path.exists("textfile.txt")))
# print("Item is a file: " + str(path.isfile("textfile.txt")))
# print("Item is a directory: " + str(path.isdir("textfile.txt")))

# print("item path " + str(path.realpath("textfile.txt")))
# print("item path and name " + str(path.split(path.realpath("textfile.txt"))))

# t=time.ctime(path.getatime("textfile.txt"))
# print(t)
# print(datetime.datetime.fromtimestamp(path.getatime("textfile.txt"))) #two different ways to get the time of last modification of a file

#how long ago the item was modified
# td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getatime("textfile.txt"))
# print("its been " + str(td) + " since last modification")
# print(td.total_seconds())

#------------------------------------------------------------------------------------------------
# import os
# from os import path
# import shutil #working with filesystem shell methods
# import datetime

# if path.exists("textfile.txt"):
#     src = path.realpath("textfile.txt")
#     dst = src + ".bak"
#     shutil.copy(src, dst)

# td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getatime("textfile.txt"))
# print("its been " + str(td) + " since last modification")
# print("-----------------------------------------")
# td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getatime("textfile.txt.bak"))
# print("its been " + str(td) + " since last modification")

# if path.exists("textfile.txt"):
#     src = path.realpath("textfile.txt")
#     dst = src + ".bak"
#     shutil.copystat(src, dst)

# td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getatime("textfile.txt"))
# print("its been " + str(td) + " since last modification")
# print("-----------------------------------------")
# td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getatime("textfile.txt.bak"))
# print("its been " + str(td) + " since last modification")

# os.rename("text.txt", "textfile.txt")
#-----------------------------------------------------------------------
# import os
# from os import path
# import shutil #working with filesystem shell methods
# import datetime
# from shutil import make_archive
# from zipfile import ZipFile
# if path.exists("textfile.txt"):
#     src = path.realpath("textfile.txt")
# root_dir, tail = path.split(src)
# # shutil.make_archive("archive", "zip", root_dir) #making a zip file
# with ZipFile("textZip.zip", "w") as newzip:
#     newzip.write("textfile.txt")
#     newzip.write("textfile.txt.bak")

# from pyexpat import features
# import urllib.request
# import json
# webUrl = urllib.request.urlopen("http://www.google.com")

# print("result code: " + str(webUrl.getcode())) #result code: 200 means the request has succeeded.
# data = webUrl.read()
# print(data)
#-----------------------------------------------------------------------------------------------------------
# def printResult(data):
#     theJSON = json.loads(data)
    # if "title" in theJSON["metadata"]:
    #     print(theJSON["metadata"]["title"]) #https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
    # if "count" in theJSON["metadata"]:
    #     print(theJSON["metadata"]["count"])
    # for i in theJSON["features"]:
    #     print(i["properties"]["place"])
    # for i in theJSON["features"]:
    #     if i["properties"]["mag"] >= 6.0:
    #         print("%2.1f" %i["properties"]["mag"], i["properties"]["place"] )
    # for i in theJSON["features"]:
    #     if 'CA' in i["properties"]["place"]:
    #         print("%2.1f" %i["properties"]["mag"], i["properties"]["place"] )

# url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

# webUrl = urllib.request.urlopen(url)
# # print("result " + str(webUrl.getcode()))
# if(webUrl.getcode() == 200):
#     data = webUrl.read()
#     # print(data)
#     printResult(data)
# else:
#     print("some err happened")
#--------------------------------------------------------------------
# from html.parser import HTMLParser
# metacount = 0
# class MyHTMLParser(HTMLParser):
    # def handle_comment(self, data):
    #     print("Encountered comment: ", data)
    #     position = self.getpos()
    #     print("atline " , position[0], " position ", position[1])
    #     print("\n")
    # def handle_starttag(self, tag, attrs):
    #     global metacount
    #     if tag == 'meta':
    #         metacount+=1
    #     print("Encountered tag: ", tag)
    #     position = self.getpos()
    #     print("atline " , position[0], " position ", position[1])
    #     if attrs.__len__() > 0:
    #         print("attributes:")
    #         for a in attrs:
    #             print(a[0], " = ", a[1])
    #         print("\n")
    # def handle_endtag(self, tag):
    #     print("Encountered tag: ", tag)
    #     position = self.getpos()
    #     print("atline " , position[0], " position ", position[1])
    #     print('\n')
    # def handle_data(self, data: str):
    #     if data.isspace():
    #         return
    #     print("Encountered data: ", data)
    #     position = self.getpos()
    #     print("atline " , position[0], " position ", position[1])
    #     print("\n")
    
# def main():
#     parser = MyHTMLParser();
#     f = open("samplehtml.html")
#     if f.mode == 'r':
#         contents = f.read()
#         parser.feed(contents)
#     print("number of meta tag" , metacount)
    
# if __name__ == '__main__':
#     main()
#-----------------------------------------
# import xml.dom.minidom

# def main():
#     doc = xml.dom.minidom.parse("samplexml.xml")
#     # print(doc.nodeName)
#     # print(doc.firstChild.tagName)

#     newSkill = doc.createElement("skill")
#     newSkill.setAttribute("name", "jQuery")
#     doc.firstChild.appendChild(newSkill)

#     skills = doc.getElementsByTagName("skill")
#     print("%d skills: " %skills.length )
#     for skill in skills:
#         print(skill.getAttribute("name"))

    
# if __name__ == '__main__':
#     main()
#---------------------------------------------------
#JSON practice

# JSONfile = [ { "country": [
#         { "city": "New York", "state": "NY" },
#         { "city": "Boston", "state": "MA" }
#   ]},
#   { "country": [
#         { "city": "Quebec", "state": "QC" },
#         { "city": "Toronto", "state": "ON" }
#   ]} ]


# for i in JSONfile:
#     for c in i['country']:
#         print(c['city'])
# #-------------------------------------------------
# for test.html
# from html.parser import HTMLParser
# class MyHTMLParser(HTMLParser):
    # def handle_starttag(self, tag, attrs):
    #     print("Encountered tag: ", tag)
    #     position = self.getpos()
    #     print("at line " , position[0], " position ", position[1])
    #     if attrs.__len__() > 0:
    #         print("attributes:")
    #         for a in attrs:
    #             print(a[0], " = ", a[1])
    #         print("\n")
#     def handle_endtag(self, tag):
#         print("Encountered tag: ", tag)
#         position = self.getpos()
#         print("at line " , position[0], " position ", position[1])
#         print('\n')
    
# def main():
#     parser = MyHTMLParser();
#     f = open("test.html")
#     if f.mode == 'r':
#         contents = f.read()
#         parser.feed(contents)
    
# if __name__ == '__main__':
#     main()
#------------------------------------------------------------------------
#xml test file practice
# import xml.dom.minidom

# def main():
#     doc = xml.dom.minidom.parse("test.xml")
#     # print(doc.nodeName)
#     # print(doc.firstChild.tagName)

#     item = doc.createElement("item")
#     item.setAttribute("color", "blue")
#     item.setAttribute("size", "small")
#     doc.firstChild.appendChild(item)

#     items = doc.getElementsByTagName("item")
#     print("%d items: " %items.length )
#     for item in items:
#         print(item.getAttribute("color"), item.getAttribute("size"))
    
# if __name__ == '__main__':
#     main()
#---------------------------------------------------------------------
#JSON practic

jFile = {
    "name": "John",
    "title": "Python Developer",
    "skills": [{
        "name": "coding",
        "level": "expert"
        },
        {
        "name": "documentation",
        "level": "basic"
    }]
}

for i in jFile["skills"]:
    print (i['name'])