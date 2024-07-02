import requests
from bs4 import BeautifulSoup

class ExchangeClient:
    def __init__(self):
        self.base_url = 'https://www.doviz.com/'

    def scrape_exchange_rate(self, currency_name):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            rates = soup.find_all('div', class_='item')
            for rate in rates:
                name_tag = rate.find('span', class_='name')
                value_tag = rate.find('span', class_='value')
                if name_tag and value_tag:
                    currency = name_tag.get_text(strip=True).upper()
                    value = value_tag.get_text(strip=True)
                    if currency_name.upper() in currency:
                        return {currency: value}
            return None
        else:
            return None
