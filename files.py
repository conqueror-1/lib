import os

folder = "/Users/user/Projects/lib"
filepaths = [os.path.join(folder,f) for f in os.listdir(folder)]

# print (filepaths)

files = [f.path for f in os.scandir(folder) if f.is_file()]
dirs = [d.path for d in os.scandir() if d.is_dir()]
# print (dirs)
# print (files)

for (dirpath, dirnames, filenames) in os.walk(folder):
    for f in filenames:
        print ("file :: {}".format(os.path.join(dirpath,f)))
    for d in dirnames:
        print ("dir :: {}".format(os.path.join(dirpath,d)))
