
import ftplib

session = ftplib.FTP('connection string','login','pass')
file = open('index.html','rb')
session.storbinary('STOR site/wwwroot/index.html', file)
file.close()
session.quit()

