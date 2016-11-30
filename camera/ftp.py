
import ftplib

session = ftplib.FTP('waws-prod-db3-059.ftp.azurewebsites.windows.net','ivlinkoping\ivlinkoping1','Ivan123!')
file = open('index.html','rb')
session.storbinary('STOR site/wwwroot/index.html', file)
file.close()
session.quit()

