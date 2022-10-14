from bs4 import BeautifulSoup

# read from html to a string
with open('test.html', 'r') as f:
    html_string = f.read()

# soup
soup = BeautifulSoup(html_string, 'html.parser')

tickers = []

# read each data cell and parse for the ticker name
for stock in soup.find_all("tr", class_="row-EdyDtqqh listRow"):
    data = str(stock)
    print(type(data))
    start = data.find(":") + 1
    end = data.find("\"", start)
    print(type(start))

    ticker = data[start:end]

    tickers.append(ticker)


print(tickers)