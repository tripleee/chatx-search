#!/usr/bin/env python3

import feedparser
from urllib.parse import quote
from html import unescape


rssurl = 'https://chat.stackexchange.com/feeds/search/'

def search(phrase):
    rss = feedparser.parse('{0}{1}'.format(rssurl, quote(phrase, safe='')))
    for entry in rss.entries:
        yield entry

def search_summary(phrase):
    for entry in search(phrase):
        result = unescape(entry.summary_detail.value)
        if '<br>' in result:  # or '<br/>' in result:
            if result.startswith("<div class='full'>"):
                result = result[18:]
            if result.endswith("</div>"):
                result = result[:-6]
            for line in result.split('<br>'):
                yield line.strip()
        else:
            yield result


def main():
    import sys
    for arg in sys.argv[1:]:
        for entry in search(arg):
            print(unescape(entry.summary_detail.value))

if __name__ == '__main__':
    main()
