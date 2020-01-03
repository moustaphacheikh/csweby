# swagger_client.SyncApi

All URIs are relative to *http://sistaconsult.tech/api/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sync_history**](SyncApi.md#get_sync_history) | **GET** /dictionaries/{dictName}/syncs | Get sync history


# **get_sync_history**
> SyncHistory get_sync_history(dict_name, _from=_from, to=to, device_id=device_id, limit=limit, offset=offset)

Get sync history

List synchronizations for the server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SyncApi()
dict_name = 'dict_name_example' # str | Name of dictionary containing case
_from = '2013-10-20T19:20:30+01:00' # datetime | Start date in RFC3339 format ( e.g. 1985-04-12T23:20:50.52Z) (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | End date in RFC3339 format ( e.g. 1985-04-12T23:20:50.52Z) (optional)
device_id = 'device_id_example' # str | Device Id (optional)
limit = 56 # int | maximum number of cases in response (optional)
offset = 56 # int | zero-based index of first case to return in response (optional)

try:
    # Get sync history
    api_response = api_instance.get_sync_history(dict_name, _from=_from, to=to, device_id=device_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_sync_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dict_name** | **str**| Name of dictionary containing case | 
 **_from** | **datetime**| Start date in RFC3339 format ( e.g. 1985-04-12T23:20:50.52Z) | [optional] 
 **to** | **datetime**| End date in RFC3339 format ( e.g. 1985-04-12T23:20:50.52Z) | [optional] 
 **device_id** | **str**| Device Id | [optional] 
 **limit** | **int**| maximum number of cases in response | [optional] 
 **offset** | **int**| zero-based index of first case to return in response | [optional] 

### Return type

[**SyncHistory**](SyncHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

