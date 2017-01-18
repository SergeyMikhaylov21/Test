import urllib.request
headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)'}
req = urllib.request.Request('https://meduza.io/', headers = headers)
html = urllib.request.urlopen(req)
respData = html.read()

saveFile = open('Headers.txt', 'w')
saveFile.write(str(respData))
saveFile.close()
html.close()
