import streamlit as st
import requests
st.set_page_config(page_title="Weatherapi",page_icon=":sunny:")
WMO_CODES = {
    0:"Clear Sky",
    1: "Mainly Clear",
    2: "Partly cloudy",
    3: "Overcast",
    45:"fog",
    48:"Depositing rime fog",
    51: "Light drizzle",
    53:"Moderate drizzle",
    55:"Dense drizzle",
    56:"Light freezing drizzle",
    57:"Dense freezing drizzle",
    61:"Slight rain",
    63:"Moderate rain",
    65:"Heavy rain",
    66:"Light freezing rain",
    67:"Heavy freezing rain",
    71:"Slight snow fall",
    73:"Moderate snow fall",
    75:"Heavy snow fall",
    77:"Snow grains",
    80:"Slight rain showers",
    81:"Moderate rain showers",
    82:"Violent rain showers",
    85:"Slight snow showers",
    86:"Heavsnow showers",
    90:"Thunderstorm with slight rain",
    91:"Thunderstorm with Moderate rain",
    92:"Thunderstorm with heavy rain",
    95:"Thunderstorm with slight or moderate rain",
    96:"Thunderstorm with slight hail",

}
def get_WMO(code):
    return WMO_CODES.get(code,"Unknown weather Condition")
def wind_direction(degree):
    directions = ["N","NE","E","SE","S","SW","W","NW"]
    deg = round(degree/45) % 8
    return directions[deg]

# API calls
def geocode(city):
    r = requests.get("https://geocoding-api.open-meteo.com/v1/search",params = {"name":city,"count":5,"language":"en","format":"json"},timeout = 8,)
    r.raise_for_status() #200:success , 300:redirecting,400 client error,500:server error
    return r.json().get("results",[])

def fetch_weather(lat,lon):
    r=requests.get("https://api.open-meteo.com/v1/forecast",
                   params= {
                       "latitude":lat,
                       "longitude":lon,
                       "current":["temperature_2m","apparent_temperature","relative_humidity_2m","wind_speed_10m","wind_direction_10m","weather_code","precipitation","uv_index",],
                       "daily":["temperature_2m_max","temperature_2m_min",
                                "precipitation_sum",
                                "uv_index_max",
                                "weather_code",],
                       "hourly":["temperature_2m",
                                 "precipitation_probability",],
                       "timezone":"auto",
                       "forecast_days":7
                   },timeout = 10,
                   )
    r.raise_for_status()
    return r.json()

#UI components
st.title("Weather App :sunny:")
st.caption("Get the current weather and 7-days forecast for any city in the world.")

city_input=st.text_input("Enter a city name", placeholder="e.g. New York, Tokyo, Paris")
unit=st.radio("Select temperature unit",("Celsius","Fahrenheit"),horizontal=True)
