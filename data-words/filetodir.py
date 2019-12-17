import os.path
import shutil

home = os.getcwd()
 

def list_dir(path):
    path_list = []
    for direct in os.listdir(path):
        if os.path.isdir(direct):
            path_list.append(direct)
    return path_list

path_list = []
for direct in list_dir(home):
    #print(direct)
    if os.path.isdir(direct):
        home = os.path.join(home,direct)
        os.chdir(home)
        for d in list_dir(home):
            path = os.path.join(home,d)
            if os.path.isdir(path):
                path_list.append(path)

for d in path_list:
    #print(d)
    for dirt in os.listdir(d):
        new = os.path.join(d,dirt)
        for f in os.listdir(new):
            file_path = os.path.join(new,f)
            print(file_path)
            new_loc = os.path.join('D:\IU\word',f)
            print(new_loc)
            shutil.move(file_path, new_loc)
            
