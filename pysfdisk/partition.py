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

import re

from pysfdisk.errors import MissingAttribute


class Partition(object):
    """Interface for defining partitions"""

    @staticmethod
    def load_from_sfdisk_output(config, block_device):
        """Generate partition object from output of sfdisk"""
        if 'node' not in config:
            raise MissingAttribute('node attribute not found in sfdisk config')

        if 'start' not in config:
            raise MissingAttribute('start attribute not found in sfdisk config')

        if 'size' not in config:
            raise MissingAttribute('size attribute not found in sfdisk config')

        partition_number = re.match('^.*([0-9]+)$', config['node']).group(1)
        partition_config = {
            'node': config['node'],
            'uuid': config['uuid'] if 'uuid' in config else None,
            'start': config['start'],
            'size': config['size'],
            'attrs': config['attrs'] if 'attrs' in config else None,
            'type': config['type'] if 'type' in config else None
        }
        return Partition(partition_number=partition_number,
                         block_device=block_device,
                         **partition_config)

    def __init__(self, partition_number, block_device, **kwargs):
        """Set member variables"""
        self.block_device = block_device
        self.partition_number = partition_number
        for config_name in kwargs:
            setattr(self, config_name, kwargs[config_name])

    def get_partition_number(self):
        return self.partition_number
