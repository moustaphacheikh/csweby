# swagger_client.DictionaryApi

All URIs are relative to *http://sistaconsult.tech/api/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dictionary**](DictionaryApi.md#add_dictionary) | **POST** /dictionaries | Add new dictionary
[**delete_dictionary**](DictionaryApi.md#delete_dictionary) | **DELETE** /dictionaries/{dictName} | Delete dictionary
[**get_dict_by_name**](DictionaryApi.md#get_dict_by_name) | **GET** /dictionaries/{dictName} | Get dictionary by name
[**list_dictionaries**](DictionaryApi.md#list_dictionaries) | **GET** /dictionaries | List dictionaries


# **add_dictionary**
> add_dictionary(dictionary)

Add new dictionary

Upload a new data dictionary to the server so that data    (cases) may be associated with it. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DictionaryApi()
dictionary = 'dictionary_example' # str | CSPro data dictionary as plain text

try:
    # Add new dictionary
    api_instance.add_dictionary(dictionary)
except ApiException as e:
    print("Exception when calling DictionaryApi->add_dictionary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dictionary** | **str**| CSPro data dictionary as plain text | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json, text/plain, application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dictionary**
> delete_dictionary(dict_name)

Delete dictionary

Delete a dictionary on the server and all associated data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DictionaryApi()
dict_name = 'dict_name_example' # str | Name of dictionary to delete

try:
    # Delete dictionary
    api_instance.delete_dictionary(dict_name)
except ApiException as e:
    print("Exception when calling DictionaryApi->delete_dictionary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dict_name** | **str**| Name of dictionary to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dict_by_name**
> str get_dict_by_name(dict_name)

Get dictionary by name

Download the dictionary named dictName

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DictionaryApi()
dict_name = 'dict_name_example' # str | Name of dictionary to download

try:
    # Get dictionary by name
    api_response = api_instance.get_dict_by_name(dict_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->get_dict_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dict_name** | **str**| Name of dictionary to download | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dictionaries**
> list[Dictionary] list_dictionaries()

List dictionaries

List names of available data dictionaries on this server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DictionaryApi()

try:
    # List dictionaries
    api_response = api_instance.list_dictionaries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionaryApi->list_dictionaries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Dictionary]**](Dictionary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

