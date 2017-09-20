import json
import re
import os
import urllib
url = "https://grumble.bandcamp.com/album/freestyle-tools-vol-9"
f = urllib.urlopen(url)
x = f.read()
m = re.search(r'(?<=album_title: )"(.+)"', x)
album = m.group(1)
print 'downloading %s' % album
m = re.search(r'(?<=trackinfo: )\[\{.+\}\]', x)
if not os.path.exists(album):
    os.makedirs(album)
data = json.loads(m.group(0))
for i in data:
    print 'downloading %s...' % i['title']
    #print i['file']['mp3-128']
    urllib.urlretrieve("https:"+i['file']['mp3-128'], album+"/"+i['title']+".mp3")
#print m.group(0)
