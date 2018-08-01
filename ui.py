import wx
from map_methods import tour, init, animate


class Window(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        #self.tour = tour
        self.basicGUI()


    def basicGUI(self):
        panel = wx.Panel(self)
        editButton = wx.Menu()
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'status msg...')
        menuBar.Append(fileButton, '&File')
        menuBar.Append(editButton, 'Edit')

        trbutton = wx.Button(self, label="tour", pos=(20, 70))
        trbutton.Bind(wx.EVT_BUTTON, tour)
        #wx.TextCtrl(panel, pos=(10,10), size=(250,150))

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        self.SetTitle('Fish Data')
        self.Show(True)

    def Quit(self, e):
        self.Close()



def Main():
    app = wx.App()
    Window(None)
    app.MainLoop()

Main()

'''
app = wx.App()
frame = wx.Frame(None, -1, 'Window Title')
frame.Show()
app.MainLoop()
'''