# Copyright (c) 2016 - Matt Comben
#
# This file is part of pysfdisk.
#
# pysfdisk is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# pysfdisk is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pysfdisk.  If not, see <http://www.gnu.org/licenses/>

import os
import json
import subprocess

from pysfdisk.errors import NotRunningAsRoot, BlockDeviceDoesNotExist
from pysfdisk.partition import Partition


class BlockDevice(object):
    """Provide interface to obtain and set partition tables"""

    SFDISK_EXECUTABLE = '/sbin/sfdisk'

    def __init__(self, path, use_sudo=False):
        """Set member variables, performm checks and obtain the initial parititon table"""
        # Setup member variables
        self.path = path
        self.use_sudo = use_sudo
        self.partitions = {}
        self.label = None
        self.uuid = None

        self._assert_root()
        self._ensure_exists()
        self._read_partition_table()

    def get_partitions(self):
        """Return the partition objects for the block object"""
        return self.partitions

    def _read_partition_table(self):
        """Create the parititon table using sfdisk and load partitions"""
        command_list = [self.SFDISK_EXECUTABLE, '--json', self.path]
        if self.use_sudo:
            command_list.insert(0, 'sudo')
        disk_config = json.loads(subprocess.check_output(command_list))
        self.label = disk_config['partitiontable']['label'] or None
        self.uuid = disk_config['partitiontable']['id'] or None

        for partition_config in disk_config['partitiontable']['partitions']:
            partition = Partition.load_from_sfdisk_output(partition_config, self)
            self.partitions[partition.get_partition_number()] = partition

    def _ensure_exists(self):
        if not os.path.exists(self.path):
            raise BlockDeviceDoesNotExist('Block device %s does not exist' % self.path)

    def _assert_root(self):
        """Ensure that the sciprt is being run as root, or 'as root' has been speicified"""
        if os.getuid() != 0 and not self.use_sudo:
            raise NotRunningAsRoot('Must be running as root or specify to use sudo')
