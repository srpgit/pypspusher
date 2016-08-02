# -*- coding: utf-8 -*-
'''
Created on 2016年7月26日

@author: srpol_000
'''
import wx

import os
os.environ['PATH'] = ''

class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Bar')
        frame.Show()
        return True

app = App()
app.MainLoop()