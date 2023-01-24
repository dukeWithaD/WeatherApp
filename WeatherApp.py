from tkinter import *
import customtkinter
import requests
from PIL import Image, ImageTk
import json
from datetime import date
import os

today = str(date.today()) #Date
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

imgPath_var = "5"
folder_path = os.getcwd()
path = f"{folder_path}\WeatherAppIcons\\" + str(imgPath_var) + ".png"
img = customtkinter.CTkImage(Image.open(path), size=(250, 250))

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{800}x{1000}")
        self.title("Weather App - by RandomPeeps")

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

        self.icon = customtkinter.CTkLabel(self, image=img, text="").place(x=165,y=190)

        self.container1 = customtkinter.CTkFrame(self, width=460,height=180).place(x=165,y=190)
        self.enterCityLbl= customtkinter.CTkLabel(self, text = 'Enter City name:', font = ('Arial', 18)).place(x=165,y=100)
        self.cityEntry = customtkinter.CTkEntry(self, textvariable = self.city_value,  width = 300, height=40, font = ('Arial', 18)).place(x=165,y=135)

        self.searchBtn = customtkinter.CTkButton(self, command = self.showWeather, text = "Check Weather", font = ('Arial', 14), hover= True, 
        hover_color= "black", height=40, width= 140, border_width=2, corner_radius=10).place(x=485,y=135) #border_color= "#c75d55", fg_color= "#262626"  text_color="#c75d55",
        # self.dateLbl = customtkinter.CTkLabel(self, text= f"Date: {today}", font = ('Arial', 18)).place(x=820, y=40)  
        # self.locationLbl = customtkinter.CTkLabel(self, textvariable = self.location_var, font = ('Arial', 18)).place(x=100, y=100)   
          
        # self.countryLbl = customtkinter.CTkLabel(self, textvariable = self.country_var, font = ('Arial', 14)).place(x=130, y=160)
        # self.longLbl = customtkinter.CTkLabel(self, textvariable = self.long_var, font = ('Arial', 14)).place(x=130, y=190)
        # self.latLbl = customtkinter.CTkLabel(self, textvariable = self.lat_var, font = ('Arial', 14)).place(x=130, y=220) 
        self.cityLbl = customtkinter.CTkLabel(self.container1, textvariable = self.city_var, fg_color="#2b2b2b", font = ('Arial', 18)).place(x=400, y=340, anchor = CENTER)
        self.tempLbl = customtkinter.CTkLabel(self.container1, textvariable = self.temp_var, fg_color="#2b2b2b", font = ('Arial', 100)).place(x=400, y=250, anchor = CENTER)

        # self.tempMinLbl = customtkinter.CTkLabel(self, textvariable = self.tempMin_var, font = ('Arial', 14)).place(x=130, y=310)
        # self.tempMaxLbl = customtkinter.CTkLabel(self, textvariable = self.tempMax_var, font = ('Arial', 14)).place(x=130, y=340)
        self.feelsLbl = customtkinter.CTkLabel(self.container1, textvariable = self.feelsLike_var, fg_color="#2b2b2b", font = ('Arial', 20)).place(x=300, y=310, anchor = W)
        # self.feelsMinLbl = customtkinter.CTkLabel(self, textvariable = self.feelsLike_varMin_var, font = ('Arial', 14)).place(x=130, y=430)
        # self.feelsMaxLbl = customtkinter.CTkLabel(self, textvariable = self.feelsLike_varMax_var, font = ('Arial', 14)).place(x=130, y=460)  

        self.probPrecipLbl = customtkinter.CTkLabel(self, textvariable = self.probPrecip_var, font = ('Arial', 80)).place(x=170, y=625, anchor = CENTER)  
        self.speed = customtkinter.CTkLabel(self, textvariable = self.speed_var, font = ('Arial', 80)).place(x=400, y=625, anchor = CENTER)  
        self.humidityLbl = customtkinter.CTkLabel(self, textvariable = self.humidity_var, font = ('Arial', 80)).place(x=610, y=625, anchor = CENTER)

        self.probPrecipLbl = customtkinter.CTkLabel(self, textvariable = self.prob_var, font = ('Arial', 18)).place(x=120, y=675)  
        self.speed = customtkinter.CTkLabel(self, textvariable = self.wind_var, font = ('Arial', 18)).place(x=375, y=675)  
        self.humidityLbl = customtkinter.CTkLabel(self, textvariable = self.humidity, font = ('Arial', 18)).place(x=575, y=675)

        # self.angle = customtkinter.CTkLabel(self, textvariable = self.angle_var, font = ('Arial', 14)).place(x=400, y=220)
        # self.cloudCoverLbl = customtkinter.CTkLabel(self, textvariable = self.cloudCover_var, font = ('Arial', 18)).place(x=370, y=280) 
        # self.pressLbl = customtkinter.CTkLabel(self, textvariable = self.press_var, font = ('Arial', 18)).place(x=370, y=310)
        # self.precipLbl = customtkinter.CTkLabel(self, textvariable = self.precip_var, font = ('Arial', 18)).place(x=370, y=400)
        # self.totalLbl = customtkinter.CTkLabel(self, textvariable = self.total_var, font = ('Arial', 14)).place(x=400, y=430)
        # self.typeLbl = customtkinter.CTkLabel(self, textvariable = self.type_var, font = ('Arial', 14)).place(x=400, y=460)
        # self.probLbl = customtkinter.CTkLabel(self, textvariable = self.prob_var, font = ('Arial', 18)).place(x=600, y=100)
        
        # self.stormLbl = customtkinter.CTkLabel(self, textvariable = self.storm_var, font = ('Arial', 14)).place(x=630, y=160)   
        # self.freezeLbl = customtkinter.CTkLabel(self, textvariable = self.freeze_var, font = ('Arial', 14)).place(x=630, y=190)  
        # self.ozoneLbl = customtkinter.CTkLabel(self, textvariable = self.ozone_var, font = ('Arial', 18)).place(x=600, y=250)
        # self.humidityLbl = customtkinter.CTkLabel(self, textvariable = self.humidity_var, font = ('Arial', 18)).place(x=600, y=280)
        # self.visibilityLbl = customtkinter.CTkLabel(self, textvariable = self.visibility_var, font = ('Arial', 18)).place(x=600, y=310) 
        #self.weatherLbl = customtkinter.CTkLabel(self, textvariable = self.weather_var, font = ('Arial', 18)).place(x=600, y=340)
        #self.summaryLbl = customtkinter.CTkLabel(self, textvariable = self.summary_var, font = ('Arial', 18)).place(x=375, y=500, anchor = CENTER) 

        
        self.tabview = customtkinter.CTkTabview(self, width=690, border_width = 4)
        self.tabview.grid(row=0, column=0, padx=(55, 0), pady=(725, 0), sticky="nsew")
        self.tabview.add("Location")
        self.tabview.add("Wind")

        #self.wind = customtkinter.CTkLabel(self.tabview.tab("Wind"), textvariable = self.wind_var, font = ('Arial', 18)).place(x=370, y=100)   
        
        self.gusts = customtkinter.CTkLabel(self.tabview.tab("Wind"), textvariable = self.gusts_var, font = ('Arial', 24)).place(x=200, y=60)
        self.dir = customtkinter.CTkLabel(self.tabview.tab("Wind"), textvariable = self.dir_var, font = ('Arial', 24)).place(x=200, y=90)
        
        # self.cityLbl = customtkinter.CTkLabel(self.tabview.tab("Location"), textvariable = self.city_var, font = ('Arial', 14)).place(x=130, y=80)  
        # self.countryLbl = customtkinter.CTkLabel(self.tabview.tab("Location"), textvariable = self.country_var, font = ('Arial', 14)).place(x=130, y=110)
        # self.longLbl = customtkinter.CTkLabel(self.tabview.tab("Location"), textvariable = self.long_var, font = ('Arial', 14)).place(x=130, y=140)
        # self.latLbl = customtkinter.CTkLabel(self.tabview.tab("Location"), textvariable = self.lat_var, font = ('Arial', 14)).place(x=130, y=170) 

        #self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Location"), dynamic_resizing=False,
                                                        #values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.optionmenu_1.set("CTkOptionmenu")
        
    #     self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self, values=["blue", "green", "dark-blue"], #"blue" (standard), "green", "dark-blue"
    #                                                                    command=self.change_default_color_theme)
    #     self.appearance_mode_optionemenu.grid(row=0, column=0, padx=20, pady=(10, 10))

    # def change_default_color_theme(self, new_default_color_theme: str):
    #     customtkinter.set_default_color_theme(new_default_color_theme)

    def display_text():
        pass

    def showWeather(self):
        city_name = self.city_value.get()

        info_url = "https://ai-weather-by-meteosource.p.rapidapi.com/find_places"
        weather_url = "https://ai-weather-by-meteosource.p.rapidapi.com/daily"
        querystring = {"text":city_name}

        headers = {
            "X-RapidAPI-Key": "4278142229mshb81b0105d4555bbp1aba29jsnb103c0c7f32e",
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
        self.speed_var.set(str(speed))
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

        str(weather.replace("_", " "))
        self.weather_var.set("Weather: " +str(weather.upper()))
        
        self.summary_var.set("Summary: " +str(summary))
  
        imgPath_var = icon
        path = f"{folder_path}\WeatherAppIcons\\" + str(imgPath_var) + ".png"
        new_image = customtkinter.CTkImage(Image.open(path), size=(250, 250))
        self.icon = customtkinter.CTkLabel(self, image=new_image, text="").place(x=165,y=190)

def main():
    App().mainloop()

main()