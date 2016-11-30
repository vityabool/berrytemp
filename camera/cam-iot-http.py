#!/usr/bin/python

import os
from azure.storage.blob import BlockBlobService
import ftplib
import time

blob_service = BlockBlobService(account_name='myiothubiv', account_key='o8IeKnrSSbbyTWBnCJfkRiYMy1x2MICwRB00a6nXZ/YczkTCBFiMnAsxaEPljH8raOBuPj70H3Bv0O07GtAN6Q==')

print "Updating index.html..."
ht = open('index.html','w')
ht.write ("<HTML><BODY>")

generator = blob_service.list_blobs('img')

links = []

for blob in generator:
#    links.append( '<a href="https://myiothubiv.blob.core.windows.net/img/' + blob.name + '">' + blob.name.split('.')[0] + '</a><br>')
    links.append( '<a href="https://myiothubiv.blob.core.windows.net/img/' + blob.name + '"><img width="450px" src="https://myiothubiv.blob.core.windows.net/img/' + blob.name + '"></img></a><br>' + blob.name.split('.')[0] + '<br>')
links.reverse()

for a in links[0:25]:
    ht.write(a)

ht.write ("</BODY></HTML>")
ht.close()


session = ftplib.FTP('waws-prod-db3-059.ftp.azurewebsites.windows.net','ivlinkoping\ivlinkoping1','Ivan123!')
file = open('index.html','rb')
session.storbinary('STOR site/wwwroot/index.html', file)
file.close()
session.quit()

