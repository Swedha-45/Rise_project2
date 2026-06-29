import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
city = input("Enter city name: ")
url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'


response = requests.get(url)
if response.status_code==200:
    data=response.json()
    print(f"Description: {data['weather'][0]['description']}")
    print(f"the current Temperature is : {data['main']['temp']}°C")
    print(f"the current Humidity is :  { data ['main']['humidity']}%")