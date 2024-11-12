#!/usr/bin/env python3

import jinja2
import pathlib


TEMPLATES_PATH = pathlib.Path(__file__).parent / 'templates'
OUTPUT_PATH = pathlib.Path(__file__).parent / 'html'


def main():
    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_PATH))
    template = environment.get_template('index.html')
    text = template.render({'tg_post_num_to_link': lambda x: f'https://t.me/s/stepanzh_blog/{x}'})

    with open(OUTPUT_PATH / 'index.html', 'w') as io:
        print(text, file=io)

if __name__ == '__main__':
    main()
