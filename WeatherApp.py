from tkinter import *
import customtkinter
import requests
import json
from datetime import date

today = str(date.today()) #Date

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{800}x{880}")
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
        self.visibility_var = StringVar()

        self.enterCityLbl= customtkinter.CTkLabel(self, text = 'Enter City name:', font = ('Arial', 18)).place(x=90,y=40)
        self.cityEntry = customtkinter.CTkEntry(self, textvariable = self.city_value,  width = 300, height=40, font = ('Arial', 18)).place(x=230,y=35)
        # self.dateLbl = customtkinter.CTkLabel(self, text= f"Date: {today}", font = ('Arial', 18)).place(x=820, y=40)  
        # self.locationLbl = customtkinter.CTkLabel(self, textvariable = self.location_var, font = ('Arial', 18)).place(x=100, y=100)   
        self.cityLbl = customtkinter.CTkLabel(self, textvariable = self.city_var, font = ('Arial', 14)).place(x=250, y=230, anchor = W)  
        # self.countryLbl = customtkinter.CTkLabel(self, textvariable = self.country_var, font = ('Arial', 14)).place(x=130, y=160)
        # self.longLbl = customtkinter.CTkLabel(self, textvariable = self.long_var, font = ('Arial', 14)).place(x=130, y=190)
        # self.latLbl = customtkinter.CTkLabel(self, textvariable = self.lat_var, font = ('Arial', 14)).place(x=130, y=220) 
        self.tempLbl = customtkinter.CTkLabel(self, textvariable = self.temp_var, font = ('Arial', 100)).place(x=400, y=150, anchor = CENTER)

        # self.tempMinLbl = customtkinter.CTkLabel(self, textvariable = self.tempMin_var, font = ('Arial', 14)).place(x=130, y=310)
        # self.tempMaxLbl = customtkinter.CTkLabel(self, textvariable = self.tempMax_var, font = ('Arial', 14)).place(x=130, y=340)
        self.feelsLbl = customtkinter.CTkLabel(self, textvariable = self.feelsLike_var, font = ('Arial', 18)).place(x=250, y=250, anchor = W)
        # self.feelsMinLbl = customtkinter.CTkLabel(self, textvariable = self.feelsLike_varMin_var, font = ('Arial', 14)).place(x=130, y=430)
        # self.feelsMaxLbl = customtkinter.CTkLabel(self, textvariable = self.feelsLike_varMax_var, font = ('Arial', 14)).place(x=130, y=460)  
        # self.wind = customtkinter.CTkLabel(self, textvariable = self.wind_var, font = ('Arial', 18)).place(x=370, y=100)   
        # self.speed = customtkinter.CTkLabel(self, textvariable = self.speed_var, font = ('Arial', 14)).place(x=400, y=130)  
        # self.gusts = customtkinter.CTkLabel(self, textvariable = self.gusts_var, font = ('Arial', 14)).place(x=400, y=160)
        # self.dir = customtkinter.CTkLabel(self, textvariable = self.dir_var, font = ('Arial', 14)).place(x=400, y=190)
        # self.angle = customtkinter.CTkLabel(self, textvariable = self.angle_var, font = ('Arial', 14)).place(x=400, y=220)
        # self.cloudCoverLbl = customtkinter.CTkLabel(self, textvariable = self.cloudCover_var, font = ('Arial', 18)).place(x=370, y=280) 
        # self.pressLbl = customtkinter.CTkLabel(self, textvariable = self.press_var, font = ('Arial', 18)).place(x=370, y=310)
        # self.precipLbl = customtkinter.CTkLabel(self, textvariable = self.precip_var, font = ('Arial', 18)).place(x=370, y=400)
        # self.totalLbl = customtkinter.CTkLabel(self, textvariable = self.total_var, font = ('Arial', 14)).place(x=400, y=430)
        # self.typeLbl = customtkinter.CTkLabel(self, textvariable = self.type_var, font = ('Arial', 14)).place(x=400, y=460)
        # self.probLbl = customtkinter.CTkLabel(self, textvariable = self.prob_var, font = ('Arial', 18)).place(x=600, y=100)
        # self.probPrecipLbl = customtkinter.CTkLabel(self, textvariable = self.probPrecip_var, font = ('Arial', 14)).place(x=630, y=130)  
        # self.stormLbl = customtkinter.CTkLabel(self, textvariable = self.storm_var, font = ('Arial', 14)).place(x=630, y=160)   
        # self.freezeLbl = customtkinter.CTkLabel(self, textvariable = self.freeze_var, font = ('Arial', 14)).place(x=630, y=190)  
        # self.ozoneLbl = customtkinter.CTkLabel(self, textvariable = self.ozone_var, font = ('Arial', 18)).place(x=600, y=250)
        # self.humidityLbl = customtkinter.CTkLabel(self, textvariable = self.humidity_var, font = ('Arial', 18)).place(x=600, y=280)
        # self.visibilityLbl = customtkinter.CTkLabel(self, textvariable = self.visibility_var, font = ('Arial', 18)).place(x=600, y=310)  

        self.searchBtn = customtkinter.CTkButton(self, command = self.showWeather, text = "Check Weather", font = ('Arial', 14), text_color="#c75d55", hover= True, 
        hover_color= "black", height=40, width= 140, border_width=2, corner_radius=10, border_color= "#c75d55", fg_color= "#262626").place(x=550,y=35)


        self.tabview = customtkinter.CTkTabview(self, width=690)
        self.tabview.grid(row=0, column=0, padx=(55, 0), pady=(590, 0), sticky="nsew")
        self.tabview.add("Location")
        self.tabview.add("Wind")
        
        # self.cityLbl = customtkinter.CTkLabel(self.tabview.tab("Location"), textvariable = self.city_var, font = ('Arial', 14)).place(x=130, y=80)  
        # self.countryLbl = customtkinter.CTkLabel(self.tabview.tab("Location"), textvariable = self.country_var, font = ('Arial', 14)).place(x=130, y=110)
        # self.longLbl = customtkinter.CTkLabel(self.tabview.tab("Location"), textvariable = self.long_var, font = ('Arial', 14)).place(x=130, y=140)
        # self.latLbl = customtkinter.CTkLabel(self.tabview.tab("Location"), textvariable = self.lat_var, font = ('Arial', 14)).place(x=130, y=170) 

        #self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Location"), dynamic_resizing=False,
                                                        #values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.optionmenu_1.set("CTkOptionmenu")

    def display_text():
        pass

    def showWeather(self):
        city_name = self.city_value.get()

        info_url = "https://ai-weather-by-meteosource.p.rapidapi.com/find_places"
        weather_url = "https://ai-weather-by-meteosource.p.rapidapi.com/daily"
        querystring = {"text":city_name}

        headers = {
            "X-RapidAPI-Key": "6ba1808ad0msh46bfae50685eb3fp1d41ebjsnac02a47c5473",
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

        self.wind_var.set("Wind")
        self.speed_var.set("Speed: "+str(speed))
        self.gusts_var.set("Gusts: "+str(gusts))
        self.dir_var.set("Direction: "+str(dir))
        self.angle_var.set("Angle: "+str(angle))

        self.cloudCover_var.set("Cloud Cover: " +str(cloud_cover))
        self.press_var.set("Pressure: " +str(pressure))

        self.precip_var.set("Precipitation")
        self.total_var.set("Total: " +str(total))
        self.type_var.set("Type: " +str(type))

        self.prob_var.set("Probability")
        self.probPrecip_var.set("Precipitation: " +str(precipitation))
        self.storm_var.set("Storm: " +str(storm))
        self.freeze_var.set("Freeze: " +str(freeze))

        self.ozone_var.set("Ozone: " +str(ozone))
        self.humidity_var.set("Humidity: " +str(humidity))
        self.visibility_var.set("Visibility: " +str(visibility))

def main():
    App().mainloop()

main()