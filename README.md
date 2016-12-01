# PYsfdisk

A Python API for linux sfdisk utility

Note: This project is pre-alpha


# Install

    git clone https://github.com/MatthewJohn/python-sfdisk
    sudo pip install ./


# Example

    import pysfdisk
    
    # Create block device object for the disk
    >>> disk = pysfdisk.BlockDevice(path='/dev/nvme0n1')

    # Optionally, if not using root and sudo is available, use this
    >>> disk = pysfdisk.BlockDevice(path='/dev/nvme0n1', use_sudo=True)

    # Partitions information is automatically loaded
    >>> disk.get_partitions()['0'].uuid
    403ACCB2-0B00-465F-B190-B59C45CFD860


# License

pysfdisk is licensed under GPL v2.


# Copyright

Copyright &copy; 2016 - Matt Comben
