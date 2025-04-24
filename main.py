import requests
from colorama import Fore, Style

print("💱 Currency Converter")

from_currency = input("From currency (e.g. USD): ").upper()
to_currency = input("To currency (e.g. BDT): ").upper()
try:
    amount = float(input("Amount to convert: "))
except ValueError:
    print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)
    exit()
API_KEY = "YOUR API KEY"
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    result = data['conversion_rates'][f'{to_currency}']
    print(Fore.GREEN + f"\n{amount} {from_currency} = {result * amount:.2f} {to_currency}" + Style.RESET_ALL)

else:
    print(Fore.RED + "Error retrieving conversion data!" + Style.RESET_ALL)