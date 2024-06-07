
from tkinter import *
import requests
import json

root = Tk()
root.geometry("500x500")
root.resizable(0,0)
wait = Label(root, text="Please wait a few seconds after entering the name of your city",font=("Arial", 10) ).pack(pady=10)
entry = Entry(root, width=50, borderwidth=5)
entry.pack(pady=10)
global frame
frame = LabelFrame(root, text="Frame", padx=5, pady=10)
frame.pack(pady=10)

def myClick():
    global frame
    frame.pack_forget()
    city = (entry.get()).lower()
    city = city.replace(' ', '%20')
    url ='https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'+city+'?unitGroup=metric&include=current&key=TL5VJ8GAC5HLEH3PPZNZ4YJTP&contentType=json'
    try:
        api_request = requests.get(url)
        api = json.loads(api_request.content)
        frame = LabelFrame(root, text="Frame", padx=5, pady=10)
        frame.pack(pady=10)
        temp = Label(frame, text="Temperature is "+str(api['currentConditions']['temp'])+' degree Celsius', font=("Arial", 15) ).pack(pady=10)
        humidity = Label(frame, text="Humidity is "+str(api['currentConditions']['humidity']),font=("Arial", 15) ).pack(pady=10)
        windspeed = Label(frame, text="Wind speed is "+str(api['currentConditions']['windspeed'])+" km/hour",font=("Arial", 15) ).pack(pady=10)
        conditions = Label(frame, text="Condition: " +api['days'][0]['conditions'],font=("Arial", 15) ).pack(pady=10)  
    
    except Exception as e:
        frame = LabelFrame(root, text="Frame", padx=5, pady=10)
        frame.pack(pady=10)
        Label(frame, text="An error occured. Please check the city name again.", justify='center').pack(pady=10)

myButton = Button(root, text="Enter the name of your city",  width=30,height=2, command=myClick, fg='white', bg='blue', state=NORMAL)  #YOU CAN ADD STATE = DISABLED or NORMAL or ACTIVE
myButton.pack(pady=10)


root.mainloop()
