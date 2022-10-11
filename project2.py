import requests

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=a07df84c3cf13626a8299e010c9472ac&units=imperial"

city = input("Enter your city: ")
zipcode = input("Enter your zipcode: ")
print(" ...Weather App... ")


def weather():

  response = requests.get(url).json()
  temp = requests.get(url).json()
  print(response)
  print(temp)


while (True):

  zip = input("Enter zipcode (Press enter to leave the field blank): ")
  city = input("Enter city: ")
  if (zip.strip() or city.strip()):
    break
  else:
    print("enter valid city/zipcode")

response = requests.get(base_url).json()
temp = requests.get(base_url).json()
print(response)
print(temp)
