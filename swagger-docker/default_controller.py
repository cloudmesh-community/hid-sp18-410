import connexion
import six

from swagger_server.models.timestamp import TIMESTAMP  # noqa: E501
from swagger_server import util
from timestamp_stub import get_timestamp

def timestamp_get(path):  # noqa: E501
    """timestamp_get

    Returns timestamp information of the file # noqa: E501

    :param path: Path to file
    :type path: str

    :rtype: TIMESTAMP
    """
    return TIMESTAMP(get_timestamp(path))








#IP of 1st(top) pi-169.254.24.132
#IP of 2nd pi - 169.254.35.145
#IP of 3rd pi - 169.254.87.91
#IP of 4th pi  169.254.225.63
#IP of 5th pi - 169.254.190.73
