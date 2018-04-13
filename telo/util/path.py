import os
import hues

static = os.getcwd()
cwd = os.getcwd
home = os.path.expanduser('~')

def localP():
    '''Get local portable path with telo database'''
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
    '''Get global device path with telo database'''
    share = os.path.abspath(os.path.join(home, '../', 'usr/', 'share/'))
    result = os.path.join(share, 'telo')
    if os.path.isdir(result):
        return result
    else:
        return None

def workingPath():
    '''Get local path or global path'''
    if localP():
        return localP()
    else:
        return globalP()
