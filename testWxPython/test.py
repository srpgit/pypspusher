# -*- coding: utf-8 -*-
'''
Created on 2016年7月27日

@author: srpol_000
'''
import wx

class MyApp:
    def __init__(self):
        '''
        __init__(
        self, 
        Window parent, 
        int id=-1, 
        String title=EmptyString, 
        Point pos=DefaultPosition, 
        Size size=DefaultSize, 
        long style=DEFAULT_FRAME_STYLE, 
        String name=FrameNameStr)
        '''
        #app
        self.app = wx.PySimpleApp()
        
        #frame
        frame = wx.Frame(None, -1, title='This is Title')
        self.frame = frame
        frame.SetPosition(wx.Point(500, 300))
        frame.SetSize(wx.Size(600, 400))
        frame.SetIcon(wx.Icon('C:\Users\srpol_000\Desktop\pspusher-icon.ico', wx.BITMAP_TYPE_ICO))
        
        #menu
        menu_file = wx.Menu()
        menu_file.Append(101, 'Open', 'Open a new document')
        menu_file.Append(102, 'Save', 'Save the document')
        menu_file.AppendSeparator()
        
        menu_item_quit = wx.MenuItem(menu_file, 105, 'Quit\tCtrl+Q', 'Quit the App')
        menu_file.AppendItem(menu_item_quit)
        
        menu_edit = wx.Menu()
        menu_edit.Append(201, 'All', kind=wx.ITEM_CHECK)
        menu_edit.Append(202, 'Copy', kind=wx.ITEM_CHECK)
        
        menubar = wx.MenuBar()
        menubar.Append(menu_file, 'File')
        menubar.Append(menu_edit, 'Edit')
        
        frame.SetMenuBar(menubar)
        
        wx.EVT_MENU(self.frame, 105, self.OnQuit)
    
    def start(self):    
        self.frame.Show()
        self.app.MainLoop()
        
    def OnQuit(self,evt):
        self.close()
        
    def close(self):
        self.app.Destroy()

if __name__=='__main__':
    MyApp().start()
    