import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

entitlementToken = os.getenv("ENTITLEMENT_TOKEN")
cKey = os.getenv("CKEY")

payload={}
headers = {
  'Sec-Fetch-Site': 'cross-site'
}

def djid(ticker):
    url = f'https://api.wsj.net/api/dylan/quotes/v2/comp/quoteByDialect?dialect=charting&needed=CompositeTrading&MaxInstrumentMatches=1&accept=application/json&EntitlementToken={entitlementToken}&ckey={cKey}&dialects=djid&id={ticker}'
    response = requests.request("GET", url, headers=headers, data=payload).json()

    return response["InstrumentResponses"][0]["Matches"][0]["DialectSymbols"][0]["Symbols"][0], response["InstrumentResponses"][0]["Matches"][0]["CompositeTrading"]["Last"]["Price"]["Value"]
