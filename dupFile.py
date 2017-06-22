import os

duplicates = []
files = {}

if __name__ == '__main__':
    path = r"C:\Users\cannistrarod\Documents"
    for filename in os.listdir(path):
        fullPath = path + "\\" + filename
        info = os.stat(fullPath)
        print filename, info.st_mtime, info.st_mode

        data = (info.st_size, info.st_mtime)

        if (data in files):
            dup = (files[data][0], filename)
            if (info.st_ctime > files[data][1]):
                dup = (filename, files[data][0])
            duplicates.append(dup)

        if (info.st_mode == 33206):
            files[data] = (filename, info.st_ctime)


        #print info

    print duplicates
