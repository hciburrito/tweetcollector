#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
from __future__ import division

__author__ = "Abigale Stangl & Yoshiki Vazquez Baeza"
__copyright__ = "Copyright 2013, The Tweet Collector Project"
__credits__ = ["Yoshiki Vazquez Baeza", "Abigale Stangl"]
__license__ = "BSD"
__version__ = "0.0.0-dev"
__maintainer__ = "Yoshiki Vazquez Baeza"
__email__ = "antgonza@gmail.com"
__status__ = "Development"

from TwitterAPI import TwitterAPI
from time import sleep

api = TwitterAPI('iXNPqanEbga0DYJEROqFQ',
	'fE4r6oYq6vVeoZjMuIDBIzfC7Xr829QAuWxxqhrs',
	'26060205-jinL28r0G0i08ESJM5yXkb78jAptJxflSFYQDojSr',
	'uhiYYTNw3mQJDhj5OwB0xe7Owchy9P57sJ45MnEw')

PRINTING_TAGS = '3D,3Dprint,3Dprinting,3dprinter,xyzprinting,3Dfabrication,3Dscan,3Dscanning,3Dscanner,3Dmodeling'
GOOGLE_GLASS_TAGS = 'Googleglass,googleglasses,GoogleGlassInfo,GoogleGlassNYC,GoogleGlassFans'
ARDUINO_TAGS = 'Arduino'
ABBY_SEARCH_TAGS = ','.join([GOOGLE_GLASS_TAGS, ARDUINO_TAGS, PRINTING_TAGS])

r = api.request('statuses/filter', {'track':ABBY_SEARCH_TAGS})

while True:
	try:
		for item in r.get_iterator():
			fd = open('abby_tweet_collection.txt', 'a')
			fd.write(str(item)+'\n')
			fd.close()

	except:
		print 'There was a problem collecting the data try a different search'
	sleep(1200)
