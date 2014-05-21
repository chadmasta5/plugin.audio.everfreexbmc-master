import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'audio')

url = 'http://chadmasta5.weebly.com/uploads/6/0/1/9/6019696/listen.pls'
li = xbmcgui.ListItem('Listen', iconImage='http://i59.tinypic.com/2wf92z6.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
