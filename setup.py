#!/usr/bin/python

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

from setuptools import setup, find_packages

import pysfdisk

with open('VERSION', 'r') as version_fh:
    version = version_fh.read()

setup(
    name='pysfdisk',
    version=version,
    license='GNU GENERAL PUBLIC LICENSE',
    author='Matt Comben',
    platforms='any',
    author_email='matthew@dockstudios.co.uk',
    packages=list(find_packages())
)
