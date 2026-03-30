from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime
from collections import defaultdict

import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    wines_from_xlsx = pd.read_excel('wine3.xlsx').fillna('').to_dict(orient='records')
    wines_by_category = defaultdict(list)

    for wine in wines_from_xlsx:
        wines_by_category[wine['Категория']].append(wine)

    age = datetime.now().year - 1920
    time = 'лет' if age % 10 == 0 or age % 10 >= 5 else 'года' if age % 10 >= 2 else 'год'

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(
        wines=wines_by_category,
        age=age,
        time=time
    )

    with open('index.html', 'w', encoding='utf8') as f:
        f.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
