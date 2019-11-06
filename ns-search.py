#!/usr/bin/env python3

#from .
from rss_search import search, unescape
from collections import defaultdict


# ######## FIXME: encapsulate this into a class
def nssearch(ns):
    nspairs = dict()
    nsset = dict()
    for entry in search(ns):
        extracted = unescape(entry.summary_detail.value)
        if ": ns ['" not in extracted:
            continue
        partition = extracted.split(": ns ['")
        domain = partition[0].split(": ")[-1]
        nses = sorted(partition[1].strip("']").split("', '"))
        nskey = ';'.join(nses)
        if nskey not in nspairs:
            nspairs[nskey] = defaultdict(int)
            nsset[nskey] = nses
        nspairs[nskey][domain] += 1
    for nskey in nsset:
        yield nsset[nskey], nspairs[nskey]

def main():
    import sys
    for arg in sys.argv[1:]:
        for nses, domaincount in nssearch(arg):
            total = sum(domaincount[x] for x in domaincount)
            print('{0:7} {1!r}'.format(total, nses))
            for domain in domaincount:
                print('\t{0:7} {1}'.format(domaincount[domain], domain))

if __name__ == '__main__':
    main()
