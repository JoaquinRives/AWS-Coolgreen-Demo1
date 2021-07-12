#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Joaquin Rives
@email: joaquin.rives01@gmail.com
@date: Dec 2020
"""
from datetime import datetime
import boto3
import time
from swagger_server.config import config, credentials

import logging

logger = logging.getLogger(__name__)
logger = config.config_logger(logger)

# todo put credential hiden
client = boto3.client('iotsitewise',
                      aws_access_key_id=credentials.AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=credentials.AWS_SECRET_ACCESS_KEY,
                      region_name=credentials.REGION_NAME
                      )


def get_asset_property_values(assetId, include_prop=None):

    response = client.describe_asset(assetId=assetId)
    # print(response)

    # 1. Get property ids
    prop_ids = {prop['name']: prop['id'] for prop in response['assetProperties']}

    # 2. Get property values
    prop_values = {}
    for propertyName, propertyId in prop_ids.items():
        response = client.get_asset_property_value(assetId=assetId, propertyId=propertyId)

        if 'propertyValue' not in response.keys():
            # TODO: add default of null to the sitewise models
            response['propertyValue'] = 'null'

        prop_values[propertyName] = response['propertyValue']

    # return only the properties requested
    if include_prop:
        prop_values = {k: v for k, v in prop_values.items() if k in include_prop}

    return prop_values


def get_asset_property_value_history(assetId, startDate, endDate, qualities='GOOD',
                                     timeOrdering='DESCENDING', maxResults=25,
                                     include_prop=None):

    response = client.describe_asset(assetId=assetId)

    # 1. Get property ids
    prop_ids = {prop['name']: prop['id'] for prop in response['assetProperties']}

    # 2. Get property values
    prop_values = {}
    for propertyName, propertyId in prop_ids.items():
        response = client.get_asset_property_value_history(
            assetId=assetId,
            propertyId=propertyId,
            # propertyAlias=property_alias,
            startDate=startDate,
            endDate=endDate,
            qualities=[qualities],  # 'GOOD' | 'BAD' | 'UNCERTAIN'
            timeOrdering=timeOrdering,  # 'ASCENDING' | 'DESCENDING'
            maxResults=maxResults
        )
        if 'assetPropertyValueHistory' not in response.keys():
            # TODO: add default of null to the sitewise models
            response['assetPropertyValueHistory'] = 'null'

        prop_values[propertyName] = response['assetPropertyValueHistory']  # ['value']

    # return only the properties requested
    if include_prop:
        prop_values = {k: v for k, v in prop_values.items() if k in include_prop}

    return prop_values


def create_asset(assetName, assetModelId, tags=None):

    response = client.create_asset(
        assetName=assetName,
        assetModelId=assetModelId)
        #tags=tags)

    return response


def delete_asset(assetId):
    response = client.delete_asset(assetId=assetId)
    return response


def list_associated_assets(assetId, hierarchyId=None, traversalDirection='CHILD', maxResults=25):

    if traversalDirection == 'CHILD':
        response = client.list_associated_assets(
            assetId=assetId,
            hierarchyId=hierarchyId,
            traversalDirection='CHILD',
            maxResults=maxResults
        )
    else:
        response = client.list_associated_assets(
            assetId=assetId,
            traversalDirection='PARENT',
            maxResults=maxResults
        )

    return response


def associate_assets(assetId, hierarchyId, childAssetId):
    assetStatus = None
    start_time = time.time()

    # for an asset to be associated it need to have ACTIVE status and
    # if the asset was created recently it takes a while util the status
    # changes to ACTIVE
    while (time.time() - start_time) < config.WAIT_TIME:
        response = client.describe_asset(assetId=assetId)
        assetStatus = response['assetStatus']['state']

        if assetStatus == 'ACTIVE':
            break
        else:
            time.sleep(config.WAIT_INTERVAL)

    response = client.associate_assets(
        assetId=assetId,
        hierarchyId=hierarchyId,
        childAssetId=childAssetId
    )
    return response


def describe_asset(assetId):
    return client.describe_asset(assetId=assetId)


def update_asset_property(assetId, property_name, propertyAlias=None, propertyNotificationState='DISABLED'):
    assetStatus = None
    start_time = time.time()

    # for an asset to be associated it need to have ACTIVE status and
    # if the asset was created recently it takes a while util the status
    # changes to ACTIVE
    while (time.time() - start_time) < config.WAIT_TIME:
        response = client.describe_asset(assetId=assetId)
        assetStatus = response['assetStatus']['state']

        if assetStatus == 'ACTIVE':
            break
        else:
            time.sleep(config.WAIT_INTERVAL)

    property_id = [property['id'] for property in response['assetProperties'] if property['name'] == property_name][0]

    if not property_id:
        logger.error(f"ERROR: Property '{property_name}' not found in asset ({assetId})")
        return response

    response = client.update_asset_property(
        assetId=assetId,
        propertyId=property_id,
        propertyAlias=propertyAlias,
        propertyNotificationState=propertyNotificationState
    )
    return response


def disassociate_assets(assetId, hierarchyId, childAssetId):
    response = client.disassociate_assets(
        assetId=assetId,
        hierarchyId=hierarchyId,
        childAssetId=childAssetId
    )
    return response


def list_assets(asset_model, customer_id=None):
    response = client.list_assets(assetModelId=config.MODELS[asset_model])
    # asset_name = 'SensorAC011'
    # asset_id = [asset['id'] for asset in response['assetSummaries'] if asset['name'] == asset_name][0]
    #
    # response = client.describe_asset(assetId=asset_id)
    # property_name = 'Working State'
    # property_id = [prop['id'] for prop in response['assetProperties'] if prop['name'] == property_name][0]
    # property_alias = [prop['alias'] for prop in response['assetProperties'] if prop['name'] == property_name
    #                   and 'alias' in prop.keys()][0]

    return response


# TODO
def put_property_value(assetId, property_name, dataType, value, quality='GOOD'):
    """
    'value': {
                  'stringValue': 'string', |
                  'integerValue': 123,     |
                  'doubleValue': 123.0,    |
                  'booleanValue': True | False
              }
    """

    # convert dataType
    if dataType == 'integerValue':
        value = int(value)
    elif dataType == 'doubleValue':
        value = float(value)
    elif dataType == 'booleanValue':
        value = bool(value)

    value = {dataType: value}

    response = client.describe_asset(assetId=assetId)

    property_id = [property['id'] for property in response['assetProperties'] if property['name'] == property_name][0]
    # property_alias = [property['propertyAlias'] for property in response['assetProperties'] if property['name'] == property_name][0]

    if not property_id:
        logger.error(f"ERROR: Property '{property_name}' not found in asset ({assetId})")
        return response

    entryId = property_name + str(int(time.time()))

    entry = {
              'entryId': entryId,
              'assetId': assetId,
              'propertyId': property_id,
              # 'propertyAlias': property_alias,
              'propertyValues': [
                  {
                      'value': value,
                      'timestamp': {
                          'timeInSeconds': int(time.time()),
                          'offsetInNanos': 0
                      },
                      'quality': quality
                  },
              ]
          }

    response = client.batch_put_asset_property_value(entries=[entry])

    return response
