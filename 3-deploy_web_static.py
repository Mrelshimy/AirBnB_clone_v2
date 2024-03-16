#!/usr/bin/python3
"""Fab file to deploy web_static archive to servers"""

from fabric.api import *
import datetime
import os

env.hosts = ['52.3.255.212', '100.24.235.178']


def do_pack():
    """Function to add files to archive"""
    try:
        create_folder = local("mkdir -p versions")
        d_now = datetime.datetime.utcnow()
        file = f"web_static_{d_now.year}{d_now.month}\
{d_now.day}{d_now.hour}{d_now.minute}{d_now.second}"
        archive = local(f"tar -cvzf versions/{file}.tgz web_static")
        return f"versions/web_static_{file}.tgz"
    except Exception:
        return None


def do_deploy(archive_path):
    """Function to deploy archive to servers"""

    if os.path.isfile(archive_path) is False:
        return False
    archive_name = archive_path.split("/")[-1]
    name = archive_name.split(".")[0]
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
        return True
    except Exception:
        return False


def deploy():
    """Complete deploy to servers"""
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)
