#!/usr/bin/python

api = 'https://api.github.com'

import argparse
import json
import logging
import os
import re
import requests
import requests.auth
import sys

re_link = re.compile('<(?P<url>[^>]+)>; rel="(?P<rel>[^"]+)"')
LOG = logging.getLogger('repolist')


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--username', '-u')
    p.add_argument('--password', '-p')
    p.add_argument('--token', '-t')
    p.add_argument('--debug', '-d',
                   action='store_const',
                   const=logging.DEBUG,
                   dest='loglevel')

    p.set_defaults(loglevel=logging.INFO)
    return p.parse_args()


def split_link(links):
    linkmap = {}
    for link in links.split(', '):
        mo = re_link.match(link)
        if not mo:
            continue

        linkmap[mo.group('rel')] = mo.group('url')

    return linkmap

def main():
    args = parse_args()
    logging.basicConfig(
        level=args.loglevel)
    reqlog = logging.getLogger('requests')
    reqlog.setLevel(logging.WARN)

    if args.token:
        args.username = args.token
        args.password = 'x-oauth-basic'

    auth = requests.auth.HTTPBasicAuth(
        args.username, args.password)
    url = '%s/user/repos' % api
    repos = []

    LOG.info('reading list of repositories')
    while True:
        r = requests.get(url, auth=auth)
        r.raise_for_status()
        
        repos.extend(r.json())

        if 'link' not in r.headers:
            break

        links = split_link(r.headers['link'])
        if 'next' not in links:
            break

        url = links['next']
    LOG.info('found %d repositories', len(repos))

    print '\n'.join(x['git_url'] for x in repos)


if __name__ == '__main__':
    main()

