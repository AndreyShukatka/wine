import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas import read_excel

Current_date = datetime.datetime.now().year
foundation_date = 1920


def all_alcohol():
    products = collections.defaultdict(list)
    for wine_products in wines:
        products[wine_products['Категория']].append(wine_products)
    return products


def ending_word(last_digit):
    if last_digit == 0 or 5 <= last_digit <= 9:
        renderer_page = template.render(year=how_many_years,
                                        inscription='лет',
                                        wines=alcohols)
        return renderer_page
    elif last_digit == 1:
        renderer_page = template.render(year=how_many_years,
                                        inscription='год',
                                        wines=alcohols)
        return renderer_page
    else:
        renderer_page = template.render(year=how_many_years,
                                        inscription='года',
                                        wines=alcohols)
        return renderer_page


if __name__ == '__main__':
    wines = read_excel('wine.xlsx', na_values=['N/A', 'NA'],
                       keep_default_na=False).to_dict(orient='records')
    env = Environment(loader=FileSystemLoader('.'),
                      autoescape=select_autoescape(['html', 'xml'])
                      )
    template = env.get_template('template.html')
    how_many_years = Current_date - foundation_date
    last_digit_year = how_many_years % 10
    alcohols = all_alcohol()

    with open('index.html', 'w', encoding='utf8') as file:
        file.write(ending_word(last_digit_year))

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
