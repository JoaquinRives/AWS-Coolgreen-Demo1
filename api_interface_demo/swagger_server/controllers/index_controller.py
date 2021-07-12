import connexion
import six

from swagger_server.models.asset_property import AssetProperty  # noqa: E501
from swagger_server.models.create_sensor import CreateSensor  # noqa: E501
from swagger_server.models.id import Id  # noqa: E501
from swagger_server.models.sensor_type import SensorType  # noqa: E501
from swagger_server.models.todo import TODO  # noqa: E501
from swagger_server.models.asset_property_value_history_request import AssetPropertyValueHistoryRequest  # noqa: E501
from swagger_server import util

from swagger_server.config import config
import swagger_server.controllers.sitewise_client as sc


def index():
    return "JR Health OK!!!"


def base():
    return "JR Base Health OK!!!"
