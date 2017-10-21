'''选择性拷贝
遍历一个目录树，查找特定扩展名的文件，不论这些文件的位置在哪里，
将它们拷贝到一个新的文件夹中。
'''

import shutil, os

def copyFile(path, newpath):
    if os.path.exists(newpath) == False:
        os.makedirs(newpath)
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.pdf') or filename.endswith('.jpg'):
                shutil.copy(os.path.join(foldername, filename), newpath)
            else:
                continue
    print('Done.')

# copyFile(path, newpath)