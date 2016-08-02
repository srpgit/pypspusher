# -*- coding: utf-8 -*-
'''
Created on 2016年8月1日

@author: RP_S
'''
import data_trans
import model

if __name__ == '__main__':
    ws_server_link = 'ws://192.168.1.135:8080/fiiwp/pc-push/websocket'
    dt = data_trans.DT(ws_server_link)
    md = model.Model(dt)
    dt.set_header({'_u':'cyt','_p':'aaa'})
    dt.start()

