#!user/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

url = "http://www.cbssports.com/nfl/stats/playersort/nfl/year-2015-season-regular-category-touchdowns"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())



trs = soup.find_all('tr')

for tr in trs:
    for link in tr.find_all('a'):
        fulllink = link.get ('href')


    tds = tr.find_all("td")

    try: #we are using "try" because the table is not well formatted. This allows the program to continue after encountering an error.
        names = str(tds[0].get_text()) # This structure isolate the item by its column in the table and converts it into a string.
        years = str(tds[1].get_text())
        positions = str(tds[2].get_text())
        parties = str(tds[3].get_text())
        states = str(tds[4].get_text())
        congress = tds[5].get_text()

    except:
        continue

    print "Name: {} | Position: {} | Team: {} | Touchdowns {}.".format(names, years, positions, congress)
"""


trs = table.find_all('tr')
for tr in trs:

    tds = tr.findAll('td')
    print tds

    try:
        names = str(tds[0].get_text())
        test = str(tds[1].get_text())

    except:
        print "Bad tr string"
    print names"""
