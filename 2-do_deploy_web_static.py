#!/usr/bin/python3
"""Fab file to deploy web_static archive to servers"""

from fabric.api import *
import os

env.hosts = ['52.3.255.212', '100.24.235.178']


def do_deploy(archive_path):
    """Function to deploy archive to servers"""
    if not os.path.exists(archive_path):
        return False
    name = archive_path[9:-4]
    archive_name = archive_path[9:]
    try:
        put(archive_path, '/tmp/')
        sudo('mkdir -p /data/web_static/releases/{}/'.format(name))
        sudo('tar -xzf /tmp/{} -C\
 /data/web_static/releases/{}/'.format(archive_name, name))
        sudo('rm /tmp/{}'.format(archive_name))
        sudo('rsync -a /data/web_static/releases/{}/web_static/*\
 /data/web_static/releases/{}/'.format(name, name))
        sudo('rm -r /data/web_static/releases/{}/web_static'.format(name))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s /data/web_static/releases/{}/\
 /data/web_static/current'.format(name))
        print("New version deployed!")
    except Exception:
        return False
    return True
