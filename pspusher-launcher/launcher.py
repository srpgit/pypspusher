# -*- coding: utf-8 -*-
'''
Created on 2016年7月27日

@author: srpol_000

给jar写一个指定jre运行
'''
import os

os_cmd = 'start'
jre_path = 'jre7/bin/javaw'
jar_cmd = '-jar' 
jar_file = 'pspusher-client.jar'
dbg_out = '->debug.txt'

final_cmd = ' '.join([os_cmd, jre_path, jar_cmd, jar_file])

print final_cmd

os.system(final_cmd)