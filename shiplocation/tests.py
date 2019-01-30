import csv
import datetime
import os
from copy import deepcopy

from dateutil import parser
from django.test import TestCase
# Create your tests here.
from rest_framework.test import APIClient

from shiplocation.models import ShipLocation, ShipName


class ShiplocationTest(TestCase):
    """Test case for Ship API"""

    def setUp(self):
        os.path.exists('positions.csv')
        for data in csv.DictReader(open('positions.csv')):
            obj, created = ShipName.objects.get_or_create(imo=data['imo'])
            location_data = deepcopy(data)
            location_data['imo'] = obj
            ShipLocation.objects.create(**location_data)

    def test_ship_list_api(self):
        """Test ship api"""
        api_client = APIClient()
        response = api_client.get('/api/ships/')
        self.assertEqual(len(response.json()), 3)

    def test_ship_location_api(self):
        """Test ship location api"""
        api_client = APIClient()
        response = api_client.get('/api/ships/')
        def isDescending(list):
            previous = list[0]
            for number in list:
                if number > previous:
                    return False
                previous = number
            return True
        for data in response.json():
            response = api_client.get('/api/positions/{}/'.format(data.get('imo')))
            ship_dates = []
            for location_data in response.json():
                ship_dates.append(parser.parse(location_data.get('ship_date')))
            self.assertTrue(isDescending(ship_dates))
