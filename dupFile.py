import os

duplicates = []
files = []

if __name__ == '__main__':
    path = r"C:\Users\cannistrarod\Documents"
    for filename in os.listdir(path):
        fullPath = path + "\\" + filename
        info = os.stat(fullPath)
        print filename, info.st_mtime, info.st_mode

        for file in files:
            if ((info.st_size, info.st_mtime) == file[3]):
                dup = (file[0], filename)
                if (info.st_ctime > file[2]):
                    dup = (filename, file[0])
                duplicates.append(dup)

        if (info.st_mode == 33206):
            files.append([filename, fullPath, info.st_ctime, (info.st_size, info.st_mtime)])


        #print info

    print duplicates
