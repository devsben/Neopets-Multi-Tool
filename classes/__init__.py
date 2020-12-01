import sys

if sys.version_info[0] < 3:
    """
    If a Python version less than 3 is detected prevent the user from running this program.
    This will be removed once the final tweaking is completed for Python 2.
    """
    raise Exception("Python 3 is required to run this program.")