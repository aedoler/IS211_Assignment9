#!user/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import sys


reload(sys) # Was getting an error reading:
            # UnicodeEncodeError: 'ascii' codec can't encode characters in position 2-3: ordinal not in range(128)
            # Discover this solution online
sys.setdefaultencoding("utf8")

url = "https://www.wunderground.com/history/airport/KNYC/2015/1/11/MonthlyHistory.html"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

#table = soup.findAll("table")
#print table[7]

trs = soup.find_all('tr')



for tr in trs:

    tds = tr.find_all("td")



    for link in tr.find_all('a'):
        fulllink = link.get ('href')




    try:
        date = str(tds[0].get_text())
        weather = tds[2].get_text()

    except:
        continue

    print "Day: {} | Avg. Temp.: {}.".format(date, weather)