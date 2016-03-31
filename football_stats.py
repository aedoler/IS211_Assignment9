#!user/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import json
from bs4 import BeautifulSoup

url = "http://www.cbssports.com/nfl/stats/playersort/nfl/year-2015-season-regular-category-touchdowns"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

# print soup.prettify()

#final_link = soup.p.a
# final_link.decompose()

trs = soup.find_all('tr')




for tr in trs:
    tds = tr.find_all('td')

    try:
        names = str(tds[0].get_text())
        pos = str(tds[1].get_text())

    except:
        print "Bad tr string"
    print names