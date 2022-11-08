import random
import requests
import getDjid
import buyStonk
import marketwatch
import time
import json

historyURL = "https://api.henrikdev.xyz/valorant/v3/matches/na/snoopboopsnoop/8874"
mmrURL = "https://api.henrikdev.xyz/valorant/v1/mmr-history/na/snoopboopsnoop/8874"

stonks = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA', 'UNH', 'JNJ', 'XOM', 'V', 'WMT', 'META', 'LLY', 'CVX', 'JPM', 'PG', 'HD', 'NVDA', 'MA', 'ABBV', 'BAC', 'KO', 'PFE', 'MRK', 'PEP', 'COST', 'TMO', 'DHR', 'AVGO', 'ABT', 'MCD', 'TMUS', 'DIS', 'ORCL', 'CSCO', 'ACN', 'WFC', 'NEE', 'VZ', 'BMY', 'COP', 'CRM', 'TXN', 'UPS', 'NKE', 'SCHW', 'LIN', 'PM', 'ADBE', 'MS', 'AMGN', 'CMCSA', 'RTX', 'QCOM', 'LOW', 'UNP', 'HON', 'CVS', 'ELV', 'DE', 'LMT', 'MDT', 'INTU', 'IBM', 'T', 'AXP', 'INTC', 'GS', 'BX', 'SBUX', 'SPGI', 'PYPL', 'NFLX', 'CAT', 'ADP', 'AMD', 'CI', 'GILD', 'BLK', 'REGN', 'SYK', 'MO', 'C', 'NOC', 'BA', 'CB', 'MDLZ', 'EL', 'MMC', 'VRTX', 'NOW', 'TJX', 'PGR', 'EOG', 'ADI', 'TGT', 'GE', 'ABNB', 'SO', 'DUK']

# get 2 random positions in stonks
rand1 = random.randint(0, len(stonks)-1)
rand2 = random.randint(0, len(stonks)-1)
while(rand1 == rand2) :
    rand2 = random.randint(0, len(stonks)-1)

# get the ticker names
stock1 = stonks[rand1]
stock2 = stonks[rand2]
print("---------------------------------------------------------------------------------------------")
print("WELCOME TO THE VALORANT STOCK MARKET, WHERE YOU LET YOUR BOOSTED ASS CONTROL STOCK PURCHASES")
print("---------------------------------------------------------------------------------------------\n")
time.sleep(1)
print("LET'S SEE WHAT LUCK YOU HAVE TODAY...")
time.sleep(1)
print(f"IF YOU WIN YOUR VALORANT MATCH, YOU'LL BE THE LUCKY OWNER OF {stock1} STOCK!")
time.sleep(1)
print(f"IF YOU HAPPEN TO LOSE, HOWEVER, YOU'LL GO HOME WITH SOME {stock2} STOCK. EVERYONE'S A WINNER!\n")
time.sleep(1)
print("ALRIGHT, TIME TO PLAY! I'LL KEEP CHECKING UNTIL YOU'VE EITHER WON OR LOST YOUR NEXT GAME!\n")
time.sleep(60)
# buy = random.randint(0, 1)
# stocktobuy = stock1
# if(buy == 1):
#     stocktobuy = stock2

# print("buying " + stocktobuy)

#djid = getDjid.djid(stocktobuy)
#buyStonk.buy(djid, 1)

r = requests.get(url = historyURL).json()
#print(json.dumps(r, indent=2))
#print(r.keys())
#print(r["data"][0].keys())
#print(r["data"][0]["metadata"]["matchid"])


#print(kd)

#print(r["data"][0]["players"]["all_players"].keys())

# print(json.dumps(r, indent=2))

#["data"][0]["players"]["all_players"][0]

lastID = r["data"][0]["metadata"]["matchid"]
newID = lastID

while(newID == lastID):
    print("No new games. Checking again in 1 minute.")
    time.sleep(60)
    print("Checking for new game...")
    r = requests.get(url = historyURL).json()
    #print(r.keys())
    found = False
    while found is False:
        try:
            newID = r["data"][0]["metadata"]["matchid"]
            found = True
        except:
            print("Could not get player data. Trying again in 30 seconds.")
            time.sleep(30)
            r = requests.get(url = historyURL).json()
    

for i in r["data"][0]["players"]["all_players"]: 
    if(i["name"] == "snoopboopsnoop"):
        kd = (int(i["stats"]["kills"]) / int(i["stats"]["deaths"]))

mmr = requests.get(url=mmrURL).json()

#print(mmr.keys())
elo = mmr['data'][0]['mmr_change_to_last_game']

if(elo > 0): 
    print("Congratulations! Time to buy " + stock1 + "!")
    stocktobuy = stock1
else: 
    print("Uh oh. Looks like you're buying " + stock2 + "...")
    stocktobuy = stock2

#print("buying " + stocktobuy)

djid = getDjid.djid(stocktobuy)
price = djid[1]
djid = djid[0]

shares = round((2000 * kd) / price)

print(f'Buying {shares} shares of {stocktobuy}...')

buyStonk.buy(djid, shares)

k=input("press close to exit")