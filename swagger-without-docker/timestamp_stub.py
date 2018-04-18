import os
import platform
import time

def get_timestamp(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    # path_to_file='/home/algo.txt'
    ans={}
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            ans['accessed_time']=time.ctime(os.path.getatime(path_to_file))
            ans['modified_time']=time.ctime(os.path.getmtime(path_to_file))
            ans['creation_time']=time.ctime(os.path.getctime(path_to_file))

            return ans
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime

