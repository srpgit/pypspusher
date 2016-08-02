# -*- coding: utf-8 -*-
'''
Created on 2016年8月1日

@author: RP_S
'''
import websocket

class DT():
    def __init__(self, url):
        self.__observers__ = []
        self.__ws__ = None
        self.__url__ = url
        self.__header__ = None
    
    def __on_open__(self):
        self.notify_observers('on_open')
    
    def __on_msg__(self, msg):
        self.notify_observers(msg)
    
    def __on_close__(self):
        self.notify_observers('on_close')
    
    def __on__error__(self, e):
        self.notify_observers('on_error')
    
    def start(self):
        self.__ws__ = websocket.WebSocketApp(self.__url__,
                                             on_open=self.__on_open__,
                                             on_close=self.__on_close__,
                                             on_message=self.__on_msg__,
                                             on_error=self.__on__error__
                                             )

    def send(self, data):
        if self.__ws__ is not None and self.__ws__.keep_running:
            self.__ws__.send(data)
    
    def close(self):
        if self.__ws__ != None:
            self.__ws__.close()
    
    def set_header(self, header):
        self.__header__ = header
    
    def notify_observers(self, msg):
        for observer in self.__observers__:
            observer.handle_msg(msg)
            
    def add_observer(self, observer):
        self.__observers__.append(observer)
        
    def remove_observer(self, observer):
        self.__observers__.remove(observer)
