from bs4 import BeautifulSoup
import requests

def web_scraper():
  url = "https://quotes.toscrape.com/"
  response = requests.get(url)
  raw_html = response.text
  soup = BeautifulSoup(raw_html, "html.parser")
  quotes = soup.find_all("div", class_ = "quote")
  scraped_data = []

  for quote in quotes:
    scraped_quotes = quote.find("span", class_ = "text").text
    author = quote.find("small", class_ = "author").text
    working_dict = {f'Quotes': scraped_quotes, 'Author': author}
    scraped_data.append(working_dict)

  return scraped_data

final_data = web_scraper()

with open('quotes.txt', mode = 'w') as file:
  for line in final_data:
    final_list = f"Quote: {line['Quotes']}, Author: {line['Author']}\n"
    file.write(final_list)
    print(final_list)

