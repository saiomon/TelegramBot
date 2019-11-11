import os,shutil

def get_dir(node):
    dirs=[]
    files=[]
    for d in os.listdir(node):
        if  is_dir(node+d):
            dirs.append(d)
        else:
            files.append(d)
    return sorted(dirs),sorted(files)

def check_abs(path):
    print("Abs path: ",os.path.abspath(path))
    print(os.path.commonprefix([os.path.abspath(path),os.path.abspath("cloud/")]))

def add_dir(path):
    check_abs(path)
    try:
        os.mkdir(path)
    except Exception as e:
        print(e)
        return "Could not add {}".format(pretty_dir(path))
    else:
        return "{} added.".format(pretty_dir(path))

def del_dir(path):
    dn=pretty_dir(path)
    try:
        shutil.rmtree(path)
    except Exception as e:
        print(e)
        return "Could not delete {}".format(dn)
    else:
        return "{} deleted".format(dn)

def del_file(path):
    fn=get_fn(path)
    try:
        os.remove(path)
    except Exception as e:
        print(e)
        return "Could not delete {}".format(fn)
    else:
        return "{} deleted".format(fn) 


#Example path: cloud/dir2/dir55/dirq/moi.txt
def pretty_dir(node):   #-> dir2/dir55/dirq/
    lst=node.split("/")
    ss=""
    for s in lst[1:]:
        ss=ss+'/'+s
    return ss

def strip_last(node):   #-> cloud/dir2/dir55/
    lst=node.split("/")
    ss=""
    for s in lst[:-2]:
        ss=ss+s+'/'
    return ss

def strip_file(node):   #-> cloud/dir2/dir55/dirq/
    if is_file(node):
        lst=node.split("/")
        ss=""
        for s in lst[:-1]:
            ss=ss+s+'/'
        return ss
    else:
        return ""

def get_full_path(node):    #-> /home/erno/TelegramBot/cloud/dir2/dir55/dirq/moi.txt
    return os.path.abspath(node)

def is_file(path):
    return os.path.isfile(path)
def is_dir(path):
    return os.path.isdir(path)
def get_fn(path):
    if is_file(path):
        return path.split("/")[-1]
    else:
        return ""
