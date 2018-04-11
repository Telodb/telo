import configparser
import os

pwd = os.getcwd()
home = os.path.expanduser('~')

def put(place, key, value):
    '''Put configuration in config file'''
    parser = configparser.ConfigParser()
    section = key.split('.')[0]
    option = key.split('.')[1]

    if place == 'local':
        confFile = os.path.join(pwd, '.telo/', 'config')
    if place == 'global':
        confFile = os.path.join(home, '.teloconfig')

    parser.read(confFile)

    if not parser.has_section(section):
        parser.add_section(section)
    parser.set(
        section=section,
        option=option,
        value=value,
    )

    fp = open(confFile, 'w')
    parser.write(fp)
    fp.close()
