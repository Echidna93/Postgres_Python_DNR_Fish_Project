import wx


class Window(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.basicGUI()

    def basicGUI(self):
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'status msg...')

        menuBar.Append(fileButton, '&File')

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