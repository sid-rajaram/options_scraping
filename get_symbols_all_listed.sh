#!/bin/bash

echo -en "$(curl -s --compressed 'ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt' | tail -n+2 | ghead -n-1 | perl -pe 's/ //g' | tr '|' ' ' | awk '{printf $1" "} {print $4}')\n$(curl -s --compressed 'ftp://ftp.nasdaqtrader.com/SymbolDirectory/otherlisted.txt' | tail -n+2 | ghead -n-1 | perl -pe 's/ //g' | tr '|' ' ' | awk '{printf $1" "} {print $7}')" | grep -v 'Y$' | awk '{print $1}' | grep -v '[^a-zA-Z]'
