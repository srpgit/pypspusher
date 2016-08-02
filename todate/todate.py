# -*- coding: utf-8 -*-
'''
Created on 2016年7月27日

@author: srpol_000
'''
import re

d = '2016-5-月31'
rd = re.compile('[^\d]')
ds = rd.split(d)


fmt = 'yyyy--mm--dd'
