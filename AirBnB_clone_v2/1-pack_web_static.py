#!/usr/bin/python3
"""
import modules
this file is fabfile
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    this function execute script that generates a .tgz
        archive from the contents of the web_static folder
    """
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f'versions/web_static_{date}.tgz'
    print(f'Packing web_static to {file_path}')
    try:
        local(f"tar -czvf {file_path} web_static")
        size = os.path.getsize(file_path)
        print(f'web_static packed: {file_path} -> {size}Bytes')
        return file_path
    except Exception:
        return None
