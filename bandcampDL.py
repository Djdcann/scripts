import json
import re
import os
import urllib


def bandcamp_download(url):
    site = urllib.urlopen(url)
    url_data = url.split('/')
    html = site.read()
    
    #determine if url is to album or track
    if url_data[3] == 'album':
        m = re.search(r'(?<=album_title: )"(.+)"', html)
        album = m.group(1)
    else:
        album = url_data[4]

    #remove non-valid characters from path
    album = re.sub(r'[^\w\-_\. ]', '_', album)

    print 'downloading %s' % album

    m = re.search(r'(?<=trackinfo: )\[\{.+\}\]', html)

    if not os.path.exists(album):
        os.makedirs(album)

    data = json.loads(m.group(0))

    #foreach song in album
    for i in data:
        print 'downloading %s...' % i['title']
        print i['file']['mp3-128']
        path = '%s/%s.mp3' % (album, re.sub(r'[^\w\-_\. ]', '_', i['title']))
        mp3 = i['file']['mp3-128']

        #dl the file
        try:
            if "https:/" in mp3:
                urllib.urlretrieve(mp3, path)
            else:
                urllib.urlretrieve("https:" + mp3, path)
        except Exception as e:
            print e


if __name__ == '__main__':
    get_url = "https://strawberrygirls.bandcamp.com/track/first-kiss"
    #print get_url.split('/')
    bandcamp_download(get_url)
