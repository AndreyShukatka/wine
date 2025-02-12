import argparse
import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas import read_excel


def get_wines(wines):
    products = collections.defaultdict(list)
    for wine in wines:
        products[wine_products['Категория']].append(wine)
    return products


def calc_age_string():
    foundation_date = 1920
    current_date = datetime.datetime.now().year
    factory_age = current_date - foundation_date
    year_last_digit = str(factory_age)[-1]
    if year_last_digit in ['2', '3', '4']:
        return f'{factory_age} года'
    elif year_last_digit == '1':
        return f'{factory_age} год'
    else:
        return f'{factory_age} лет'


def enter_path():
    parser = argparse.ArgumentParser(
        description='Программа формирует страницу сайта-магазина по продаже крымских вин '
                    'на основе шаблона template.html и таблицы со списком вин в формате .xlsx'
    )
    parser.add_argument(
        '-wp ', '--wine_path', help='Путь к файлу cо списком продукции', default='wine.xlsx'
    )
    wine_path = parser.parse_args().wine_path
    return wine_path


if __name__ == '__main__':
    wines = read_excel(enter_path(), na_values=['N/A', 'NA'],
                       keep_default_na=False).to_dict(orient='records')
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(
        wine_map=get_wines(wines),
        company_age=calc_age_string()
    )


    with open('index.html', 'w', encoding='utf8') as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
