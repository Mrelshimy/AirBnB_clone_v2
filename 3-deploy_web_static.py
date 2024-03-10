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
        print("New version deployed!")
    except Exception:
        return False
    return True


def deploy():
    """Complete deploy to servers"""
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)
