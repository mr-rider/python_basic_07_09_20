import requests

class SomeError(Exception):
    def __init__(self, text = None):
        self.text = text

for num in range(50):
    if num == 15:
        pass #raise SomeError('Some text this error')


class Product:
    id = ''
    name = ''
    def __init__(self, data: dict):
        for key, value in data.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.id}: {self.name}'

class Parser:
    __headers = {
        "User-Agent": "Mozilla/5.0 ",
    }
    __params = {
        'records_per_page': 50,
        'catecories': '',
    }

    def __init__(self, stat_url:str):
        self.__start_url = stat_url
        self.products = []

    def parse(self):
        url = self.__start_url
        while url:
            response = requests.get(url, params=self.__params, headers = self.__headers )
            data = response.json()
            url = None #data['next']
            self.products.extend(Product(itm) for itm in data['results'])

if __name__ == '__main__':
    parser = Parser('https://5ka.ru/api/v2/special_offers/')
    parser.parse()
    print(1)