import os
from pathlib import Path
current_path = os.getcwd() + '/dxvk-caches'

dir:list

for root, dirs, files in os.walk(current_path):
    for folder in dirs:    
        cur_path = root + '/' + folder
        for files in os.listdir(cur_path):
            if files == 'Credits.md':
                os.rename(cur_path+'/Credits.md', cur_path+'/readme.md')
