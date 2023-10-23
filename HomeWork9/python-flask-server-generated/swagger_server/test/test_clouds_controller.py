# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cloud import Cloud  # noqa: E501
from swagger_server.models.clouds import Clouds  # noqa: E501
from swagger_server.models.error import Error  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCloudsController(BaseTestCase):
    """CloudsController integration test stubs"""

    def test_cancel_cloud_by_id(self):
        """Test case for cancel_cloud_by_id

        Отмена заказа в облаке по ID
        """
        response = self.client.open(
            '/api/v1//clouds/{cloud_id}'.format(cloud_id='cloud_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_cloud(self):
        """Test case for create_cloud

        Создание заказа на облако
        """
        body = Error()
        response = self.client.open(
            '/api/v1//clouds',
            method='POST',
            data=json.dumps(body),
            content_type='adplication/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_clouds(self):
        """Test case for get_all_clouds

        Метод получения списка ресурсов на облако
        """
        response = self.client.open(
            '/api/v1//clouds',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cloud_by_id(self):
        """Test case for get_cloud_by_id

        Метод получения заказа на облако по ID
        """
        response = self.client.open(
            '/api/v1//clouds/{cloud_id}'.format(cloud_id='cloud_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
