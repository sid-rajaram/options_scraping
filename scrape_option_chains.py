#!/usr/bin/env python

import urllib3
import demjson
import ujson as json
import gzip

def main():

    http = urllib3.PoolManager()
    js = {}

    for line in open('symbols.txt','rb'):
        symb = line.strip()
        print symb
        
        s = http.request('GET', 'http://www.google.com/finance/option_chain?q=' + symb + '&output=json').data
        try:
            js[symb] = demjson.decode(s)
        except:
            continue
    
    json.dump(js, open('tmp','wb'))

if __name__ == "__main__":
    main()