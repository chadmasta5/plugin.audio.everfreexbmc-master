import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'audio')

li.setIconImage('http://i59.tinypic.com/2wf92z6.png')
li.setProperty('fanart_image', 'http://fc07.deviantart.net/fs71/i/2013/251/b/2/the_everfree_network_by_kibbiethegreat-d6lk9hi.png')
url = 'http://chadmasta5.weebly.com/uploads/6/0/1/9/6019696/listen.pls'
li = xbmcgui.ListItem('Listen', iconImage='http://i60.tinypic.com/2hnozec.png')
li.setProperty('fanart_image', 'http://fc07.deviantart.net/fs71/i/2013/251/b/2/the_everfree_network_by_kibbiethegreat-d6lk9hi.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
