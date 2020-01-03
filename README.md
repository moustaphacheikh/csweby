# swagger-client
Web API for synchronizing data and files from devices in the field to a web server. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
appname = 'appname_example' # str | The name of the app to be deleted

try:
    # Delete app
    api_instance.delete_app(appname)
except ApiException as e:
    print("Exception when calling AppApi->delete_app: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://sistaconsult.tech/api/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AppApi* | [**delete_app**](docs/AppApi.md#delete_app) | **DELETE** /apps/{appname} | Delete app
*AppApi* | [**get_app**](docs/AppApi.md#get_app) | **GET** /apps/{appname} | Get app package
*AppApi* | [**get_apps**](docs/AppApi.md#get_apps) | **GET** /apps | Get list of applications
*AppApi* | [**update_app**](docs/AppApi.md#update_app) | **PUT** /apps/{appname} | Upload app package
*CaseApi* | [**add_or_update_case**](docs/CaseApi.md#add_or_update_case) | **POST** /dictionaries/{dictName}/cases | Add or update new cases to dictionary
*CaseApi* | [**delete_case**](docs/CaseApi.md#delete_case) | **DELETE** /dictionaries/{dictName}/cases/{caseId} | Delete existing case
*CaseApi* | [**get_case_by_id**](docs/CaseApi.md#get_case_by_id) | **GET** /dictionaries/{dictName}/cases/{caseId} | Get case by id
*CaseApi* | [**get_cases_for_dict**](docs/CaseApi.md#get_cases_for_dict) | **GET** /dictionaries/{dictName}/cases | Get cases for dictionary
*CaseApi* | [**get_sync_history**](docs/CaseApi.md#get_sync_history) | **GET** /dictionaries/{dictName}/syncs | Get sync history
*CaseApi* | [**update_case**](docs/CaseApi.md#update_case) | **PUT** /dictionaries/{dictName}/cases/{caseId} | Update existing case
*DictionaryApi* | [**add_dictionary**](docs/DictionaryApi.md#add_dictionary) | **POST** /dictionaries | Add new dictionary
*DictionaryApi* | [**delete_dictionary**](docs/DictionaryApi.md#delete_dictionary) | **DELETE** /dictionaries/{dictName} | Delete dictionary
*DictionaryApi* | [**get_dict_by_name**](docs/DictionaryApi.md#get_dict_by_name) | **GET** /dictionaries/{dictName} | Get dictionary by name
*DictionaryApi* | [**list_dictionaries**](docs/DictionaryApi.md#list_dictionaries) | **GET** /dictionaries | List dictionaries
*FileApi* | [**get_file_content**](docs/FileApi.md#get_file_content) | **GET** /files/{filePath}/content | Get file
*FileApi* | [**get_file_info**](docs/FileApi.md#get_file_info) | **GET** /files/{filePath} | Get file
*FileApi* | [**get_files_in_folder**](docs/FileApi.md#get_files_in_folder) | **GET** /folders/{folderPath} | Get files in folder
*FileApi* | [**put_file_content**](docs/FileApi.md#put_file_content) | **PUT** /files/{filePath}/content | Upload file
*FolderApi* | [**get_files_in_folder**](docs/FolderApi.md#get_files_in_folder) | **GET** /folders/{folderPath} | Get files in folder
*ServerApi* | [**get_server_info**](docs/ServerApi.md#get_server_info) | **GET** /server | Get server details
*SyncApi* | [**get_sync_history**](docs/SyncApi.md#get_sync_history) | **GET** /dictionaries/{dictName}/syncs | Get sync history
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /users/{username} | Delete user
*UserApi* | [**get_user_by_name**](docs/UserApi.md#get_user_by_name) | **GET** /users/{username} | Get user by user name
*UserApi* | [**get_users**](docs/UserApi.md#get_users) | **GET** /users | Get list of users
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /users/{username} | Updated user


## Documentation For Models

 - [ApplicationDeploymentSpecification](docs/ApplicationDeploymentSpecification.md)
 - [ApplicationDeploymentSpecificationDeployment](docs/ApplicationDeploymentSpecificationDeployment.md)
 - [ApplicationDeploymentSpecificationDictionaries](docs/ApplicationDeploymentSpecificationDictionaries.md)
 - [ApplicationDeploymentSpecificationFiles](docs/ApplicationDeploymentSpecificationFiles.md)
 - [Case](docs/Case.md)
 - [CaseList](docs/CaseList.md)
 - [ClockVector](docs/ClockVector.md)
 - [ClockVectorInner](docs/ClockVectorInner.md)
 - [Dictionary](docs/Dictionary.md)
 - [Field](docs/Field.md)
 - [FileInfo](docs/FileInfo.md)
 - [FileListing](docs/FileListing.md)
 - [Note](docs/Note.md)
 - [NoteList](docs/NoteList.md)
 - [PartialSaveStatus](docs/PartialSaveStatus.md)
 - [RecordList](docs/RecordList.md)
 - [ServerInfo](docs/ServerInfo.md)
 - [SyncHistory](docs/SyncHistory.md)
 - [SyncHistoryEntry](docs/SyncHistoryEntry.md)
 - [User](docs/User.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



