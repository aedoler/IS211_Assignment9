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

    try:
        names = str(tds[0].get_text())
        position = str(tds[1].get_text())
        team = str(tds[2].get_text())
        touchdowns = tds[6].get_text()

    except:
        continue

    print "Name: {} | Position: {} | Team: {} | Touchdowns {}.".format(names, position, team, touchdowns)
