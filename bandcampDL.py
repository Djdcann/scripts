import json
import re
import os
import urllib

#download music from bandcamp URL
def bandcamp_download(url):
    site = urllib.urlopen(url)
    url_data = url.split('/')
    html = site.read()
    
    #determine if url is to album or track
    if len(url_data) < 5 or url_data[3] == 'album':
        m = re.search(r'(?<=album_title: )"(.+)"', html)
        album = m.group(1)
    else:
        album = url_data[4]

    #remove non-valid characters from path
    album = validate(album)

    print 'downloading album/track %s' % album

    m = re.search(r'(?<=trackinfo: )\[\{.+\}\]', html)

    if not os.path.exists(album):
        os.makedirs(album)

    data = json.loads(m.group(0))

    #foreach song in album
    for i in data:
        file = validate(i['title'])
        print 'downloading %s...' % file
        print i['file']['mp3-128']
        path = '%s/%s.mp3' % (album, file)
        mp3 = i['file']['mp3-128']

        #dl the file
        try:
            if "https:/" in mp3:
                urllib.urlretrieve(mp3, path)
            else:
                urllib.urlretrieve("https:" + mp3, path)
        except Exception as e:
            print e
            
    return album

#validate directory or file name
def validate(name):
    return re.sub(r'[^\w\-_\. ]', '_', name)

if __name__ == '__main__':
    get_url = "https://birocratic.bandcamp.com/album/beets"
    #print get_url.split('/')
    bandcamp_download(get_url)
