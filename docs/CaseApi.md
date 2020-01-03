# swagger_client.CaseApi

All URIs are relative to *http://sistaconsult.tech/api/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_or_update_case**](CaseApi.md#add_or_update_case) | **POST** /dictionaries/{dictName}/cases | Add or update new cases to dictionary
[**delete_case**](CaseApi.md#delete_case) | **DELETE** /dictionaries/{dictName}/cases/{caseId} | Delete existing case
[**get_case_by_id**](CaseApi.md#get_case_by_id) | **GET** /dictionaries/{dictName}/cases/{caseId} | Get case by id
[**get_cases_for_dict**](CaseApi.md#get_cases_for_dict) | **GET** /dictionaries/{dictName}/cases | Get cases for dictionary
[**get_sync_history**](CaseApi.md#get_sync_history) | **GET** /dictionaries/{dictName}/syncs | Get sync history
[**update_case**](CaseApi.md#update_case) | **PUT** /dictionaries/{dictName}/cases/{caseId} | Update existing case


# **add_or_update_case**
> add_or_update_case(dict_name, case, x_csw_device, if_match=if_match)

Add or update new cases to dictionary

Upload new cases to the dictionary named dictName

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CaseApi()
dict_name = 'dict_name_example' # str | Name of dictionary to add case to
case = swagger_client.CaseList() # CaseList | Cases to add/update
x_csw_device = 'x_csw_device_example' # str | id of device sending cases
if_match = 'if_match_example' # str | etag from previous call. If server does not have this etag it will return status 412. (optional)

try:
    # Add or update new cases to dictionary
    api_instance.add_or_update_case(dict_name, case, x_csw_device, if_match=if_match)
except ApiException as e:
    print("Exception when calling CaseApi->add_or_update_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dict_name** | **str**| Name of dictionary to add case to | 
 **case** | [**CaseList**](CaseList.md)| Cases to add/update | 
 **x_csw_device** | **str**| id of device sending cases | 
 **if_match** | **str**| etag from previous call. If server does not have this etag it will return status 412. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain, application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_case**
> delete_case(dict_name, case_id)

Delete existing case

Delete existing case from the dictionary named dictName with id caseId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CaseApi()
dict_name = 'dict_name_example' # str | Name of dictionary containing case
case_id = 'case_id_example' # str | Id of case to delete (GUID)

try:
    # Delete existing case
    api_instance.delete_case(dict_name, case_id)
except ApiException as e:
    print("Exception when calling CaseApi->delete_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dict_name** | **str**| Name of dictionary containing case | 
 **case_id** | **str**| Id of case to delete (GUID) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_case_by_id**
> Case get_case_by_id(dict_name, case_id)

Get case by id

Download case for the dictionary named dictName with id caseId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CaseApi()
dict_name = 'dict_name_example' # str | Name of dictionary to get cases from
case_id = 'case_id_example' # str | Id of case to download (GUID)

try:
    # Get case by id
    api_response = api_instance.get_case_by_id(dict_name, case_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseApi->get_case_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dict_name** | **str**| Name of dictionary to get cases from | 
 **case_id** | **str**| Id of case to download (GUID) | 

### Return type

[**Case**](Case.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cases_for_dict**
> CaseList get_cases_for_dict(dict_name, x_csw_universe=x_csw_universe, x_csw_case_range_start_after=x_csw_case_range_start_after, x_csw_case_range_count=x_csw_case_range_count, x_csw_exclude_revisions=x_csw_exclude_revisions, x_csw_device=x_csw_device, if_match=if_match)

Get cases for dictionary

Download cases for the dictionary named dictName

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CaseApi()
dict_name = 'dict_name_example' # str | Name of dictionary to get cases from
x_csw_universe = 'x_csw_universe_example' # str | universe to limit cases returned (optional)
x_csw_case_range_start_after = 'x_csw_case_range_start_after_example' # str | only return cases whose guid is strictly greater (alphabetically) than this value. Used for paging results. (optional)
x_csw_case_range_count = 56 # int | limit number cases returned to this number of cases. (optional)
x_csw_exclude_revisions = ['x_csw_exclude_revisions_example'] # list[str] | exclude cases from following revisions from the result. Allows device to avoid downloading cases that it previously uploaded. (optional)
x_csw_device = 'x_csw_device_example' # str | id of device requesting cases (optional)
if_match = 'if_match_example' # str | etag from previous call. Only cases added/modified since this etag are returned. If server does not have this etag it will return status 412. (optional)

try:
    # Get cases for dictionary
    api_response = api_instance.get_cases_for_dict(dict_name, x_csw_universe=x_csw_universe, x_csw_case_range_start_after=x_csw_case_range_start_after, x_csw_case_range_count=x_csw_case_range_count, x_csw_exclude_revisions=x_csw_exclude_revisions, x_csw_device=x_csw_device, if_match=if_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CaseApi->get_cases_for_dict: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dict_name** | **str**| Name of dictionary to get cases from | 
 **x_csw_universe** | **str**| universe to limit cases returned | [optional] 
 **x_csw_case_range_start_after** | **str**| only return cases whose guid is strictly greater (alphabetically) than this value. Used for paging results. | [optional] 
 **x_csw_case_range_count** | **int**| limit number cases returned to this number of cases. | [optional] 
 **x_csw_exclude_revisions** | [**list[str]**](str.md)| exclude cases from following revisions from the result. Allows device to avoid downloading cases that it previously uploaded. | [optional] 
 **x_csw_device** | **str**| id of device requesting cases | [optional] 
 **if_match** | **str**| etag from previous call. Only cases added/modified since this etag are returned. If server does not have this etag it will return status 412. | [optional] 

### Return type

[**CaseList**](CaseList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = swagger_client.CaseApi()
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
    print("Exception when calling CaseApi->get_sync_history: %s\n" % e)
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

# **update_case**
> update_case(dict_name, case_id, case)

Update existing case

Overwrite existing case for the dictionary named dictName with id caseId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CaseApi()
dict_name = 'dict_name_example' # str | Name of dictionary containing case
case_id = 'case_id_example' # str | Id of case to update (GUID)
case = swagger_client.Case() # Case | Case to update

try:
    # Update existing case
    api_instance.update_case(dict_name, case_id, case)
except ApiException as e:
    print("Exception when calling CaseApi->update_case: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dict_name** | **str**| Name of dictionary containing case | 
 **case_id** | **str**| Id of case to update (GUID) | 
 **case** | [**Case**](Case.md)| Case to update | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json, text/plain, application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

