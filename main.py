import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas import read_excel


def all_alcohol():
    products = collections.defaultdict(list)
    for wine_products in wines:
        products[wine_products['Категория']].append(wine_products)
    return products


def year_view():
    foundation_date = 1920
    how_many_years = current_date - foundation_date
    year_last_digit = str(how_many_years)[-1]
    if year_last_digit in ['2', '3', '4']:
        return f'{how_many_years} года'
    elif year_last_digit == '1':
        return f'{how_many_years} год'
    else:
        return f'{how_many_years} лет'


if __name__ == '__main__':
    wines = read_excel('wine.xlsx', na_values=['N/A', 'NA'],
                       keep_default_na=False).to_dict(orient='records')
    env = Environment(loader=FileSystemLoader('.'),
                      autoescape=select_autoescape(['html', 'xml'])
                      )
    template = env.get_template('template.html')
    current_date = datetime.datetime.now().year
    rendered_page = template.render(alcohols=all_alcohol(),
                                    company_age=year_view())


    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
