#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Joaquin Rives
@email: joaquin.rives01@gmail.com
@date: Dec 2020
"""

import connexion
import six

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


def associate_zone(site_id, zone_id):  # noqa: E501
    """associate_zone

     # noqa: E501

    :param site_id: 
    :type site_id: dict | bytes
    :param zone_id: 
    :type zone_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        site_id = Id.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        zone_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    response = sc.associate_assets(site_id, config.HIERARCHY_MODELS['ZONE'], zone_id)

    logger.info(response)
    return response


def create_site(body):  # noqa: E501
    """create_site

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = NameObj.from_dict(connexion.request.get_json())  # noqa: E501

    tags = None
    response = sc.create_asset(assetName=body.name,
                               assetModelId=config.MODELS['SITE_MODEL'],
                                tags=tags)
    logger.info(response)
    return response


def delete_site(site_id):  # noqa: E501
    """delete_site

     # noqa: E501

    :param site_id: 
    :type site_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        site_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    response = sc.delete_asset(assetId=site_id)

    logger.info(response)
    return response


def disassociate_zone(site_id, zone_id):  # noqa: E501
    """disassociate_zone

     # noqa: E501

    :param site_id: 
    :type site_id: dict | bytes
    :param zone_id: 
    :type zone_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        site_id = Id.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        zone_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    response = sc.disassociate_assets(site_id, config.HIERARCHY_MODELS['ZONE'], zone_id)

    logger.info(response)
    return response


def get_site_by_id(site_id):  # noqa: E501
    """get_site_by_id

     # noqa: E501

    :param site_id: 
    :type site_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        site_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    response = sc.describe_asset(site_id)
    logger.info(response)
    return response


def get_site_property_value_history(body):  # noqa: E501
    """get_site_property_value_history

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AssetPropertyValueHistoryRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_site_property_values(site_id):  # noqa: E501
    """get_site_property_values

     # noqa: E501

    :param site_id: 
    :type site_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        site_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    response = sc.get_asset_property_values(site_id, include_prop=None)

    logger.info(response)
    return response


def get_site_zones(site_id):  # noqa: E501
    """get_site_zones

     # noqa: E501

    :param site_id: 
    :type site_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        site_id = Id.from_dict(connexion.request.get_json())  # noqa: E501

    response = sc.list_associated_assets(site_id, config.HIERARCHY_MODELS['ZONE'], traversalDirection='CHILD', maxResults=25)

    logger.info(response)
    return response


def get_sites():  # noqa: E501
    """get_sites

     # noqa: E501


    :rtype: None
    """

    response = sc.list_assets(asset_model='SITE_MODEL')

    logger.info(response)
    return response


def put_site_property_value(body):  # noqa: E501
    """put_site_property_value

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AssetProperty.from_dict(connexion.request.get_json())  # noqa: E501

    quality = 'GOOD'
    site_id = body.asset_id
    property_name = body.property_name
    dataType = body.data_type
    value = body.value

    """
    example request:
    {"propertyName": "SiteName",
    "assetId": "0e6499c9-2945-4bd8-8c93-3e193602d0a3",
    "dataType": "stringValue",
    "value": "sitenamexxx"}
    
    """

    response = sc.put_property_value(site_id, property_name, dataType, value, quality)

    logger.info(response)
    return response
