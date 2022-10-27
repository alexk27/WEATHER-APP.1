import requests

# import the tkinter module and alias is :tk
import tkinter as tk

from tkinter import *
# pip install pyinstaller

# click event for input


def click(event):
    entry.config(state=NORMAL)
    entry.delete(0, END)


def get_it(entry_o):
    print("there are the following: ", entry_o)


#  fnl ='City : %str \nCondition: %str \nTemperature(F): %s' % (name, des, temp)
# except:
# fnl= 'please try again'
# return  fnl
# api.openweathermap.org/data/ 2.5 /forecast?   q = {city name}, {country code} & appid = {API key}
# function that defines current weather
def fmt_response(weather):
     name = weather['name']
     des = weather['weather'][0]['description']
     temp = weather['main']['temp']

     return "City: " + str(name) + "," + '  Description: ' + str(des) + "," + '  Current Temperature: ' + str(temp)


def get_weather(city):
    weather_key = 'bc25f93fcd1cb2cf0003d0a1f3909e1e'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    attr = {'q': city, 'appid': weather_key}
    response = requests.get(url, attr)

    weather = response.json()
    label_into['text'] = fmt_response(weather)
# print(response.json())
# function tk for the main window


root = tk.Tk()


# all code goes here
root.title(" Alex WEATHER APP ")
root.geometry('600x550')

# bg images as png only for now unless: pip install pillow is downloaded

bg_image = tk.PhotoImage(file="images/weatherlog.PNG")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)


# label for welcoming
label = tk.Label(root, text='welcome to the Weather App ', font=50, background="black", fg="white", height=1)
label.place(relx=0.27, relheight=0.1, relwidth=0.40)

# frame(small app background)
frame = tk.Frame(root, bg="skyblue", bd=3)
frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='n')


button = tk.Button(frame, text=' Search ', background="black", fg="red", command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

# entry field and function that applies to it (<button-1> :for the widget)
entry = tk.Entry(frame, bg="white")
entry.place(relwidth=0.65, relheight=1)
entry.insert(0, "Enter A City Of Your Choice")
entry.config(state=DISABLED)
entry.bind("<Button-1>", click)

# lower frame
lowerFrame = tk.Frame(root, bg='skyblue', bd=10)
lowerFrame.place(relx=0.5, rely=0.25, relheight=0.50, relwidth=0.70, anchor='n')

# label for results
label_into = tk.Label(lowerFrame)
label_into.place(relheight=1, relwidth=1)

# mainloop method keeps the window  opened
root.mainloop()

# for exe file
# cd C:\Users\Dell\PycharmProjects\firstpy
# pyinstaller --onefile  --icon=weathericon.ico main.py
