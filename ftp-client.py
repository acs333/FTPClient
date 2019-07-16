from ftplib import FTP

ftp = FTP('')
ftp.connect('localhost',1033)
ftp.login()
ftp.cwd('/Users/AySanni/Desktop') #replace with your directory
ftp.retrlines('LIST')

def uploadFile():
 filename = 'sample-file.txt' #replace with your file in your home folder
 ftp.storbinary('STOR '+filename, open(filename, 'rb'))
 ftp.quit()

def downloadFile():
 filename = 'sample-file2.txt' #replace with your file in the directory ('directory_name')
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

uploadFile()
#downloadFile()