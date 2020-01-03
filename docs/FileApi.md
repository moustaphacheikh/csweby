# swagger_client.FileApi

All URIs are relative to *http://sistaconsult.tech/api/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_file_content**](FileApi.md#get_file_content) | **GET** /files/{filePath}/content | Get file
[**get_file_info**](FileApi.md#get_file_info) | **GET** /files/{filePath} | Get file
[**get_files_in_folder**](FileApi.md#get_files_in_folder) | **GET** /folders/{folderPath} | Get files in folder
[**put_file_content**](FileApi.md#put_file_content) | **PUT** /files/{filePath}/content | Upload file


# **get_file_content**
> file get_file_content(file_path, if_none_match=if_none_match)

Get file

Get contents of file matching path.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileApi()
file_path = 'file_path_example' # str | path of file to download
if_none_match = 'if_none_match_example' # str | ETag value from previous response, 304 is returned if this matches current ETag (optional)

try:
    # Get file
    api_response = api_instance.get_file_content(file_path, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->get_file_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**| path of file to download | 
 **if_none_match** | **str**| ETag value from previous response, 304 is returned if this matches current ETag | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_info**
> FileInfo get_file_info(file_path)

Get file

Get contents of file matching path.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileApi()
file_path = 'file_path_example' # str | path of file to download for

try:
    # Get file
    api_response = api_instance.get_file_info(file_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->get_file_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**| path of file to download for | 

### Return type

[**FileInfo**](FileInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = swagger_client.FileApi()
folder_path = 'folder_path_example' # str | path of folder to list contents of

try:
    # Get files in folder
    api_response = api_instance.get_files_in_folder(folder_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->get_files_in_folder: %s\n" % e)
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

# **put_file_content**
> FileInfo put_file_content(file_path, content_md5)

Upload file

Put contents of file to server directory specified by filePath. Create directory filePath if it does not exist.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FileApi()
file_path = 'file_path_example' # str | Full path to upload file to
content_md5 = 'content_md5_example' # str | Signature of file contents

try:
    # Upload file
    api_response = api_instance.put_file_content(file_path, content_md5)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileApi->put_file_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**| Full path to upload file to | 
 **content_md5** | **str**| Signature of file contents | 

### Return type

[**FileInfo**](FileInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octect-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

