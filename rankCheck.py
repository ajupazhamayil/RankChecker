
import urllib, sys, re

def rankCheck(rsk):
    xml = urllib.urlopen('http://data.alexa.com/data?cli=10&dat=s&url=%s'%site).read()
    try: rank = int(re.search(r'<POPULARITY[^>]*TEXT="(\d+)"', xml).groups()[0])
    except: rank = -1
    print 'Your rank for %s is %d\n' % (site, rank)



site = "www.google.com"
rankCheck(site)
