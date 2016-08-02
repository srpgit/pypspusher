# -*- coding: utf-8 -*-
'''
Created on 2016年7月26日

@author: srpol_000
'''

import os

os_path = os.environ['path']

paths = [path for path in os_path.split(';')]
for path in paths:
    try:
        for dll in os.listdir(path):
            if 'msvcr100.dll' == dll:
                print path
    except :
        pass

