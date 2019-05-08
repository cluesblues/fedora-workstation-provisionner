#!/usr/bin/env python3

# @TODO : this instructions need to be translate in ansible.

import os
import tarfile
import re

# Configuration vars.
src_directory = "/usr/local/src/"

"""
Function who return telegram setup filename.
"""
def get_file_name(filename):
    files = os.listdir(filename)
    for file in files:
        if re.match(r"tsetup.*", file):
            return file
    return 0

"""
Function to extract archive.
"""
def extract_file(file, dest):
    tar = tarfile.open(file, "r:xz")
    tar.extractall("/usr/local/src/")
    tar.close()


# Script execution.
file = get_file_name(src_directory)

if file != 0:
    full_path = src_directory + file
    extract_file(full_path, ".")

    if os.path.islink('/usr/local/bin/telegram'):
        os.unlink('/usr/local/bin/telegram')
        os.symlink(src_directory + '/Telegram/Telegram', '/usr/local/bin/telegram')