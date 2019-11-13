#!/usr/bin/env python3

#from .
from rss_search import search_summary
from collections import defaultdict


# ######## TODO: encapsulate this into a class
def ipmap(ip):
    ips = defaultdict(set)
    hosts = defaultdict(int)
    for host, ip in ipsearch(ip):
        ips[ip].add(host)
        hosts[host] += 1
    return ips, hosts
        
def ipsearch(ip):
    for line in search_summary(ip):
        if ": ip " not in line:
            continue
        partition = line.split(": ip ")
        host = partition[0].split(": ")[-1]
        ip = partition[1].split()[0]
        yield host, ip    

def main():
    import sys
    for arg in sys.argv[1:]:
        ips, hosts = ipmap(arg)
        for ip in ips:
            total = sum(hosts[x] for x in ips[ip])
            print('{0:7} {1}'.format(total, ip))
            for host in ips[ip]:
                print('\t{0:7} {1}'.format(hosts[host], host))

if __name__ == '__main__':
    main()
