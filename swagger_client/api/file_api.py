# coding: utf-8

"""
    CSPro Sync

    Web API for synchronizing data and files from devices in the field to a web server.   # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class FileApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_file_content(self, file_path, **kwargs):  # noqa: E501
        """Get file  # noqa: E501

        Get contents of file matching path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_file_content(file_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_path: path of file to download (required)
        :param str if_none_match: ETag value from previous response, 304 is returned if this matches current ETag
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_file_content_with_http_info(file_path, **kwargs)  # noqa: E501
        else:
            (data) = self.get_file_content_with_http_info(file_path, **kwargs)  # noqa: E501
            return data

    def get_file_content_with_http_info(self, file_path, **kwargs):  # noqa: E501
        """Get file  # noqa: E501

        Get contents of file matching path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_file_content_with_http_info(file_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_path: path of file to download (required)
        :param str if_none_match: ETag value from previous response, 304 is returned if this matches current ETag
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_path', 'if_none_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_file_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_path' is set
        if ('file_path' not in params or
                params['file_path'] is None):
            raise ValueError("Missing the required parameter `file_path` when calling `get_file_content`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'file_path' in params:
            path_params['filePath'] = params['file_path']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/files/{filePath}/content', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_file_info(self, file_path, **kwargs):  # noqa: E501
        """Get file  # noqa: E501

        Get contents of file matching path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_file_info(file_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_path: path of file to download for (required)
        :return: FileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_file_info_with_http_info(file_path, **kwargs)  # noqa: E501
        else:
            (data) = self.get_file_info_with_http_info(file_path, **kwargs)  # noqa: E501
            return data

    def get_file_info_with_http_info(self, file_path, **kwargs):  # noqa: E501
        """Get file  # noqa: E501

        Get contents of file matching path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_file_info_with_http_info(file_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_path: path of file to download for (required)
        :return: FileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_file_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_path' is set
        if ('file_path' not in params or
                params['file_path'] is None):
            raise ValueError("Missing the required parameter `file_path` when calling `get_file_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'file_path' in params:
            path_params['filePath'] = params['file_path']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/files/{filePath}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FileInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_files_in_folder(self, folder_path, **kwargs):  # noqa: E501
        """Get files in folder  # noqa: E501

        Get file info for files in the given folder  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_files_in_folder(folder_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder_path: path of folder to list contents of (required)
        :return: FileListing
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_files_in_folder_with_http_info(folder_path, **kwargs)  # noqa: E501
        else:
            (data) = self.get_files_in_folder_with_http_info(folder_path, **kwargs)  # noqa: E501
            return data

    def get_files_in_folder_with_http_info(self, folder_path, **kwargs):  # noqa: E501
        """Get files in folder  # noqa: E501

        Get file info for files in the given folder  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_files_in_folder_with_http_info(folder_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder_path: path of folder to list contents of (required)
        :return: FileListing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_files_in_folder" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_path' is set
        if ('folder_path' not in params or
                params['folder_path'] is None):
            raise ValueError("Missing the required parameter `folder_path` when calling `get_files_in_folder`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folder_path' in params:
            path_params['folderPath'] = params['folder_path']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/folders/{folderPath}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FileListing',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_file_content(self, file_path, content_md5, **kwargs):  # noqa: E501
        """Upload file  # noqa: E501

        Put contents of file to server directory specified by filePath. Create directory filePath if it does not exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_file_content(file_path, content_md5, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_path: Full path to upload file to (required)
        :param str content_md5: Signature of file contents (required)
        :return: FileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_file_content_with_http_info(file_path, content_md5, **kwargs)  # noqa: E501
        else:
            (data) = self.put_file_content_with_http_info(file_path, content_md5, **kwargs)  # noqa: E501
            return data

    def put_file_content_with_http_info(self, file_path, content_md5, **kwargs):  # noqa: E501
        """Upload file  # noqa: E501

        Put contents of file to server directory specified by filePath. Create directory filePath if it does not exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_file_content_with_http_info(file_path, content_md5, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file_path: Full path to upload file to (required)
        :param str content_md5: Signature of file contents (required)
        :return: FileInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_path', 'content_md5']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_file_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_path' is set
        if ('file_path' not in params or
                params['file_path'] is None):
            raise ValueError("Missing the required parameter `file_path` when calling `put_file_content`")  # noqa: E501
        # verify the required parameter 'content_md5' is set
        if ('content_md5' not in params or
                params['content_md5'] is None):
            raise ValueError("Missing the required parameter `content_md5` when calling `put_file_content`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'file_path' in params:
            path_params['filePath'] = params['file_path']  # noqa: E501

        query_params = []

        header_params = {}
        if 'content_md5' in params:
            header_params['Content-MD5'] = params['content_md5']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/octect-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/files/{filePath}/content', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FileInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)