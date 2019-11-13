#!/usr/bin/env python3

# from .
from rss_search import search_summary
from collections import defaultdict

def strip_code(url):
    if url.startswith('<code>'):
        url = url[6:]
    if url.endswith('</code>'):
        url = url[:-7]
    return url

# ######## FIXME: encapsulate this into a class
def pharma_redirects(redir):
    for line in search_summary(redir):
        if ": Wordpress promotion URL " not in line:
            continue
        redirect = line.split(": Wordpress promotion URL ")[1]
        if " redirects to " not in redirect:
            raise ValueError('Apparent redirect without " redirects to ": {0}'.format(
                extracted))
        partition = redirect.split(" redirects to ")
        # ######## TODO: parse URLs
        yield strip_code(partition[0]), strip_code(partition[1])

def main():
    import sys
    for arg in sys.argv[1:]:
        for redirect, destination in pharma_redirects(arg):
            print('{0} -> {1}'.format(redirect, destination))

if __name__ == '__main__':
    main()
