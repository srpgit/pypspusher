# -*- coding: utf-8 -*-
'''
Created on 2016年8月1日

@author: RP_S
'''
class Model():
    def __init__(self, data_trans):
        if data_trans is not None:
            data_trans.add_observer(self)
        pass
    
    def handle_msg(self, msg):
        print msg
