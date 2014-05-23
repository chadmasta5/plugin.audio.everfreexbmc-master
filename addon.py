import xbmc, xbmcgui, xbmcaddon

addon = xbmcaddon.Addon('plugin.audio.everfree.xbmc')
title = addon.getAddonInfo('name')
icon = li.setIconImage('http://i60.tinypic.com/2hnozec.png')
link = 'http://chadmasta5.weebly.com/uploads/6/0/1/9/6019696/listen.pls'

 
li = xbmcgui.ListItem(label=title, iconImage=icon, thumbnailImage=icon, path=link)
li.setInfo(type='Audio', infoLabels={ "Title": Everfree Radio })
li.setProperty('IsPlayable', 'true')
li.setProperty('fanart_image', 'http://i59.tinypic.com/b669vt.jpg')

xbmc.Player().play(item=link, listitem=li)
