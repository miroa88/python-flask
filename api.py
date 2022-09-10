from flask import Flask, request, jsonify
import datetime
from flask_cors import CORS
from apiHandler import * 
import re

app = Flask(__name__)
CORS(app)  

currentDateTime = datetime.now()
instylApp = AppContainer("instyle")

@app.route('/add', methods=['POST'])
def add():
    try:
        #checking request content type
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            dict = request.get_json()
        else:
            return jsonify({"msg" : "Content-Type not supported!"}), 400
        #destructuring the request
        customerId, customerName, customerPhone, orderId, status, dateAndTime = dict.values()
        #creating new appointment
        newApp = Appointment(customerId, customerName, customerPhone, orderId, status, dateAndTime)
        
        schedule = None
        if(not instylApp.keyExist(newApp.getDate())):
            #creating a new daily schedule
            schedule = DailySchedule(newApp.getDate())
            instylApp.putDailySchedule(schedule)
        else:
            schedule = instylApp.getScheduleObj(newApp.getDate())

        if schedule.setAppointment(newApp):
            return jsonify({"msg" : "succesfully added"}), 201
        return jsonify({"msg" : "unable to add"}), 400
    except:
        return jsonify({"msg" : "something went wrong"}), 500


@app.route('/<date>/', methods=['GET'])
def getDailyReport(date):
    try:
        if instylApp.keyExist(date):
            schedule = instylApp.getScheduleObj(date)
            return jsonify(schedule.getScheduleJson()), 200
        else:
            return jsonify({"msg" : "There is no scheduled appointment."}), 404
    except:
        return jsonify({"msg" : "something went wrong"}), 500


@app.route('/<date>/<time>/edit', methods=['PUT'])
def update(date, time):
    try:
        #checking request content type
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            dict = request.get_json()
            #checking if appointment exist
            appointment = None
            if instylApp.keyExist(date):
                schedule = instylApp.getScheduleObj(date)
                appointment = schedule.getAppByTime(time)
            if not appointment:
                return jsonify({"msg" : "The appointment does not exist."}), 404
            #destructuring the request
            orderId, status, dateAndTime = dict.values()
            #updating order id
            if len(orderId.strip()) > 0:
                appointment.setOrderId(orderId.strip())
            else:
                return jsonify({"msg" : "updating failed! Wrong order id."}), 400 
            #updating order status    
            if status.strip().lower() in ['first fitting', 'second fitting','third fitting', 'custom']:
                appointment.setStatus(status.strip())
            else:
                return jsonify({"msg" : "updating failed! Wrong status."}), 400    
            #updating order date and time     
            if re.match('[0-9]{6} [0-9]{1,2}:[0-9]{2}', dateAndTime.strip()):
                newDate = dateAndTime.strip().split(" ")[0]
                newTime = dateAndTime.strip().split(" ")[1]
                #if time or date has changed
                if date != newDate or time != newTime:    
                    appointment.setDateTime(dateAndTime.strip())
                    if(date != newDate):
                        #if appontment date has change, creating
                        # a new daily schedule in case it does not exist
                        newSchedule = None
                        if instylApp.keyExist(newDate):
                            newSchedule = instylApp.getScheduleObj(newDate)
                        else:
                            newSchedule = DailySchedule(newDate)
                            instylApp.putDailySchedule(newSchedule)
                        #adding the modified appointment to the new schedule
                        
                        if newSchedule.setAppointment(appointment):
                            #deleting the appointment old reference if it successfully added to the new schedule
                            schedule.deleteApp(time)
                        else:
                            return jsonify({"msg" : "updating failed!"}), 400
                    else: #if the appointment time changes and the date remains the same
                        if schedule.setAppointment(appointment):
                            schedule.deleteApp(time)
                        else:
                            return jsonify({"msg" : "updating time failed!"}), 400
            return jsonify({"msg" : "succesfully updated"}), 200
        else:
            return jsonify({"msg" : "Content-Type not supported!"}), 400
    except KeyError as err:
        return jsonify({"msg" : "Something went wrong"})


@app.route('/<date>/<time>', methods=['DELETE'])
def delete(date, time):
    try:
        # checking if appointment exist
        if instylApp.keyExist(date):
            schedule = instylApp.getScheduleObj(date)
            if schedule.getAppByTime(time):
                schedule.deleteApp(time)
                return jsonify({"msg" : "succesfully deleted"}), 200
        return jsonify({"msg" : "The appointment does not exist."}), 404
            
    except KeyError as err:
        return jsonify({"msg" : "Something went wrong"})
            
   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
