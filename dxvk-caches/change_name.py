import os
from pathlib import Path
current_path = os.getcwd() + '/dxvk-caches'



for root, dirs, files in os.walk(current_path):
    for folder in dirs:    
        
        curr_path = root + '/' + folder
        
        readme_file = ''
        dxvk_cache_md = ''
        
        for file in os.listdir(curr_path):
            if file == 'readme.md':
                readme_file = open(curr_path + '/readme.md','a+')
                readme_file_contents = readme_file.read()
            
            elif file.endswith('.md'):
                dxvk_cache_md = open(curr_path+'/'+file, 'r')
                dxvk_cache_md_file_contents = dxvk_cache_md.read()
                dxvk_cache_md.close()

                os.remove(curr_path + '/' + file)
            
            try:
                readme_file.write('\n\n\n {}'.format(dxvk_cache_md_file_contents))
                readme_file.close()
            except:
                pass
