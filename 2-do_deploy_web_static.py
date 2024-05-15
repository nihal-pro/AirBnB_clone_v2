#!/usr/bin/python3
"""
import modules
this file is fabfile
"""
from fabric.api import local, task, env, put, run
from datetime import datetime
import os

env.hosts = ['54.172.182.205', '52.91.165.220']
env.user = 'ubuntu'


@task
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


@task
def do_deploy(archive_path):
    """this function distributes an archive to your web servers"""
    if os.path.exists(archive_path):
        File = os.path.basename(archive_path)
        Dir = os.path.splitext(File)[0]
        FullPath = "/data/web_static/releases/{}".format(Dir)
        put(archive_path, "/tmp/")
        run("rm -rf {}".format(FullPath))
        run("mkdir -p {}/".format(FullPath))
        run("tar -xzf /tmp/{} -C {}/".format(File, FullPath))
        run("rm /tmp/{}".format(File))
        run("mv {0}/web_static/* {0}/".format(FullPath))
        run("rm -rf {}/web_static".format(FullPath))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(FullPath))
        print("New version deployed!")
        return True
    return False
