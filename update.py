import os
import base64


def update():
    url = 'https://api.github.com/repos/hg0428/hg0428db/contents/'
    files = []
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        req = req.json()  # the response is a JSON
        # req is now a dict with keys: name, encoding, url, size ...
        # and content. But it is encoded with base64.
        for i in req:
            files.append([i['name'], i['url']])
        #content = base64.decodestring(req['content'])
    else:
        return
    for f in files:
        req = requests.get(f[1])
        req = req.json()
        content = base64.decodestring(req['content'].encode())
        open(os.path.dirname(__file__) + '/' + f[0],
             'w+').write(content.decode())
