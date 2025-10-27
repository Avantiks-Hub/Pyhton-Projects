#importing modules
import time
from tkinter import *
from tkinter import messagebox as mb
from plyer import notification 
import requests

def getnotif():
    cityname=place.get()
    baseurl="https://api.openweathermap.org/data/2.5/weather?"
    try:
        url=baseurl+"appid="+'5262bdda9ccc63ea30dd742c96a65079'+"&q="+cityname
        response=requests.get(url)
        x=response.json()
        y=x["main"]
        temp=y["temp"]
        temp-=273
        pres=y["pressure"]
        hum=y["humidity"]
        z=x["weather"]
        weather_desc=z[0]["description"]
        info="Here the weather desc of "+cityname+":"+"\nTemperature ="+str(temp)+"°C"+"\nAtmospheric Pressure= "+str(pres)+"hpa"+"\nHumidity= "+str(hum)+"%"+"\n Description of the weather= "+str(weather_desc)
        notification.notify(title="YOUR WEATHER REPORT",message=info,timeout=2)
        time.sleep(7)
    except Exception as e:
        mb.showerror("Error",e)

    

#creating the window
win= Tk()
win.title("AS Weather Alerts")
win.geometry("600x200")
win.config(bg="azure")
#lables
Label(win,text="AS Weather Notifier",font=("arial",15),fg="black",bg="azure").place(x=200,y=15)
Label(win,text="Enter the location",font=("arial",15),fg="black",bg="azure").place(x=120,y=60)
#entry
place=StringVar(win)
place_entry=Entry(win,width=20,textvariable=place)
place_entry.place(relx=0.5,rely=0.33)
#button to get notification
btn=Button(win,text="Get Weather Report",font=7,fg="black",bg="white",command=getnotif).place(relx=0.35,rely=0.60)

win.mainloop()
