import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'audio')

li.setProperty('fanart_image', 'http://i59.tinypic.com/b669vt.jpg')
url = 'http://chadmasta5.weebly.com/uploads/6/0/1/9/6019696/listen.pls', iconImage='http://i60.tinypic.com/2hnozec.png')
li = xbmcgui.ListItem('Listen', iconImage='http://i60.tinypic.com/2hnozec.png')
li.setProperty('fanart_image', 'http://i59.tinypic.com/b669vt.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
