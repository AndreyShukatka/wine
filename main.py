from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
from pandas import read_excel
import collections

wines = read_excel('wine2.xlsx', na_values=['N/A', 'NA'],
                   keep_default_na=False).to_dict(orient='records')
env = Environment(loader=FileSystemLoader('.'),
                  autoescape=select_autoescape(['html', 'xml'])
                  )


def all_alcohol():
    products = collections.defaultdict(list)
    types_wine = list()
    categories = dict()
    for category in wines:
        categories.setdefault(category['Категория'])
    for types in categories:
        types_wine.append(types)
    for wine_products in wines:
        products[wine_products['Категория']].append(wine_products)
    return products


def ending_word(last_digit):
    if last_digit == 0 or 5 <= last_digit <= 9:
        renderer_page = template.render(year=year,
                                        inscription='лет',
                                        wines=wines)
        return renderer_page
    elif last_digit == 1:
        renderer_page = template.render(year=year,
                                        inscription='год',
                                        wines=wines)
        return renderer_page
    else:
        renderer_page = template.render(year=year,
                                        inscription='года',
                                        wines=wines)
        return renderer_page


if __name__ == '__main__':
    template = env.get_template('template.html')
    now = datetime.datetime.now().year
    start_date = 1920
    year = now - start_date
    last_digit = year % 10
    wines = all_alcohol()

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(ending_word(last_digit))

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
