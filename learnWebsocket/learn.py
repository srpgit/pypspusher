# -*- coding: utf-8 -*-
'''
Created on 2016年8月1日

@author: RP_S
'''
from websocket import create_connection
ws_server_link = 'ws://192.168.1.135:8080/fiiwp/pc-push/websocket'
# ws_server_link = 'ws://echo.websocket.org'
ws = create_connection(ws_server_link)
ws.send('Hello websocket!')
result = ws.recv()
print 'Received %s'% result
ws.close()