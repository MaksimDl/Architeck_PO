# coding: utf-8

"""
    Robot service 3.0

    API сервис управления роботом - пылесосом.  # noqa: E501

    OpenAPI spec version: 1.0.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ScheduleApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_schedule(self, body, **kwargs):  # noqa: E501
        """Добавить расписание  # noqa: E501

        Добавить расписание в базу  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_schedule(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Schedule body: Создать новое расписание в базе (required)
        :return: Schedule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_schedule_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_schedule_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_schedule_with_http_info(self, body, **kwargs):  # noqa: E501
        """Добавить расписание  # noqa: E501

        Добавить расписание в базу  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_schedule_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Schedule body: Создать новое расписание в базе (required)
        :return: Schedule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_schedule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_schedule`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'id' in params:
            form_params.append(('id', params['id']))  # noqa: E501
        if 'date_time' in params:
            form_params.append(('dateTime', params['date_time']))  # noqa: E501
        if 'mode' in params:
            form_params.append(('mode', params['mode']))  # noqa: E501
        if 'robot_id' in params:
            form_params.append(('robotId', params['robot_id']))  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/Schedule', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Schedule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_schedule(self, id, date_time, mode, robot_id, **kwargs):  # noqa: E501
        """Добавить расписание  # noqa: E501

        Добавить расписание в базу  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_schedule(id, date_time, mode, robot_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str date_time: (required)
        :param int mode: (required)
        :param int robot_id: (required)
        :return: Schedule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_schedule_with_http_info(id, date_time, mode, robot_id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_schedule_with_http_info(id, date_time, mode, robot_id, **kwargs)  # noqa: E501
            return data

    def add_schedule_with_http_info(self, id, date_time, mode, robot_id, **kwargs):  # noqa: E501
        """Добавить расписание  # noqa: E501

        Добавить расписание в базу  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_schedule_with_http_info(id, date_time, mode, robot_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str date_time: (required)
        :param int mode: (required)
        :param int robot_id: (required)
        :return: Schedule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'date_time', 'mode', 'robot_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_schedule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_schedule`")  # noqa: E501
        # verify the required parameter 'date_time' is set
        if ('date_time' not in params or
                params['date_time'] is None):
            raise ValueError("Missing the required parameter `date_time` when calling `add_schedule`")  # noqa: E501
        # verify the required parameter 'mode' is set
        if ('mode' not in params or
                params['mode'] is None):
            raise ValueError("Missing the required parameter `mode` when calling `add_schedule`")  # noqa: E501
        # verify the required parameter 'robot_id' is set
        if ('robot_id' not in params or
                params['robot_id'] is None):
            raise ValueError("Missing the required parameter `robot_id` when calling `add_schedule`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'id' in params:
            form_params.append(('id', params['id']))  # noqa: E501
        if 'date_time' in params:
            form_params.append(('dateTime', params['date_time']))  # noqa: E501
        if 'mode' in params:
            form_params.append(('mode', params['mode']))  # noqa: E501
        if 'robot_id' in params:
            form_params.append(('robotId', params['robot_id']))  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/Schedule', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Schedule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_schedule_by_id(self, schedule_id, **kwargs):  # noqa: E501
        """Удаляет расписание  # noqa: E501

        Удаляет расписание  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_schedule_by_id(schedule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int schedule_id: (required)
        :param str schedule_id: Идентификатор расписания
        :return: Schedule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_schedule_by_id_with_http_info(schedule_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_schedule_by_id_with_http_info(schedule_id, **kwargs)  # noqa: E501
            return data

    def delete_schedule_by_id_with_http_info(self, schedule_id, **kwargs):  # noqa: E501
        """Удаляет расписание  # noqa: E501

        Удаляет расписание  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_schedule_by_id_with_http_info(schedule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int schedule_id: (required)
        :param str schedule_id: Идентификатор расписания
        :return: Schedule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['schedule_id', 'schedule_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_schedule_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'schedule_id' is set
        if ('schedule_id' not in params or
                params['schedule_id'] is None):
            raise ValueError("Missing the required parameter `schedule_id` when calling `delete_schedule_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'schedule_id' in params:
            path_params['scheduleId'] = params['schedule_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'schedule_id' in params:
            header_params['scheduleId'] = params['schedule_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/Schedule/deleteById/{scheduleId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Schedule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_schedule_by_id(self, id, **kwargs):  # noqa: E501
        """Найти ркасписание по ID  # noqa: E501

        вернуть одно расписание  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_schedule_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Идентификатор расписания (required)
        :return: Schedule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_schedule_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_schedule_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_schedule_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Найти ркасписание по ID  # noqa: E501

        вернуть одно расписание  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_schedule_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Идентификатор расписания (required)
        :return: Schedule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_schedule_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_schedule_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['Id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/Schedule/findById/{Id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Schedule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_schedule(self, body, **kwargs):  # noqa: E501
        """Обновить расписание  # noqa: E501

        Обновить расписание  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_schedule(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Schedule body: Обновить существующее расписание в базе (required)
        :return: Schedule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_schedule_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_schedule_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_schedule_with_http_info(self, body, **kwargs):  # noqa: E501
        """Обновить расписание  # noqa: E501

        Обновить расписание  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_schedule_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Schedule body: Обновить существующее расписание в базе (required)
        :return: Schedule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_schedule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_schedule`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'id' in params:
            form_params.append(('id', params['id']))  # noqa: E501
        if 'date_time' in params:
            form_params.append(('dateTime', params['date_time']))  # noqa: E501
        if 'mode' in params:
            form_params.append(('mode', params['mode']))  # noqa: E501
        if 'robot_id' in params:
            form_params.append(('robotId', params['robot_id']))  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/Schedule', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Schedule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_schedule(self, id, date_time, mode, robot_id, **kwargs):  # noqa: E501
        """Обновить расписание  # noqa: E501

        Обновить расписание  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_schedule(id, date_time, mode, robot_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str date_time: (required)
        :param int mode: (required)
        :param int robot_id: (required)
        :return: Schedule
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_schedule_with_http_info(id, date_time, mode, robot_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_schedule_with_http_info(id, date_time, mode, robot_id, **kwargs)  # noqa: E501
            return data

    def update_schedule_with_http_info(self, id, date_time, mode, robot_id, **kwargs):  # noqa: E501
        """Обновить расписание  # noqa: E501

        Обновить расписание  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_schedule_with_http_info(id, date_time, mode, robot_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param str date_time: (required)
        :param int mode: (required)
        :param int robot_id: (required)
        :return: Schedule
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'date_time', 'mode', 'robot_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_schedule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_schedule`")  # noqa: E501
        # verify the required parameter 'date_time' is set
        if ('date_time' not in params or
                params['date_time'] is None):
            raise ValueError("Missing the required parameter `date_time` when calling `update_schedule`")  # noqa: E501
        # verify the required parameter 'mode' is set
        if ('mode' not in params or
                params['mode'] is None):
            raise ValueError("Missing the required parameter `mode` when calling `update_schedule`")  # noqa: E501
        # verify the required parameter 'robot_id' is set
        if ('robot_id' not in params or
                params['robot_id'] is None):
            raise ValueError("Missing the required parameter `robot_id` when calling `update_schedule`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'id' in params:
            form_params.append(('id', params['id']))  # noqa: E501
        if 'date_time' in params:
            form_params.append(('dateTime', params['date_time']))  # noqa: E501
        if 'mode' in params:
            form_params.append(('mode', params['mode']))  # noqa: E501
        if 'robot_id' in params:
            form_params.append(('robotId', params['robot_id']))  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/Schedule', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Schedule',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
