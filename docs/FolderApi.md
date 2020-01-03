# swagger_client.FolderApi

All URIs are relative to *http://sistaconsult.tech/api/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_files_in_folder**](FolderApi.md#get_files_in_folder) | **GET** /folders/{folderPath} | Get files in folder


# **get_files_in_folder**
> FileListing get_files_in_folder(folder_path)

Get files in folder

Get file info for files in the given folder

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FolderApi()
folder_path = 'folder_path_example' # str | path of folder to list contents of

try:
    # Get files in folder
    api_response = api_instance.get_files_in_folder(folder_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderApi->get_files_in_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_path** | **str**| path of folder to list contents of | 

### Return type

[**FileListing**](FileListing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

