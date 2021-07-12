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

import logging

logger = logging.getLogger(__name__)
logger = config.config_logger(logger)


def create_sensor(body):  # noqa: E501
    """create_sensor

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = CreateSensor.from_dict(connexion.request.get_json())  # noqa: E501

    name = body.name
    sensor_model = body.sensor_type + '_MODEL'
    device_id = body.device_id
    tags = None

    response = sc.create_asset(assetName=name,
                               assetModelId=config.MODELS[sensor_model],
                                tags=tags)

    assetId = response['assetId']

    # get properties of type measurement
    properties = sc.describe_asset(assetId)['assetProperties']

    # set property "device"
    # TODO: create device property (stack003-models)

    # set aliases
    for prop in properties:
        if prop['name'] in config.PROPERTIES_WITH_ALIAS:
            alias = f"/sitewise/treon/devices/{device_id}/{prop['name']}"
            sc.update_asset_property(assetId, prop['name'], propertyAlias=alias, propertyNotificationState='DISABLED')

    logger.info(response)
    return response


def delete_sensor(sensor_id):  # noqa: E501
    """delete_sensor

     # noqa: E501

    :param sensor_id: 
    :type sensor_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        sensor_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    response = sc.delete_asset(assetId=sensor_id)

    logger.info(response)
    return response


def get_all_sensors():  # noqa: E501
    """get_all_sensors

     # noqa: E501


    :rtype: None
    """
    sensor_types = config.SENSOR_TYPES

    all_assetSummaries = []
    for sensor_type in sensor_types:
        asset_model = sensor_type + '_MODEL'
        response = sc.list_assets(asset_model=asset_model)

        all_assetSummaries += response['assetSummaries']

    response['assetSummaries'] = all_assetSummaries

    logger.info(response)
    return response


def get_sensor_by_id(sensor_id):  # noqa: E501
    """get_sensor_by_id

     # noqa: E501

    :param sensor_id: 
    :type sensor_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        sensor_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    response = sc.describe_asset(sensor_id)
    logger.info(response)
    return response


def get_sensor_parents(sensor_id):  # noqa: E501
    """get_sensor_parents

     # noqa: E501

    :param sensor_id: 
    :type sensor_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        sensor_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    response = sc.list_associated_assets(
        sensor_id, traversalDirection='PARENT', maxResults=25)

    logger.info(response)
    return response


def get_sensor_property_value_history(body):  # noqa: E501
    """get_sensor_property_value_history

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AssetPropertyValueHistoryRequest.from_dict(connexion.request.get_json())  # noqa: E501

    # example request
    """
{"assetId": "94400776-e093-4437-8ff4-f41c8c74e92c",
"maxResults": 25,
"startDate": "2020-12-20",
"endDate": "2020-12-31",
"timeOrdering": "DESCENDING",
"include_prop": ["Temperature", "WorkingState"]}
    """
    asset_id = body.asset_id
    start_date = body.start_date
    end_date = body.end_date
    max_results = int(body.max_results) if body.max_results else 50
    time_ordering = body.time_ordering if body.time_ordering else 'DESCENDING'
    include_prop = body.include_prop

    print(body)
    print(start_date)
    print(type(start_date))

    prop_values = sc.get_asset_property_value_history(assetId=asset_id,
                                                      startDate=start_date,
                                                      endDate=end_date,
                                                      maxResults=max_results,
                                                      timeOrdering=time_ordering,
                                                      include_prop=include_prop)

    return prop_values


def get_sensor_property_values(sensor_id):  # noqa: E501
    """get_sensor_property_values

     # noqa: E501

    :param sensor_id: 
    :type sensor_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        sensor_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    response = sc.get_asset_property_values(sensor_id, include_prop=None)

    logger.info(response)
    return response


def get_sensors(sensor_type):  # noqa: E501
    """get_sensors

     # noqa: E501

    :param sensor_type: 
    :type sensor_type: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        sensor_type = SensorType.from_dict(connexion.request.get_json())  # noqa: E501

    asset_model = sensor_type + '_MODEL'
    response = sc.list_assets(asset_model=asset_model)

    logger.info(response)
    return response


def put_sensor_property_value(body):  # noqa: E501
    """put_sensor_property_value

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AssetProperty.from_dict(connexion.request.get_json())  # noqa: E501

    quality = 'GOOD'
    sensor_id = body.asset_id
    property_name = body.property_name
    dataType = body.data_type
    value = body.value

    """
    example request:
    {"propertyName": "Wattage",
    "assetId": "1f08d927-c544-48f5-a9d5-c98bd9ce852f",
    "dataType": "doubleValue",
    "value": "3000.0"}

    """

    response = sc.put_property_value(sensor_id, property_name, dataType, value, quality)

    logger.info(response)
    return response
