#!/usr/bin/python3
"""Fab file to generates a .tgz archive
from the contents of the web_static folder """

from fabric.api import local
import datetime
import os


def do_pack():
    """Function to add files to archive"""

    create_folder = local("mkdir -p versions")
    if create_folder.stderr != "":
        return None
    d_now = datetime.datetime.utcnow()
    file = f"web_static_{d_now.year}{d_now.month}\
{d_now.day}{d_now.hour}{d_now.minute}{d_now.second}"
    archive = local(f"tar -cvzf versions/{file} web_static")
    if archive.stderr != "":
        return None
    return f"versions/web_static_{file}.tgz"
