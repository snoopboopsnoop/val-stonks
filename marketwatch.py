import requests
from dotenv import load_dotenv
import os
import json
from bs4 import BeautifulSoup
import urllib

class MarketWatch:
    def __init__(self, email, password, game, debug = False):
        self.debug = debug
        self.game = game
        self.session = requests.Session()

        url = f'https://www.marketwatch.com/'
        payload = {}
        headers = {}
        response = self.session.get(url, headers=headers, data=payload)

        url = f'https://accounts.marketwatch.com/login?target=https%3A%2F%2Fwww.marketwatch.com%2F'

        payload = {}
        headers = {}

        response = self.session.get(url, headers=headers, data=payload)

        #print(f'{response.history[1].headers["location"]}\n\n')
        redirect_url = response.history[1].headers["location"]
        id_start = redirect_url.find("client_id")+10
        id_end = redirect_url.find('&', id_start)
        id = redirect_url[id_start : id_end]

        state_start = redirect_url.find("state")+6
        state_end = redirect_url.find('&', state_start)
        state = redirect_url[state_start : state_end]

        nonce_start = redirect_url.find("nonce")+6
        nonce_end = redirect_url.find("&", nonce_start)
        nonce = redirect_url[nonce_start : nonce_end]

        #print(f'{id}\n\n{state}')

        url = f'https://sso.accounts.dowjones.com/error/login-html-onload?'
        payload = {
            "methodName" : "ContinuteWithEmail",
            "cookieEnabled" : 'true',
            'nonce': nonce,
            'state': state,
            'client': id,
            'protocol': 'oauth2',
            'response_type' : 'code',
            'redirect_uri': 'https://accounts.marketwatch.com/auth/sso/login',
        }
        response = self.session.get(url, headers=headers, data=payload, cookies=self.session.cookies)

        print(response.headers)

        print('\n\n')


        url = f'https://sso.accounts.dowjones.com/login-page?'
        payload = {
            'username': email,
            'password': password,
        }
        response = self.session.get(url, headers=headers, data=payload, cookies=self.session.cookies)

        print(response.headers)

        print('\n\n')

        print(self.session.cookies.get_dict())
        print('\n\n')


        login_url = "https://sso.accounts.dowjones.com/usernamepassword/login"

        payload = json.dumps({
        "client_id": id,
        "connection": "DJ1dap",
        "nonce": nonce,
        "password": password,
        "protocol": "oauth2",
        "redirect_uri": "https://accounts.marketwatch.com/auth/sso/login",
        "response-type": "code",
        "scope" : "openid idp_id roles email given_name family_name djid djUsername djStatus trackid tags prts suuid createTimestamp",
        "state" : state,
        "tenant": "sso",
        "username": email,
        })
        headers = {
            "X-REMOTE-USER" : email,
            "x-_dj-_client__id" : id,
            "x-_oidc-_provider": "localop",
            'content-type': 'application/json',
        }

        response = self.session.post(login_url, headers=headers, data=payload, cookies=self.session.cookies)

        # print(response.headers)
        # print('\n\n')

        # print(self.session.cookies.get_dict())
        # print('\n\n')

        soup = BeautifulSoup(response.text, 'html.parser')

        # print(soup.prettify())
        # print('\n\n')

        inputs = soup.find_all("input")

        token = inputs[0]["value"]
        params = inputs[1]["value"]

        # print(token)
        # print('\n\n')
        # print(params)

        auth_url = "https://sso.accounts.dowjones.com/postauth/handler"
        payload = {
            "token": token,
            "params": urllib.parse.quote(json.dumps({
                "response_type" : "code",
                "client_id": id,
                "redirect_uri": "https://accounts.marketwatch.com/auth/sso/login",
                "state" : state,
                "nonce" : nonce,
            })),
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        # print(payload)
        # print('\n\n')

        response = self.session.post(auth_url, headers=headers, data=payload, cookies=self.session.cookies, allow_redirects=True)

        print(response.headers)
        
        print(response.history[1].headers)
        print('\n\n')

        #print(self.session.cookies.get_dict())

    def buy(self, djid, shares):
        ledgerID = os.getenv("LEDGER_ID")
        gameID = os.getenv("GAME_ID")
        cookie = os.getenv("COOKIE")

        url = f'https://vse-api.marketwatch.com/v1/games/{gameID}/ledgers/{ledgerID}/trades'
        payload = json.dumps({
            "djid": djid,
            "ledgerId": ledgerID,
            "tradeType": "Buy",
            "shares": f'{shares}',
            "expiresEndOfDay": False,
            "orderType": "Market"
        })
        headers = {
            'content-type': 'application/json',
            'cookie': cookie,
        }
        response = self.session.post(url, headers=headers, data=payload)

        print(response.text)

        # if(response["data"]["status"] == "Submitted"):
        #     print("Purchased " + str(response["data"]["shares"]) + " shares")
        # else:
        #     print("Failed to purchase stonk. Maybe your dogshit ass cookies reset? idfk")
        


        
