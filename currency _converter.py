from tkinter import * #From tkinter import everything
from PIL import Image
from PIL import ImageTk
import requests

'''
APPLICATION LOGIC
'''
# API live currency rates
def fetch_live_rates():
    try:
        liverates_api_url = "https://v6.exchangerate-api.com/v6/0f970505e8d9c2358f2620e2/latest/USD"

        # Remember to error control your API incase of when it fails 
        response = requests.get(liverates_api_url)
        response.raise_for_status()

        # Parse your response so that python can extract that information.
        return response.json()
    except Exception as e:
        return None #Returns None if there's an error
    


#Json response is a dictionary
live_rates = fetch_live_rates()

if live_rates:
    # Key data pulled from Json response
    exchange_rates = live_rates["conversion_rates"]
    base_currency = live_rates["base_code"]
    last_update = live_rates["time_last_update_utc"]
else:
    exchange_rates = {} 
    base_currency = {}
    last_update = {}

#Function to get the base(USD) currency rate of the currency to be converted
def firstcurrency_baserate():
    try:

        first_currency = "1234"
        while (len(first_currency) != 3) or (type(first_currency) != str):
            #first_currency = input("Enter first currency:\n").upper()
            first_currency = from_entry.get().upper().strip()
        else:
            return exchange_rates[first_currency], first_currency
    except:
        return None,'N/A'

# Function to get thw base(USD) currency rate of the target currency
def targetcurrency_baserate():
    try:
        target_currency = "5678"
        while (len(target_currency) != 3) or (type(target_currency) != str):
            #target_currency = input("Enter target currency:\n").upper()
            target_currency = to_entry.get().upper().strip()
        else:
            return exchange_rates[target_currency], target_currency
    except:
        return None,'N/A'

# Function to get target currency 
def calc_targetcurrency():
    try:
        b_rate,b_currency = firstcurrency_baserate()
        t_rate,t_currency = targetcurrency_baserate() 
        
        initial_amount="ZERO"
        while not initial_amount.isdigit():
            #initial_amount = input("Enter Amount:\n")
            initial_amount = amount_entry.get().strip()
        else:
            return round((t_rate/b_rate)*int(initial_amount),2),t_currency #read carefully to understand the parentheses
    except:
        return None,'N/A'
    
#Convert button function
def converter():
    result_value,currency_id = calc_targetcurrency()
    result_text = f"{result_value} {currency_id}"
    display_result.config(text=result_text)


#Instantiate an insance of a window
window = Tk()

#Set the geometry of your window(widthxheight)
window.geometry("500x550")
window.title("LE Currency Converter") #Set your application title

icon = PhotoImage(file='currency_converter_icon.png') # Create variable for your application's icon
window.iconphoto(True,icon) #Set image as application icon

window.config(background="#ffffff") #Set application background color

#Create App Label
app_label = Label(window, # Always include the canvas
              text="LE Currency Converter",
              font=('Montserrat', 20, 'bold'),
              fg="#b56a14",
              bg="#145364",
              bd=10,
              #relief=RAISED,
              padx= 80,
              pady=20,
              )
app_label.pack() #This line of code is essential to display your label on screen

#FROM Label
from_ = Label(window,text="From:")
from_.config(
    font=('Monospace',19,'bold'),
    fg='#b56a14',
    bg='#145364',
)
from_.place(x=10,y=100)

#Entry for From
from_entry = Entry()
from_entry.config(
    font=('Roboto Mono',20,),
    bg="#eef5f9",
    width=5,
)
from_entry.place(x=140,y=100)

#To Label
to_= Label(window,text='To:',
           font=('Monospace',19,'bold'),
           fg='#b56a14',
           bg='#145364',
           )
to_.place(x=10,y=150)

#Entry for To
to_entry = Entry()
to_entry.config(
    font=('Roboto Mono',20,),
    bg="#eef5f9",
    width=5,
)
to_entry.place(x=140,y=150)

#Amount Label
amount = Label(window,text='Amount:')
amount.config(
    font=('Monospace',19,'bold'),
    fg='#b56a14',
    bg='#145364',
    )
amount.place(x=10,y=220)

#Amount entry 
amount_entry = Entry()
amount_entry.config(
    font=('Roboto Mono',20,),
    bg="#eef5f9",
)
amount_entry.place(x=140,y=220)

#Result Label
result = Label(window,text="Result:")
result.config(
    font=('Roboto Mono',19,'bold'),
    fg='#b56a14',
    bg='#145364',
)
result.place(x=10,y=400)

#Display result label
display_result = Label(window,text="                            ",
                font=('Roboto Mono',20,),
                bg="#778187",
                )
display_result.place(x=140,y=400)

# Create an instance of the convert button
convert = Button(window, text="convert")
convert.config(
    command=converter,
    font=('Poppins',20, 'bold'),
    fg='#b56a14',
    bg='#145364',
    activeforeground='#b56a14',
    activebackground='#145364',
)
convert.place(x=190,y=300)

window.mainloop() #Places application window on screen
