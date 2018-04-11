"""
Initialize database
"""

import os
import configparser

from telo.core.echo import log
from telo.conf import *


class init():

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def init(self):
        abspath = os.path.abspath(self.path) + '/.telo'
        try:
            os.mkdir(abspath)
            log('Initialize empty telo database named {} in {} '
                .format(self.name, abspath)
            )
        except FileExistsError:
            log('Reinitialize empty telo database named {} in {} '
                .format(self.name, abspath)
            )

        confFile = os.path.join(abspath, 'config')
        localConfig = open(confFile, 'w')
        globalConfig = open(confPath('global'))
        localConfig.write(globalConfig.read())
        globalConfig.close()
        localConfig.close()

        put('local', 'telo.name', self.name)
        put('local', 'telo.path', abspath)
