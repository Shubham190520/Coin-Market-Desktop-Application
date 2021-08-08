# str = 'Perfect-Plan-B:0.7541'
# pos = str.find(':')
# result = str[pos+1:]
# floating_number = float(result)
# print(floating_number)

pycrypto = Tk()
pycrypto.title("My Crypto Portfolio")
pycrypto.iconbitmap('favicon.ico')

def font_color(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"


def my_portfolio():
    api_request = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=300&convert=USD&CMC_PRO_API_KEY=135e34cb-79b4-40df-8af3-be11f8a93d24")
    api = json.loads(api_request.content)

    coins = [
      {
        "symbol": "BTC",
        "amount_owned": 2,
        "price_per_coin": 3200
      },
      {
        "symbol": "EOS",
        "amount_owned": 100,
        "price_per_coin": 2.75
      },
      {
         "symbol": "LTC",
         "amount_owned": 75,
         "price_per_coin": 25
      },
      {
          "symbol": "XMR",
          "amount_owned": 10,
          "price_per_coin": 48.05
      }
   ]
      total_pl = 0
      coin_row = 1
      total_current_value = 0

for i in range(0, 300):
    for coin in coins:
        if api["data"][i]["symbol"] == coin["symbol"]:
            total_paid = coin["amount_owned"] * coin["price_per_coin"]
            current_value = coin["amount_owned"] * api["data"][0]["quote"]["USD"]["price"]
            pl_per_coin = api["data"][0]["quote"]["USD"]["price"] - coin["price_per_coin"]
            total_pl_coin = pl_per_coin * coin["amount_owned"]

            total_pl = total_pl + total_pl_coin
            total_current_value = total_current_value + current_value

               # print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
               # print("Price - ${0: .2f}".format(api["data"][0]["quote"]["USD"]["price"]))
               # print("Number of coins: ",coin["amount_owned"])
               # print("Total Amount paid: ", "${0:.2f}".format(total_paid))
               # print("Current Value: ", "${0:.2f}".format(current_value))
               # print("P/L per coin: ", "${0:.2f}".format(pl_per_coin))
               # print("Total with P/L coin: ", "${0:.2f}".format(total_pl_coin))
               # print("----------------------")

            name = Label(pycrypto, text=api["data"][i]["symbol"], bg="white", fg="black", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
            name.grid(row=coin_row, column=0, sticky=N+S+E+W)

            price = Label(pycrypto, text="${0: .2f}".format(api["data"][0]["quote"]["USD"]["price"]), bg="white", fg="black", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
            price.grid(row=coin_row, column=1, sticky=N+S+E+W)

            no_coins = Label(pycrypto, text= coin["amount_owned"], bg="white", fg="black", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
            no_coins.grid(row=coin_row, column=2, sticky=N+S+E+W)

            amount_paid = Label(pycrypto, text="${0:.2f}".format(total_paid), bg="white", fg="black", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
            amount_paid.grid(row=coin_row, column=3, sticky=N+S+E+W)

            current_val = Label(pycrypto, text="${0:.2f}".format(current_value), bg="white", fg="black", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
            current_val.grid(row=coin_row, column=4, sticky=N+S+E+W)

            pl_coin = Label(pycrypto, text="${0:.2f}".format(pl_per_coin), bg="white", fg=font_color(float("{0:.2f}".format(pl_per_coin))), font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
            pl_coin.grid(row=coin_row, column=5, sticky=N+S+E+W)

            totalpl = Label(pycrypto, text="${0:.2f}".format(total_pl_coin), bg="white", fg=font_color(float("{0:.2f}".format(total_pl_coin))), font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
            totalpl.grid(row=coin_row, column=6, sticky=N+S+E+W)

            coin_row = coin_row + 1

        totalpl = Label(pycrypto, text="${0:.2f}".format(total_current_value), bg="white", fg="black", font="Lato 12 bold",padx="5", pady="5", borderwidth=2, relief="groove")
        totalpl.grid(row=coin_row, column=4, sticky=N+S+E+W)

        totalpl = Label(pycrypto, text="${0:.2f}".format(total_pl), bg="white", fg=font_color(float("{0:.2f}".format(total_pl))), font="Lato 12 bold",padx="5", pady="5", borderwidth=2, relief="groove")
        totalpl.grid(row=coin_row, column=6, sticky=N+S+E+W)

api =" "

update = Button(pycrypto, text="Update", bg="white", fg="black", command=my_portfolio, font="Lato 12 bold", padx="5", pady="5",borderwidth=2, relief="groove")
update.grid(row=coin_row + 1, column=6, sticky=N+S+E+W)


         # print("Total P/L For Portfolio", "${0:.2f}".format(total_pl))

name = Label(pycrypto, text="Coin name", bg="navyblue", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=0, sticky=N+S+E+W)

price = Label(pycrypto, text="Price" , bg="navyblue", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
price.grid(row=0, column=1, sticky=N+S+E+W)

no_coins = Label(pycrypto, text="Coins owned", bg="navyblue", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
no_coins.grid(row=0, column=2, sticky=N + S + E + W)

amount_paid = Label(pycrypto, text="Total Amount Paid", bg="navyblue", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
amount_paid.grid(row=0, column=3, sticky=N + S + E + W)

current_val = Label(pycrypto, text="Current Value", bg="navyblue", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
current_val.grid(row=0, column=4, sticky=N + S + E + W)

pl_coin = Label(pycrypto, text="P/L Per Coin", bg="navyblue", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
pl_coin.grid(row=0, column=5, sticky=N + S + E + W)

totalpl = Label(pycrypto, text="Total P/L With Coin", bg="navyblue", fg="white", font="Lato 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
totalpl.grid(row=0, column=6, sticky=N + S + E + W)

my_portfolio()
pycrypto.mainloop()
print("Program Completed")

