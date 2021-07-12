#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Joaquin Rives
@email: joaquin.rives01@gmail.com
@date: Dec 2020
"""
import connexion
import six
import re

from swagger_server.models.asset_property import AssetProperty  # noqa: E501
from swagger_server.models.id import Id  # noqa: E501
from swagger_server.models.name_obj import NameObj  # noqa: E501
from swagger_server.models.todo import TODO  # noqa: E501
from swagger_server.models.asset_property_value_history_request import AssetPropertyValueHistoryRequest  # noqa: E501
from swagger_server import util

from swagger_server.config import config
import swagger_server.controllers.sitewise_client as sc

import logging

logger = logging.getLogger(__name__)
logger = config.config_logger(logger)


def associate_sensor(zone_id, sensor_id):  # noqa: E501
    """associate_sensor

     # noqa: E501

    :param zone_id: 
    :type zone_id: dict | bytes
    :param sensor_id: 
    :type sensor_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        zone_id = Id.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        sensor_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    # get the sensor type
    sensor_model = None
    assetModelId = sc.describe_asset(sensor_id)['assetModelId']
    for k, v in config.MODELS.items():
        if v == assetModelId:
            sensor_model = k

    sensor_type = re.sub('_MODEL', '', sensor_model)

    response = sc.associate_assets(zone_id, config.HIERARCHY_MODELS[sensor_type], sensor_id)

    logger.info(response)
    return response


def create_zone(body):  # noqa: E501
    """create_zone

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = NameObj.from_dict(connexion.request.get_json())  # noqa: E501

    tags = None
    response = sc.create_asset(assetName=body.name,
                               assetModelId=config.MODELS['ZONE_MODEL'],
                               tags=tags)
    logger.info(response)
    return response


def delete_zone(zone_id):  # noqa: E501
    """delete_zone

     # noqa: E501

    :param zone_id: 
    :type zone_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        zone_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    response = sc.delete_asset(assetId=zone_id)

    logger.info(response)
    return response


def disassociate_sensor(zone_id, sensor_id):  # noqa: E501
    """disassociate_sensor

     # noqa: E501

    :param zone_id: 
    :type zone_id: dict | bytes
    :param sensor_id: 
    :type sensor_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        zone_id = Id.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        sensor_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    # get the sensor type
    sensor_model = None
    assetModelId = sc.describe_asset(sensor_id)['assetModelId']
    for k, v in config.MODELS.items():
        if v == assetModelId:
            sensor_model = k

    sensor_type = re.sub('_MODEL', '', sensor_model)

    response = sc.disassociate_assets(zone_id, config.HIERARCHY_MODELS[sensor_type], sensor_id)

    logger.info(response)
    return response


def get_zone_all_sensors(zone_id):  # noqa: E501
    """get_zone_all_sensors

     # noqa: E501

    :param zone_id: 
    :type zone_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        zone_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    sensor_types = config.SENSOR_TYPES

    all_assetSummaries = []
    for sensor_type in sensor_types:
        response = sc.list_associated_assets(
            zone_id, config.HIERARCHY_MODELS[sensor_type], traversalDirection='CHILD', maxResults=25)

        all_assetSummaries += response['assetSummaries']

    response['assetSummaries'] = all_assetSummaries

    logger.info(response)
    return response


def get_zone_assetsensor_sensors(zone_id):  # noqa: E501
    """get_zone_assetsensor_sensors

     # noqa: E501

    :param zone_id: 
    :type zone_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        zone_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    response = sc.list_associated_assets(
        zone_id, config.HIERARCHY_MODELS['ASSET_SENSOR'], traversalDirection='CHILD', maxResults=25)

    logger.info(response)
    return response


def get_zone_by_id(zone_id):  # noqa: E501
    """get_zone_by_id

     # noqa: E501

    :param zone_id: 
    :type zone_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        zone_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    response = sc.describe_asset(zone_id)
    logger.info(response)
    return response


def get_zone_property_value_history(body):  # noqa: E501
    """get_zone_property_value_history

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AssetPropertyValueHistoryRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_zone_property_values(zone_id):  # noqa: E501
    """get_zone_property_values

     # noqa: E501

    :param zone_id: 
    :type zone_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        zone_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    response = sc.get_asset_property_values(zone_id, include_prop=None)

    logger.info(response)
    return response


def get_zone_sensornode_sensors(zone_id):  # noqa: E501
    """get_zone_sensornode_sensors

     # noqa: E501

    :param zone_id: 
    :type zone_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        zone_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    response = sc.list_associated_assets(
        zone_id, config.HIERARCHY_MODELS['SENSOR_NODE'], traversalDirection='CHILD', maxResults=25)

    logger.info(response)
    return response


def get_zones():  # noqa: E501
    """get_zones

     # noqa: E501


    :rtype: None
    """
    response = sc.list_assets(asset_model='ZONE_MODEL')

    logger.info(response)
    return response


def put_zone_property_value(body):  # noqa: E501
    """put_zone_property_value

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AssetProperty.from_dict(connexion.request.get_json())  # noqa: E501

    quality = 'GOOD'
    zone_id = body.asset_id
    property_name = body.property_name
    dataType = body.data_type
    value = body.value

    """
    example request:
    {"propertyName": "ZoneName",
    "assetId": "667ed4de-4cb4-42c3-a09b-77aad59ee4c3",
    "dataType": "stringValue",
    "value": "zonenamexxx"}

    """

    response = sc.put_property_value(zone_id, property_name, dataType, value, quality)

    logger.info(response)
    return response
