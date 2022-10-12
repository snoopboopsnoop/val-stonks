from bs4 import BeautifulSoup

with open('test.html', 'r') as f:
    html_string = f.read()

soup = BeautifulSoup(html_string, 'html.parser')

for stock in soup.find_all("tr", class_="row-EdyDtqqh listRow"):
    start = int(stock.find("data-rowkey") or 0) + 13
    end = int(stock.find("\">", start) or 0)

    print(stock)
    print("\n")
    print(str(start) + " " + str(end) + "\n")