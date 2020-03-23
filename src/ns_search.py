#!/usr/bin/env python3

#from .
from rss_search import search_summary
from collections import defaultdict


# ######## FIXME: encapsulate this into a class
def nssearch(*nslist):
    result = dict()
    nsset = dict()
    seen = set()
    for ns in nslist:
        for line in search_summary(ns):
            if not line.startswith("halflife:"):
                continue
            if ": ns ['" not in line:
                continue
            if line in seen:
                continue
            seen.add(line)
            partition = line.split(": ns ['")
            date, post, domain = partition[0][len('halflife:'):].rsplit(':', 2)
            domain = domain.lstrip()
            nses = sorted(partition[1].strip("']").split("', '"))
            nskey = ';'.join(nses)
            if nskey not in result:
                # Remember the precise key
                nsset[nskey] = nses
                # Assemble a 4-tuple which sorts according to our requirements
                #  0 - number of matched query terms from the input query
                #  1 - number of total hits
                #  2 - age of newest sub-entry
                #  3 - dict of individual domains, each a list of dates
                # Need a list, not a tuple, because some items need updating
                result[nskey] = [
                    sum(1 if y in nskey else 0 for y in nslist),
                    1, date, defaultdict(list)]
            else:
                result[nskey][1] += 1
                result[nskey][2] = max(date, result[nskey][2])
            result[nskey][3][domain].append(date)
    for nskey in sorted(result, key=lambda x: result[x]):
        yield nsset[nskey], result[nskey][3]

def main():
    import sys
    for nses, domaincount in nssearch(*sys.argv[1:]):
        total = sum(len(domaincount[x]) for x in domaincount)
        print('{0:7} {1!r}'.format(total, nses))
        for domain in domaincount:
            print('\t{0:7} {1} ({2})'.format(
                len(domaincount[domain]), domain, max(domaincount[domain])))

if __name__ == '__main__':
    main()
