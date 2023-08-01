from tkinter import END

import requests
import tkinter
apiKey = "cf6b333fba3f73ae00ceb63986e769f9"
window = tkinter.Tk()
window.title("Weather App")
window.minsize(width=300,height=300)
window.config(bg="light blue")
window.config(padx=20,pady=20)

def getWeatherData(apiKey = "cf6b333fba3f73ae00ceb63986e769f9"):
    cityName = entry.get()
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
    completeUrl = f"{baseUrl}q={cityName}&appid={apiKey}"

    response = requests.get(completeUrl)
    data = response.json()

    if data["cod"] == "404":
        resultLable.config(text="City not found")
        resultLable2.destroy()
        resultLable3.destroy()
    else:
        mainData = data["main"]
        weather_data = data["weather"][0]

        temperature = mainData["temp"]
        humidity = mainData["humidity"]
        weather_description = weather_data["description"]


        resultLable.config(text=f"Weather: {weather_description}")
        resultLable2.config(text=f"Temparature: {temperature-273.15} C")
        resultLable3.config(text=f"Humidity: {humidity}%")

    entry.delete(0,END)

label = tkinter.Label(text="Enter the city for which you want to know the weather: " ,bg="pink")
label.pack()

entry = tkinter.Entry(width=18)
entry.place(x=90,y=30)

button = tkinter.Button(text="Find" , width=15,command=getWeatherData)
button.place(x=90,y=60)

resultLable =tkinter.Label(bg="pink")
resultLable.place(x=90,y=100)

resultLable2 =tkinter.Label(bg="pink")
resultLable2.place(x=90,y=120)

resultLable3 =tkinter.Label(bg="pink")
resultLable3.place(x=90,y=140)


window.mainloop()