from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime
from collections import defaultdict
import os

import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape
import argparse


def main():
    parser = argparse.ArgumentParser(description='Wine site')
    parser.add_argument(
        '--wine-file',
        default=os.getenv('wine.xlsx'),
        help='Путь к Excel файлу с данными (по умолчанию: wine.xlsx)'
    )

    args = parser.parse_args()

    wines_from_xlsx = pd.read_excel(args.wine_file).fillna('').to_dict(orient='records')
    wines_by_category = defaultdict(list)

    for wine in wines_from_xlsx:
        wines_by_category[wine['Категория']].append(wine)

    winery_age = datetime.now().year - 1920
    age_word = 'лет' if winery_age % 10 == 0 or winery_age % 10 >= 5 else 'года' if winery_age % 10 >= 2 else 'год'

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(
        wines=wines_by_category,
        age=winery_age,
        time=age_word
    )

    with open('index.html', 'w', encoding='utf8') as f:
        f.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
