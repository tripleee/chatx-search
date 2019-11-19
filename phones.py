#!/usr/bin/env python3

from collections import defaultdict
# from .
from rss_search import search_summary

def phone_search():
    counts = defaultdict(int)
    for entry in search_summary("Extracted possible phone number"):
        number = entry.split()[-1]
        counts[number] += 1
    for item in counts:
        yield counts[item], item


def main():
    import sys
    for count, item in phone_search():
        print('{0:7} {1}'.format(count, item))

if __name__ == '__main__':
    main()
