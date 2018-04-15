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
