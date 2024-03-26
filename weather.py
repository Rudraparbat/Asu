import requests
import json
api_key= 'c24ebed86cb54b1bba2181902242403'
city = input("enter the name of your city : ")  
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
response = requests.get(url)
#print(response.text)
wea = json.loads(response.text)
def decor(function) :
	def wrapper(*args , **kwargs) :
		function(*args , **kwargs)
		print("THIS WEATHER REPORT WILL BE UPDATED IN EVERY 15 MINUTES ")
		a = "THANK YOU SO MUCH"
		print(a.center(100))
	return wrapper
@decor
def display() :
	print("LOCATION : ",wea["location"]["country"])
	print("CURRENT DATE AND TIME :",wea ['location']["localtime"])
	print("CURRENT TEMPARATURE :",wea ['current'] ['temp_c'],"°c")
	print("HUMIDITY :",wea["current"] ["humidity"],"%")
	print("FEELS LIKE :", wea["current"] ["feelslike_c"],"°c")
	print("CONDITION :",wea["current"]["condition"] ["text"])
	print("WIND SPEED :",wea["current"]["wind_kph"],"kph")
	a = wea["current"]["condition"]["icon"]
	


display()