
import requests
import json
headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/74.0.3729.169 Chrome/74.0.3729.169 Safari/537.36",
'Content-Type': 'multipart/image-png'}
# url = 'http://localhost:8100/process/'
# s = json.dumps({'sl': '0.5', 'yaw': '0.5','ss':'spp'})
# r = requests.post(url, data=s,headers=headers)
# print( r.text)

files = {'file': open('/home/aaron/图片/2019-04-11 15-36-28屏幕截图.png', 'rb')}
r = requests.post('http://localhost:8100/processImg/', data=files,headers=headers)
print( r.text)