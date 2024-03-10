#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['52.3.255.212', '100.24.235.178']


def do_clean(number=0):
    """Delete out-of-date archives"""
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(x)) for x in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [x for x in archives if "web_static_" in x]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(x)) for x in archives]
