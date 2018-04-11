import configparser
import os

from telo.core.echo import log

pwd = os.getcwd()
home = os.path.expanduser('~')


def confPath(place):
    if place == 'local':
        return os.path.join(pwd, '.telo/', 'config')

    elif place == 'global':
        return os.path.join(home, '.teloconfig')

    else:
        return None


def put(place, key, value):
    '''Put configuration in config file'''
    parser = configparser.ConfigParser()
    section = key.split('.')[0]
    option = key.split('.')[1]
    confFile = confPath(place)
    parser.read(confFile)
    if not parser.has_section(section):
        parser.add_section(section)
    parser.set(section=section, option=option, value=value)
    fp = open(confFile, 'w')
    parser.write(fp)
    fp.close()


def take(place, key):
    '''Take configuration in config file'''
    parser = configparser.ConfigParser()
    section = key.split('.')[0]
    option = key.split('.')[1]
    confFile = confPath(place)
    parser.read(confFile)
    # if parser.has_section(section) and parser.has_option(option):
    try:
        return parser.get(section=section, option=option)

    except NoSectionError as e:
        log(e)
        return None

    except NoOptionError as e:
        log(e)
        return None
