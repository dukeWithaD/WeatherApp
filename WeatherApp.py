from tkinter import *
import customtkinter
import requests
from PIL import Image, ImageTk
import json
from datetime import date
import os

today = str(date.today()) #Date
customtkinter.set_appearance_mode("System")

#Global var
imgPath_var = "2"
folder_path = os.getcwd()
path = f"{folder_path}\WeatherAppIcons\\" + str(imgPath_var) + ".png"
img = customtkinter.CTkImage(Image.open(path) ,size=(200, 200))

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        self.geometry(f"{700}x{900}")
        self.title("Weather App - by RandomPeeps")

        #self.config(bg="white")
        self.city_value = StringVar()
        self.location_var = StringVar()
        self.city_var = StringVar()
        self.country_var = StringVar()
        self.long_var = StringVar()
        self.lat_var = StringVar()
        self.temp_var = StringVar()
        self.tempMin_var = StringVar()
        self.tempMax_var = StringVar()
        self.feelsLike_var = StringVar()
        self.feelsLike_varMin_var = StringVar()
        self.feelsLike_varMax_var = StringVar()
        self.wind_var = StringVar()
        self.speed_var = StringVar()
        self.gusts_var = StringVar()
        self.dir_var = StringVar()
        self.angle_var = StringVar()
        self.cloudCover_var = StringVar()
        self.press_var = StringVar()
        self.precip_var = StringVar()
        self.total_var = StringVar()
        self.type_var = StringVar()
        self.prob_var = StringVar()
        self.probPrecip_var = StringVar()
        self.storm_var = StringVar() 
        self.freeze_var = StringVar()
        self.ozone_var = StringVar()
        self.humidity_var = StringVar()
        self.humidity = StringVar()
        self.weather_var = StringVar()
        self.summary_var = StringVar()
        self.visibility_var = StringVar()

        self.location_var.set("Location")
        self.city_var.set("Manila, Philippines")
        # self.city_var.set("City: "+city)
        #self.country_var.set("Country: "+country)
        self.long_var.set("Longitude: ")
        self.lat_var.set("Latitude: ")
        self.weather_var.set("sunny")
        self.temp_var.set("27°C")
        self.tempMin_var.set("Min Temperature: "+"°C")
        self.tempMax_var.set("Max Temperature : "+"°C")

        self.feelsLike_var.set("Feels Like : "+"°C")
        self.feelsLike_varMin_var.set("Min Feels Like: "+"°C")
        self.feelsLike_varMax_var.set("Max Feels Like : "+"°C")

        self.wind_var.set("Wind: ")
        self.speed_var.set("2.1") #speed
        self.gusts_var.set("Gusts: ")
        self.dir_var.set("Direction: ")
        self.angle_var.set("Angle: ")

        self.cloudCover_var.set("Cloud Cover: ")
        self.press_var.set("Pressure: ")

        self.precip_var.set("Precipitation: ")
        self.total_var.set("Total: ")
        self.type_var.set("Type: ")

        self.prob_var.set("Precipitation: ")
        self.probPrecip_var.set("4")
        self.storm_var.set("Storm: ")
        self.freeze_var.set("Freeze: ")

        self.ozone_var.set("Ozone: ")
        self.humidity_var.set("69")
        self.humidity.set("Humidity: ")
        self.visibility_var.set("Visibility: ")
        

        # self.container1 = customtkinter.CTkFrame(self, width=460,height=180, fg_color="transparent").place(x=325,y=190)
        # self.enterCityLbl= customtkinter.CTkLabel(self, text = 'Enter City name:', font = ('Arial', 18)).place(x=165,y=100)
        self.cityEntry = customtkinter.CTkEntry(self, placeholder_text_color=("white", "black"), placeholder_text="CTkEntry", textvariable = self.city_value, fg_color="transparent",  
                                                width = 280, height=40, font = ('Arial', 14)).place(x=46,y=45)

        

        self.searchBtn = customtkinter.CTkButton(self, command = self.showWeather, text = "Check Weather", font = ('Arial', 12), hover= True, 
                                                hover_color= "black", height=40, width= 130, border_width=2, corner_radius=10).place(x=46,y=103) #border_color= "#c75d55", fg_color= "#262626"  text_color="#c75d55",
        
        # self.locationLbl = customtkinter.CTkLabel(self, textvariable = self.location_var, font = ('Arial', 18)).place(x=100, y=100)
        self.left_frame = customtkinter.CTkFrame(self, width=300, height=300, corner_radius=5)#.place(x=35, y=200)
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=(25, 345), pady=(200, 350))
        self.left_frame.grid_rowconfigure(1, weight=1)
        #self.left_frame.place(x=35, y=200)
        # self.left_frame.cget("foreground")
        # bg_color = self.left_frame.cget("background")
        self.cityLbl = customtkinter.CTkLabel(self.left_frame, textvariable=self.city_var, font = ('Arial', 25)).place(x=160, y=40, anchor = CENTER)   
        self.icon = customtkinter.CTkLabel(self.left_frame, image=img, text="", anchor = CENTER).place(x=65,y=60)
        self.weatherLbl = customtkinter.CTkLabel(self.left_frame, textvariable = self.weather_var, font = ('Arial', 22)).place(x=165, y=280, anchor=CENTER)
        # self.countryLbl = customtkinter.CTkLabel(self, textvariable = self.country_var, font = ('Arial', 14)).place(x=130, y=160)
        # self.longLbl = customtkinter.CTkLabel(self, textvariable = self.long_var, font = ('Arial', 14)).place(x=130, y=190)

        # self.latLbl = customtkinter.CTkLabel(self, textvariable = self.lat_var, font = ('Arial', 14)).place(x=130, y=220) 
        self.right_frame = customtkinter.CTkFrame(self, width=300, height=300, corner_radius=5)#.place(x=365, y=200)
        self.right_frame.grid(row=0, column=0, sticky="nsew",padx=(355, 15), pady=(200, 350))
        self.right_frame.grid_rowconfigure(1, weight=1)
        self.dateLbl = customtkinter.CTkLabel(self.right_frame, text= f"Date: {today}", font = ('Arial', 25), anchor = CENTER).place(x=60, y=30)  
        self.tempLbl = customtkinter.CTkLabel(self.right_frame, textvariable = self.temp_var, font = ('Arial', 90)).place(x=160, y=175, anchor = CENTER)
        self.feelsLbl = customtkinter.CTkLabel(self.right_frame,textvariable = self.feelsLike_var, font = ('Arial', 18)).place(x=155, y=250, anchor = CENTER)
        

        self.probPrecipLbl = customtkinter.CTkLabel(self, textvariable = self.probPrecip_var, font = ('Arial', 50)).place(x=140, y=590, anchor = CENTER)  
        self.speedLb1 = customtkinter.CTkLabel(self, textvariable = self.speed_var, font = ('Arial', 50)).place(x=352, y=590, anchor = CENTER)  
        self.humidityLbl = customtkinter.CTkLabel(self, textvariable = self.humidity_var, font = ('Arial', 50)).place(x=562, y=590, anchor = CENTER)

        self.probPrecipH = customtkinter.CTkLabel(self, textvariable = self.prob_var, font = ('Arial', 22)).place(x=80, y=625)  
        self.speedH = customtkinter.CTkLabel(self, textvariable = self.wind_var, font = ('Arial', 22)).place(x=325, y=625)  
        self.humidityH = customtkinter.CTkLabel(self, textvariable = self.humidity, font = ('Arial', 22)).place(x=520, y=625)
    
        # self.probLbl = customtkinter.CTkLabel(self, textvariable = self.prob_var, font = ('Arial', 18)).place(x=600, y=100)

        # self.humidityLbl = customtkinter.CTkLabel(self, textvariable = self.humidity_var, font = ('Arial', 18)).place(x=600, y=280)

        self.tabview = customtkinter.CTkTabview(self, width=680, height=180, border_width = 4)
        self.tabview.grid(row=0, column=0, padx=(10, 0), pady=(690, 0), sticky="nsew")
        self.tabview.add("Summary")
        self.tabview.add("Temperature")
        self.tabview.add("Wind")
        self.tabview.add("Probability")
        self.tabview.add("Others")
        #self.tabview.add("Settings")

        #self.wind = customtkinter.CTkLabel(self.tabview.tab("Wind"), textvariable = self.wind_var, font = ('Arial', 18)).place(x=370, y=100)   
        self.textbox = customtkinter.CTkTextbox(self.tabview.tab("Summary"), width=660, height=127)
        self.textbox.place(x=5, y=0)

        self.tempMinLbl = customtkinter.CTkLabel(self.tabview.tab("Temperature"), textvariable = self.tempMin_var, font = ('Arial', 14)).place(x=15, y=20)
        self.tempMaxLbl = customtkinter.CTkLabel(self.tabview.tab("Temperature"), textvariable = self.tempMax_var, font = ('Arial', 14)).place(x=15, y=40)
        self.feelsMinLbl = customtkinter.CTkLabel(self.tabview.tab("Temperature"), textvariable = self.feelsLike_varMin_var, font = ('Arial', 14)).place(x=15, y=60)
        self.feelsMaxLbl = customtkinter.CTkLabel(self.tabview.tab("Temperature"), textvariable = self.feelsLike_varMax_var, font = ('Arial', 14)).place(x=15, y=80)  
        
        # self.summaryLbl = customtkinter.CTkLabel(self.textbox, textvariable = self.summary_var, font = ('Arial', 18)).place(x=20, y=20, anchor = CENTER)
        self.gusts = customtkinter.CTkLabel(self.tabview.tab("Wind"), textvariable = self.gusts_var, font = ('Arial', 14)).place(x=15, y=20)
        self.dir = customtkinter.CTkLabel(self.tabview.tab("Wind"), textvariable = self.dir_var, font = ('Arial', 14)).place(x=15, y=40)
        self.angle = customtkinter.CTkLabel(self.tabview.tab("Wind"), textvariable = self.angle_var, font = ('Arial', 14)).place(x=15, y=60)

        self.stormLbl = customtkinter.CTkLabel(self.tabview.tab("Probability"), textvariable = self.storm_var, font = ('Arial', 14)).place(x=15, y=20)   
        self.freezeLbl = customtkinter.CTkLabel(self.tabview.tab("Probability"), textvariable = self.freeze_var, font = ('Arial', 14)).place(x=15, y=40)  

        self.cloudCoverLbl = customtkinter.CTkLabel(self.tabview.tab("Others"), textvariable = self.cloudCover_var, font = ('Arial', 14)).place(x=15, y=0) 
        self.pressLbl = customtkinter.CTkLabel(self.tabview.tab("Others"), textvariable = self.press_var, font = ('Arial', 14)).place(x=15, y=20)
        self.precipLbl = customtkinter.CTkLabel(self.tabview.tab("Others"), textvariable = self.precip_var, font = ('Arial', 14)).place(x=15, y=40)
        self.totalLbl = customtkinter.CTkLabel(self.tabview.tab("Others"), textvariable = self.total_var, font = ('Arial', 14)).place(x=15, y=60)
        self.typeLbl = customtkinter.CTkLabel(self.tabview.tab("Others"), textvariable = self.type_var, font = ('Arial', 14)).place(x=15, y=80)
        self.ozoneLbl = customtkinter.CTkLabel(self.tabview.tab("Others"), textvariable = self.ozone_var, font = ('Arial', 14)).place(x=300, y=0)
        self.visibilityLbl = customtkinter.CTkLabel(self.tabview.tab("Others"), textvariable = self.visibility_var, font = ('Arial', 14)).place(x=300, y=20) 
        
        # self.cityLbl = customtkinter.CTkLabel(self.tabview.tab("Location"), textvariable = self.city_var, font = ('Arial', 14)).place(x=130, y=80)  
        # self.countryLbl = customtkinter.CTkLabel(self.tabview.tab("Location"), textvariable = self.country_var, font = ('Arial', 14)).place(x=130, y=110)
        # self.longLbl = customtkinter.CTkLabel(self.tabview.tab("Location"), textvariable = self.long_var, font = ('Arial', 14)).place(x=130, y=140)
        # self.latLbl = customtkinter.CTkLabel(self.tabview.tab("Location"), textvariable = self.lat_var, font = ('Arial', 14)).place(x=130, y=170) 

        #self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Location"), dynamic_resizing=False,
                                                        #values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.optionmenu_1.set("CTkOptionmenu")
        
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self, height=37, corner_radius=10, values=["Dark", "Light"], #"blue" (standard), "green", "dark-blue"
                                                                       command=self.set_appearance_mode)
        self.appearance_mode_optionemenu.place(x=514, y=45)
        customtkinter.set_default_color_theme("green")

    def set_appearance_mode(self, new_default_color_theme: str):
        customtkinter.set_appearance_mode(new_default_color_theme)
    
        # if (self.appearance_mode_optionemenu == "Dark"):
        #     self.fg_c = "#242424"
        # else:
        #     self.fg_c = "#dbdbdb"
        
        # return self.fg_c
        # customtkinter.set_appearance_mode(new_default_color_theme)
        #main()
        # customtkinter.set_appearance_mode(new_default_color_theme)
    
    # def on_entry_click(self, event):
        

    def showWeather(self):
        city_name = self.city_value.get()

        info_url = "https://ai-weather-by-meteosource.p.rapidapi.com/find_places"
        weather_url = "https://ai-weather-by-meteosource.p.rapidapi.com/daily"
        querystring = {"text":city_name}

        headers = {
            "X-RapidAPI-Key": "2986e2663fmsh6b821bccce2546cp1b5da5jsnb401e9ba1d5f",
            "X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
        }

        response = requests.request("GET", info_url, headers=headers, params=querystring)

        _info = response.json()
 
        place_id = _info[0]['place_id']
        city = _info[0]['name']
        country = _info[0]['country']
        coordinatesLong = _info[0]['lon']
        coordinatesLat = _info[0]['lat']

        infostring = {"place_id":place_id,"units":"metric"}

        weather_response = requests.request("GET", weather_url, headers=headers, params=infostring)
        weather_info = weather_response.json()

        weather = str(weather_info['daily']['data'][0]['weather'])
        summary = str(weather_info['daily']['data'][0]['summary'])

        temperature = str(weather_info['daily']['data'][0]['temperature'])
        temperature_min = str(weather_info['daily']['data'][0]['temperature_min'])
        temperature_max = str(weather_info['daily']['data'][0]['temperature_max'])
        feels_like = str(weather_info['daily']['data'][0]['feels_like'])
        feels_like_min = str(weather_info['daily']['data'][0]['feels_like_min'])
        feels_like_max = str(weather_info['daily']['data'][0]['feels_like_max'])

        speed = str(weather_info['daily']['data'][0]['wind']['speed'])
        gusts = str(weather_info['daily']['data'][0]['wind']['gusts'])
        dir = str(weather_info['daily']['data'][0]['wind']['dir'])
        angle = str(weather_info['daily']['data'][0]['wind']['angle'])

        cloud_cover = str(weather_info['daily']['data'][0]['cloud_cover'])
        pressure = str(weather_info['daily']['data'][0]['pressure'])

        total = str(weather_info['daily']['data'][0]['precipitation']['total'])
        type = str(weather_info['daily']['data'][0]['precipitation']['type'])

        precipitation = str(weather_info['daily']['data'][0]['probability']['precipitation'])
        storm = str(weather_info['daily']['data'][0]['probability']['storm'])
        freeze = str(weather_info['daily']['data'][0]['probability']['freeze'])

        ozone = str(weather_info['daily']['data'][0]['ozone'])
        humidity = str(weather_info['daily']['data'][0]['humidity'])
        visibility = str(weather_info['daily']['data'][0]['visibility'])

        icon = str(weather_info['daily']['data'][0]['icon'])
        

        self.location_var.set("Location")
        self.city_var.set(city+", "+country)
        # self.city_var.set("City: "+city)
        #self.country_var.set("Country: "+country)
        self.long_var.set("Longitude: "+coordinatesLong)
        self.lat_var.set("Latitude: "+coordinatesLat)

        self.temp_var.set(str(temperature)+"°C")
        self.tempMin_var.set("Min Temperature: "+str(temperature_min)+"°C")
        self.tempMax_var.set("Max Temperature : "+str(temperature_max)+"°C")

        self.feelsLike_var.set("Feels Like : "+str(feels_like)+"°C")
        self.feelsLike_varMin_var.set("Min Feels Like: "+str(feels_like_min)+"°C")
        self.feelsLike_varMax_var.set("Max Feels Like : "+str(feels_like_max)+"°C")

        self.wind_var.set("Wind: ")
        self.speed_var.set(str(speed)+"km/h")
        self.gusts_var.set("Gusts: "+str(gusts))
        self.dir_var.set("Direction: "+str(dir))
        self.angle_var.set("Angle: "+str(angle))

        self.cloudCover_var.set("Cloud Cover: " +str(cloud_cover))
        self.press_var.set("Pressure: " +str(pressure))

        self.precip_var.set("Precipitation: ")
        self.total_var.set("Total: " +str(total))
        self.type_var.set("Type: " +str(type))

        self.prob_var.set("Precipitation: ")
        self.probPrecip_var.set(str(precipitation))
        self.storm_var.set("Storm: " +str(storm))
        self.freeze_var.set("Freeze: " +str(freeze))

        self.ozone_var.set("Ozone: " +str(ozone))
        self.humidity_var.set(str(humidity))
        self.visibility_var.set("Visibility: " +str(visibility))

        #str(weather.replace("_", " "))
        self.weather_var.set(str(weather.replace("_", " ")))
        
        self.summary_var.set("Summary: " +str(summary))
        self.textbox.insert("0.0", str(summary))

        imgPath_var = icon
        path = f"{folder_path}\WeatherAppIcons\\" + str(imgPath_var) + ".png"
        new_image = customtkinter.CTkImage(Image.open(path),size=(200, 200))
        self.icon = customtkinter.CTkLabel(self.left_frame, image=new_image, text="", fg_color="transparent").place(x=65,y=60)

def main():
    App().mainloop()

main()