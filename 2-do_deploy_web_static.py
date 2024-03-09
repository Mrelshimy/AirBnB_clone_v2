#!/usr/bin/python3
"""Fab file to deploy web_static archive to servers"""

from fabric.api import *
import os

env.hosts = ['localhost', '52.3.255.212', '100.24.235.178']


def do_deploy(archive_path):
    """Function to deploy archive to servers"""
    if not os.path.exists(archive_path):
        return False
    name = archive_path[9:-4]
    archive_name = archive_path[9:]
    try:
        put(archive_path, '/tmp/')
        run(f'sudo mkdir -p /data/web_static/releases/{name}/')
        run(f'sudo tar -xzf /tmp/{archive_name} -C\
 /data/web_static/releases/{name}/')
        run(f'sudo rm /tmp/{archive_name}')
        run(f'sudo mv /data/web_static/releases/{name}/web_static/*\
 /data/web_static/releases/{name}/')
        run(f'sudo rm -r /data/web_static/releases/{name}/web_static')
        run(f'sudo rm -rf /data/web_static/current')
        run(f'sudo ln -s /data/web_static/releases/{name}/\
 /data/web_static/current')
    except Exception:
        return False
    return True
