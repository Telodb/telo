import os
import hues

static = os.getcwd()
cwd = os.getcwd
home = os.path.expanduser('~')

def localP():
    try:
        while not '.telo' in os.listdir(cwd()):
            if cwd() == '/':
                return None
            os.chdir('../')
        result = cwd()
        os.chdir(static)
        return result
    except PermissionError:
        return None

def globalP():
    share = os.path.abspath(os.path.join(home, '../', 'usr/', 'share/'))
    return os.path.join(share, 'telo')

def workingPath():
    if localP():
        return localP()
    else:
        return globalP()
