import random
import requests
import getDjid
import buyStonk

URL = "https://api.henrikdev.xyz/valorant/v1/mmr-history/na/snoopboopsnoop/8874"

stonks = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'TSLA', 'BRK.A', 'UNH', 'JNJ', 'XOM', 'V', 'WMT', 'META', 'LLY', 'CVX', 'JPM', 'PG', 'HD', 'NVDA', 'MA', 'ABBV', 'BAC', 'KO', 'PFE', 'MRK', 'PEP', 'COST', 'TMO', 'DHR', 'AVGO', 'ABT', 'MCD', 'TMUS', 'DIS', 'ORCL', 'CSCO', 'ACN', 'WFC', 'NEE', 'VZ', 'BMY', 'COP', 'CRM', 'TXN', 'UPS', 'NKE', 'SCHW', 'LIN', 'PM', 'ADBE', 'MS', 'AMGN', 'CMCSA', 'RTX', 'QCOM', 'LOW', 'UNP', 'HON', 'CVS', 'ELV', 'DE', 'LMT', 'MDT', 'INTU', 'IBM', 'T', 'AXP', 'INTC', 'GS', 'BX', 'SBUX', 'SPGI', 'PYPL', 'NFLX', 'CAT', 'ADP', 'AMD', 'CI', 'GILD', 'BLK', 'REGN', 'SYK', 'MO', 'C', 'NOC', 'BA', 'CB', 'MDLZ', 'EL', 'MMC', 'VRTX', 'NOW', 'TJX', 'PGR', 'EOG', 'ADI', 'TGT', 'GE', 'ABNB', 'SO', 'DUK']

# get 2 random positions in stonks
rand1 = random.randint(0, len(stonks)-1)
rand2 = random.randint(0, len(stonks)-1)
while(rand1 == rand2) :
    rand2 = random.randint(0, len(stonks)-1)

# get the ticker names
stock1 = stonks[rand1]
stock2 = stonks[rand2]

print("stock options: \n")
print(stock1 + ", " + stock2 + '\n')

buy = random.randint(0, 1)
stocktobuy = stock1
if(buy == 1):
    stocktobuy = stock2

print("buying " + stocktobuy)

djid = getDjid.djid(stocktobuy)
buyStonk.buy(djid, "1")


# r = requests.get(url = URL)

# data = r.json()


#print(data['data'][1]['mmr_change_to_last_game'])

# wl = data['data'][1]['mmr_change_to_last_game']
# time = data['data'][1]['date_raw']

# print(str(wl) + ", " + str(time))