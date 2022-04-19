import os
import base64
import requests


def downloadFiles(files):
  for f in files:
        req = requests.get(f[1])
        req = req.json()
        if type(req) == list:
          downloadFiles(req)
        content = base64.decodestring(req['content'].encode())
        open(os.path.dirname(__file__) + '/' + f[0],
             'w+').write(content.decode())
def update():
    url = 'https://api.github.com/repos/hg0428/hg0428db/contents/'
    files = []
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        req = req.json()  
        for i in req:
            files.append([i['name'], i['url']])
    else:
        return
    downloadFiles(files)
