import requests
 
base_url = "http://api.openweathermap.org/data/2.5/weather?appid=a07df84c3cf13626a8299e010c9472ac&units=imperial"
country_code='us'
def weather():
 
    print("############ Weather App ##########")
 
    while(True):
        zip = input("Enter zipcode (Press enter to leave the field blank): ")
        city = input("Enter city: ")
        if (zip.strip() or city.strip()):
            break
        else:
            print("enter valid city/zipcode")
 
    #compose the url for the service
    if city.strip():
        #api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
        complete_url = base_url + "&q=" + city
    elif zip:
        #api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}&appid={API key}
        complete_url = base_url + "&szip=" + zip + "," + country_code
 
    #send a request to the service
    y = getWeatherJson(complete_url)
    #validate the response and print to output
    if len(y) > 0:
        current_temp = getTemperature(y)
        current_pressure = getPressure(y)
        current_humidity = getHumidity(y)
        # current_time = y["currentDateTime"]
 
        # print(current_time, "date time")
        print ("++Successfully connected to the service++")
        print(current_humidity, "humidity")
        print(current_pressure, "pressure")
        print(current_temp, "temp")
 
 
def getWeatherJson(url):
    try:
        print("Connecting to the below url...")
        print(url)
        response = requests.get(url)
        x = response.json()
        y = x["main"]
    except:
        y = {}
        print ("--Error connecting to the service--")
 
    return y
 
 
def getTemperature(json):
    return json['temp']
 
 
def getPressure(json):
    return json["pressure"]
 
 
def getHumidity(json):
    return json["humidity"]
 
weather()