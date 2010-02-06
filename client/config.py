# Brandon Edens
# 2010-02-06
# Copyright (C) 2010 Brandon Edens <brandon@as220.org>
#
# This file is part of jukebox.
#
# jukebox is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# jukebox is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with jukebox. If not, see <http://www.gnu.org/licenses/>.
"""
"""

###############################################################################
## Imports
###############################################################################

import os
import yaml


###############################################################################
## Constants
###############################################################################

# User's home directory.
USER_HOME_DIR = os.getenv("HOME")

# Directories where configuration file might be stored.
CONFIG_DIRECTORIES = (USER_HOME_DIR,
                      '/etc/jukebox/',
                      )

# Configuration filename.
CONFIG_FILENAME = '/.jukebox.rc'


###############################################################################
## Classes
###############################################################################

class Config:

    def __init__(self):
        self.log_filename = '/var/tmp/jukebox.log'
        self.log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    def load(self):
        config_filename = self._find_config_file()
        if config_filename:
            config_file = open(config_filename, 'r')
            options = yaml.load(config_file)
            self.log_filename = options['log_filename']
            self.log_format = options['log_format']

    def _find_config_file(self):
        absolute_path = None
        for directory in CONFIG_DIRECTORIES:
            path = directory+CONFIG_FILENAME
            if os.path.isfile(path):
                absolute_path = path
        return absolute_path


###############################################################################
## Statements
###############################################################################

config = Config()
config.load()

