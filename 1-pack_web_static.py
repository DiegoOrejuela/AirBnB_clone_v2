#!/usr/bin/python3
"""Module 1-pack_web_static.py"""
from fabric.api import local, settings
import os


def do_pack():
    """Fabric script that generates a .tgz archive from
    the contents of the web_static folder"""

    if not os.path.isdir("versions"):
        local("mkdir versions")

    with settings(warn_only=True):
        cm = "tar -czvf versions/web_static_$(date +'%Y%m%d%H%M%S').tgz"
        cm = cm + " web_static"
        result = local(cm)
        if result.return_code == 0:
            list_files = os.listdir("versions")
            return list_files[0]
        else:
            return None
