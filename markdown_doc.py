#!/usr/bin/env python

import argparse
import sys
import json

import jinja2
import markdown

TEMPLATE = "{{content}}"

def parse_args(args=None):
    d = 'Make a complete, styled HTML document from a Markdown file.'
    parser = argparse.ArgumentParser(description=d)
    parser.add_argument('mdfile', type=argparse.FileType('rb'), nargs='?',
                        default=sys.stdin,
                        help='File to convert. Defaults to stdin.')
    parser.add_argument('-o', '--out', type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='Output file name. Defaults to stdout.')
    return parser.parse_args(args)


def main(args=None):
    args = parse_args(args)
    md = args.mdfile.read().decode('utf-8')
    extensions = ['extra', 'smarty']
    html = markdown.markdown(md, extensions=extensions, output_format='html5')
    
    doc = jinja2.Template(TEMPLATE).render(content=html)
    doc = json.dumps(doc)
    args.out.write(doc)


if __name__ == '__main__':
    sys.exit(main())
