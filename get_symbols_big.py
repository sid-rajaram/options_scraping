#!/usr/bin/env python

import urllib3
import pandas as pd

def main():

    http = urllib3.PoolManager()
    
    s_mega = http.request('GET', 'http://www.nasdaq.com/screening/companies-by-industry.aspx?marketcap=Mega-cap&render=download').data
    s_large = http.request('GET', 'http://www.nasdaq.com/screening/companies-by-industry.aspx?marketcap=Mega-cap&render=download').data
    
    symbols = []
    tmp_csv = [[y.strip('",') for y in x.split('","')] for x in s_mega.strip().split('\r\n')]
    print pd.DataFrame(tmp_csv[1:], columns=tmp_csv[0])
    
if __name__ == "__main__":
    main()
