import requests
def fetch_live_rates():
    weatherapi_url = "https://v6.exchangerate-api.com/v6/0f970505e8d9c2358f2620e2/latest/USD"

    # Remember to error control your API incase of when it fails 
    response = requests.get(weatherapi_url)
    print(response.status_code)

# Parse your response so that python can extract that information.
    return response.json()

#Json response is a dictionary
live_rates = fetch_live_rates()
#print(live_rates)
base_currency = live_rates["base_code"]
last_update = live_rates["time_last_update_utc"]
exchange_rates = live_rates["conversion_rates"]

#print(base_currency)
#print(last_update)

#print(exchange_rates)
#print(exchange_rates["NGN"])
'''
You can implement user input above instead of "NGN"
'''
#Function to get the base(USD) currency rate of the currency to be converted
def firstcurrency_baserate():
    first_currency = "1234"
    while (len(first_currency) != 3) or (type(first_currency) != str):
        first_currency = input("Enter first currency:\n").upper()
    else:
        return [exchange_rates[first_currency], first_currency]

# Function to get thw base(USD) currency rate of the target currency
def targetcurrency_baserate():
    target_currency = "5678"
    while (len(target_currency) != 3) or (type(target_currency) != str):
        target_currency = input("Enter target currency:\n").upper()
    else:
        return [exchange_rates[target_currency], target_currency]


first_cur=firstcurrency_baserate()
b = first_cur[0]
#print(b)

target = targetcurrency_baserate()
a = target[0]
#print(a)

def calc_targetcurrency():
    initial_amount="ZERO"
    while not initial_amount.isdigit():
        initial_amount = input("Enter Amount:\n")
    else:
        return round((a/b)*int(initial_amount),3),initial_amount #read carefully to understand the parentheses

target_amount = calc_targetcurrency()
print(f"{target_amount[1]} {first_cur[1]} = {target_amount[0]} {target[1]}") #Displays amount and currency
