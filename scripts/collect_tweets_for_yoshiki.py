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

api = TwitterAPI('DZ83RS3IgoBN7HfOAS6zGA',
	'a2dCaqyup1UyNpph6lBPib0Ftykj8KR23OgMvtWtV78',
	'18067482-cTJCT0uQ6HIWtm8f9YMHW0RcIEUxlvVkwfF8BlZTm',
	'lm2EbhMapWF8LVcjmhUURL2PTyLeZ5DpO3ACZgno')

# chautaqua
# (40.00000497268461, -105.29022216796875)
# pleasant view
# (40.0507451947963, -105.24481773376465)
r = api.request('statuses/filter', {'locations':'-105.29,40.00,-105.24,40.05'})

try:
	for item in r.get_iterator():
		fd = open('yoshiki_twitt_collection.txt', 'a')
		fd.write(str(item)+'\n')
		fd.close()

		# print item

except ValueError:
	print 'There was a problem collecting the data try a different search'
	exit(1)
