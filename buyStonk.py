import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

ledgerID = os.getenv("LEDGER_ID")
gameID = os.getenv("GAME_ID")
cookie = os.getenv("COOKIE")

def buy(djid, shares):
    url = f'https://vse-api.marketwatch.com/v1/games/{gameID}/ledgers/{ledgerID}/trades'
    payload = json.dumps({
        "djid": djid,
        "ledgerId": ledgerID,
        "tradeType": "Buy",
        "shares": shares,
        "expiresEndOfDay": False,
        "orderType": "Market"
    })
    headers = {
        'content-type': 'application/json',
        'cookie': cookie,
    }
    response = requests.request("POST", url, headers=headers, data=payload).json()

    if(response["data"]["status"] == "Submitted"):
        print("Purchased " + str(response["data"]["shares"]) + " shares")
    else:
        print("Failed to purchase stonk. Maybe your dogshit ass cookies reset? idfk")
    
