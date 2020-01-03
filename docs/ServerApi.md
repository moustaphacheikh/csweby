# swagger_client.ServerApi

All URIs are relative to *http://sistaconsult.tech/api/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_server_info**](ServerApi.md#get_server_info) | **GET** /server | Get server details


# **get_server_info**
> ServerInfo get_server_info()

Get server details

Get information about server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()

try:
    # Get server details
    api_response = api_instance.get_server_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_server_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerInfo**](ServerInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

