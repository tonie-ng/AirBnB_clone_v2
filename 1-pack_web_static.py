#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static folder
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    return the archive path if the archive has been correctly generated
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is None:
        return None
    return archive
