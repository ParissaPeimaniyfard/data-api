# pylint: disable=missing-module-docstring

import sys
import urllib.parse
import requests

BASE_URI = "https://weather.lewagon.com"



def search_city(query):
    '''
    Look for a given city. If multiple options are returned, have the user choose between them.
    Return one city (or None)
    '''
    url= "https://weather.lewagon.com/geo/1.0/direct"
    city= requests.get(url, params ={"q":query, "limit": 5}).json()
    cit=city[0]["name"]
    clat=city[0]["lat"]
    clon=city[0]["lon"]
    output=weather_forecast(clat,clon,cit)
    return output
#print(search_city("london"))

def weather_forecast(lat, lon, city_name):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''
    url="https://weather.lewagon.com/data/2.5/forecast"
    forcast=requests.get(url, params={"lat":lat, "lon":lon}).json()
    firstline= f" Here's the weather in {city_name}"
    new_forcast= []
    new_forcast.append(firstline)
    for element in forcast["list"]:
        text=element["dt_txt"]
        if "09:00:00" in text:
            #new_forcast.append(element)
            date= text.replace(" 09:00:00", "")
            desc= element["weather"][0]["description"]
            temk= element["main"]["temp"]
            temc=round((temk-273),2)
            finalstr= f"{date}: {desc} {temc}C"
            new_forcast.append(finalstr)

    final=" \n".join(new_forcast)
    return final
#print(weather_forecast(48.8588897,2.3200410217200766))

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)

    print(city)


    # TODO: Display weather forecast for a given city
    pass  # YOUR CODE HERE

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
