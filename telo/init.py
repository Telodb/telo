"""
Initialize database
"""

import os
import configparser

from telo.core.echo import log


class init():

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def init(self):
        abspath = os.path.abspath(self.path) + '/.telo'
        log('Initialize empty telo database named {} in {} '.format(self.name, abspath))
        os.mkdir(abspath)
        confFile = os.path.join(abspath, 'config')
        create_config_file = open(confFile, 'w')
        create_config_file.close()
        parser = configparser.ConfigParser()
        parser.read(confFile)
