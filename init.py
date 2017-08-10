# -*- coding:utf-8 -*-
"""
@author: changrong
@file: build.py
@time: 2017/6/17 上午10:40
"""

import subprocess
import os
import argparse
import sys
import time
import getpass

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(SRC_DIR, 'source', '_posts')

TEMPLATE = '---\n' \
           'title:  {title}\n' \
           '{tags}' \
           '---\n' \
           'hello world'


def excute_shell(sh):
    print(sh)
    res = subprocess.call(sh, shell=True)
    print('** ** ** result : ' + str(res) + ' ** ** **\n')


def read():
    return TEMPLATE


def main(args=None):
    title = args.title
    tags = ''
    if args.tags:
        args.tags = args.tags.replace(' ', '')
        tag_list = args.tags.split(',')
        tags = 'tags:\n'
        for tag in tag_list:
            tags += '- {}\n'.format(tag)
    print("page will init new with title:{title} and tags:{tags}".format(title=title, tags=tags.replace('\n', '')))
    file_name = '{date}-{title}.md'.format(date=time.strftime("%Y-%m-%d"), title=title.replace(' ', '-'))
    template = read().format(
        title=title,
        tags=tags
    )
    file_name = os.path.join(POSTS_DIR, file_name)
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(template)
    print('page init done')
    print('new page path: {path}'.format(path=file_name))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--title', action='store', required=True, dest='title',
                        help='new page name, use \\[space] to split word')
    parser.add_argument('--tags', action='store', required=False, dest='tags',
                        help='tags for name, use "," to split')
    args = parser.parse_args()
    sys.exit(main(args))
