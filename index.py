import tkinter as tk
from tkinter import messagebox
import requests
import base64
from io import BytesIO

def get_weather():
    city = city_entry.get()
    api_key = "8fef6a42e700537e9361995ce7d15695"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temperature_label.config(text=f"Temperature: {data['main']['temp']}°C", fg="blue", font=("Helvetica", 12, "bold"))
        description_label.config(text=f"Description: {data['weather'][0]['description']}", fg="green", font=("Helvetica", 12, "italic"))
        humidity_label.config(text=f"Humidity: {data['main']['humidity']}%", fg="purple", font=("Helvetica", 12))
        pressure_label.config(text=f"Pressure: {data['main']['pressure']} hPa", fg="orange", font=("Helvetica", 12))
        wind_label.config(text=f"Wind Speed: {data['wind']['speed']} m/s", fg="brown", font=("Helvetica", 12))
        
        icon_id = data['weather'][0]['icon']
        weather_icon_url = f"http://openweathermap.org/img/w/{icon_id}.png"
        response = requests.get(weather_icon_url)
        if response.status_code == 200:
            image_data = base64.b64encode(response.content)
            photo = tk.PhotoImage(data=image_data)
            weather_icon_label.config(image=photo)
            weather_icon_label.image = photo 
    else:
        messagebox.showerror("Error", "City not found. Please try again.")

root = tk.Tk()
root.title("Weather App")
root.geometry("500x350")

city_label = tk.Label(root, text="Enter city name:", font=("Helvetica", 14))
city_label.pack()

city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Helvetica", 14), bg="lightblue", fg="white")
get_weather_button.pack(pady=10)

temperature_label = tk.Label(root, text="", font=("Helvetica", 12))
temperature_label.pack()

description_label = tk.Label(root, text="", font=("Helvetica", 12))
description_label.pack()

humidity_label = tk.Label(root, text="", font=("Helvetica", 12))
humidity_label.pack()

pressure_label = tk.Label(root, text="", font=("Helvetica", 12))
pressure_label.pack()

wind_label = tk.Label(root, text="", font=("Helvetica", 12))
wind_label.pack()


weather_icon_label = tk.Label(root)
weather_icon_label.pack()

root.mainloop()
