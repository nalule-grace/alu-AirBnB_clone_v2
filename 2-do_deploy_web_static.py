#!/usr/bin/python3
#fabric script that distributes an archive to your web servers

from datetime import datetime
from fabric.api import *
import os

def do_pack():
    """
    generates .tgz archive from contents of web_static
    """
    local("mkdir -p versions")
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(current_time)
    result = local("tar -czf {} web_satic/".format(path))
    if result.failed:
        return None
    return path
~

def do_deploy(archive_path):
    """
    Distribute archive
    """
    if os.path.exists(archive_path):
        archive_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -c {}/".format(archived_file, newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static".format(newest_version,newest_version))
        run("sudo rm -rf {}/web_static".format(newst_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".foramt(newest_version))
        print("New version deployed!")
        return True


    return False
    
