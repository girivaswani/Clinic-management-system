import requests
import json
import sqlite3
from tkinter import messagebox

URL = 'https://www.sms4india.com/api/v1/sendCampaign'


class SMS:
    def __init__(self, ID):
        conn = sqlite3.connect('patients_book.db')

        c = conn.cursor()

        sql = "SELECT * FROM 'patients' WHERE ID = " + str(ID)
        c.execute(sql)
        patient = c.fetchone()
        phneno = str(patient[8])

        # get request
        def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
            req_params = {
                'apikey': apiKey,
                'secret': secretKey,
                'usetype': useType,
                'phone': phoneNo,
                'message': textMessage,
                'senderid': senderId
            }
            return requests.post(reqUrl, req_params)

        slot = '9:00-12:00 AM'

        # get response
        response = sendPostRequest(URL, 'apikey', 'secretkey', 'stage', phneno,
                                   '8411954930', f'Dear {patient[1]}, Your Appointment has been fixed for {slot}.Kindly visit the clinic in the working hours.')
        """
          Note:-
            you must provide apikey, secretkey, usetype, mobile, senderid and message values
            and then requst to api
        """
        # print response if you want
        print(response.text)
        #print(type(response.text))
        if response.text[-9:-2] == "success":
            #print('ok')
            sql = "UPDATE 'patients' SET Status=1 where ID = " + str(ID)
            c.execute(sql)
            messagebox.showinfo('Send', 'Appointment Has Been Fixed !')

        conn.commit()
        conn.close()
