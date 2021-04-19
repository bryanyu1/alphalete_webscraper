from urllib.request import urlopen 
from bs4 import BeautifulSoup as soup 
 
url_scrape = "https://alphaleteathletics.com/collections/mens"

request_page = urlopen(url_scrape) 
page_html = request_page.read()
request_page.close()

html_soup = soup(page_html, "html.parser") 

products = html_soup.find_all("div", class_="product-item-details")

filename = "Alphalete Products.csv"
f = open(filename, "w")

headers = "Product Name, Colour, Current Price, Original Price \n"

f.write(headers)

for p in products:
    name = p.find("h3").text.strip()
    colour = p.find("p", class_="color").text.strip()
    og_price = p.find("span", class_="money").text.strip()
    
    if p.find("span", class_="rrp card-sale-price") is None:
        cur_price = og_price
    else:
        cur_price = p.find("span", class_="rrp card-sale-price").text.strip()

    f.write(name +  ", " + colour + ", " + cur_price + ", " + og_price + "\n")

f.close()
