import urllib.request
import json

url="https://api.exchangeratesapi.io/latest"
request =urllib.request.Request(url)
response = urllib.request.urlopen(request)
html = response.read()
currency_data = json.loads(html)
print(json.dumps(currency_data))
print("\n\n",currency_data['rates'])
Euro_rate = {}
for items in currency_data['rates']:
	country = items 
	exchange_rate = currency_data['rates'][items]
	print(country,exchange_rate)
	Euro_rate[country] = exchange_rate
try:
	value = int(input("Enter the amount you want to convert : "))
	country_base = input("Enter the base currency: ")
	country_end = input("Enter the currency in which you want convert your amount into: ")
	if country_base in Euro_rate and country_end in Euro_rate:
		result = float(value) * float(Euro_rate[country_end] / Euro_rate[country_base])
		print(f"{value} {country_base} is equal to {result} {country_end}")
	else:
		print("Invalid input")
except ValueError as ex:
	print("Invalid input",ex)



