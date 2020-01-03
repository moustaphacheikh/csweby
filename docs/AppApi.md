# swagger_client.AppApi

All URIs are relative to *http://sistaconsult.tech/api/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_app**](AppApi.md#delete_app) | **DELETE** /apps/{appname} | Delete app
[**get_app**](AppApi.md#get_app) | **GET** /apps/{appname} | Get app package
[**get_apps**](AppApi.md#get_apps) | **GET** /apps | Get list of applications
[**update_app**](AppApi.md#update_app) | **PUT** /apps/{appname} | Upload app package


# **delete_app**
> delete_app(appname)

Delete app

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppApi()
appname = 'appname_example' # str | The name of the app to be deleted

try:
    # Delete app
    api_instance.delete_app(appname)
except ApiException as e:
    print("Exception when calling AppApi->delete_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appname** | **str**| The name of the app to be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app**
> file get_app(appname)

Get app package

Get application deployment package (csapb file) for named application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppApi()
appname = 'appname_example' # str | name of app to download

try:
    # Get app package
    api_response = api_instance.get_app(appname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->get_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appname** | **str**| name of app to download | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apps**
> list[ApplicationDeploymentSpecification] get_apps()

Get list of applications

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppApi()

try:
    # Get list of applications
    api_response = api_instance.get_apps()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->get_apps: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApplicationDeploymentSpecification]**](ApplicationDeploymentSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app**
> update_app(appname)

Upload app package

Upload application package (csapb file) to server.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppApi()
appname = 'appname_example' # str | Name of app to upload

try:
    # Upload app package
    api_instance.update_app(appname)
except ApiException as e:
    print("Exception when calling AppApi->update_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appname** | **str**| Name of app to upload | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octect-stream
 - **Accept**: application/json, text/plain, application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

