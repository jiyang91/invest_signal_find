import requests

response = requests.get("https://v6.exchangerate-api.com/v6/6efc1973554c936722ab8b3b/latest/USD").json()

exchange_rate = response["conversion_rates"]["KRW"]
print("Exchange rate USD to KRW: ", exchange_rate)
