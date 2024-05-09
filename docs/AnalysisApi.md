# analysis_client.AnalysisApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyse**](AnalysisApi.md#analyse) | **POST** /single | Analyse content
[**merge**](AnalysisApi.md#merge) | **POST** /merge | Analyse and Merge
[**v2_analysis**](AnalysisApi.md#v2_analysis) | **POST** /v2/analyze | Analyse Web Page


# **analyse**
> Response analyse(request)

Analyse content

Analyze the content provided with the request.

### Example

* Api Key Authentication (ApiKey):

```python
import analysis_client
from analysis_client.models.request import Request
from analysis_client.models.response import Response
from analysis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = analysis_client.Configuration(
    host = "https://api.wordlift.io/analysis"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with analysis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analysis_client.AnalysisApi(api_client)
    request = analysis_client.Request() # Request | 

    try:
        # Analyse content
        api_response = await api_instance.analyse(request)
        print("The response of AnalysisApi->analyse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->analyse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Request**](Request.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge**
> str merge(request)

Analyse and Merge

Analyze content and return the results merged as HTML code.

### Example

* Api Key Authentication (ApiKey):

```python
import analysis_client
from analysis_client.models.request import Request
from analysis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = analysis_client.Configuration(
    host = "https://api.wordlift.io/analysis"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with analysis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analysis_client.AnalysisApi(api_client)
    request = analysis_client.Request() # Request | 

    try:
        # Analyse and Merge
        api_response = await api_instance.merge(request)
        print("The response of AnalysisApi->merge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->merge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Request**](Request.md)|  | 

### Return type

**str**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_analysis**
> Response v2_analysis(request)

Analyse Web Page

Analyse the content of a webpage by using the `url` property of the request.

### Example

* Api Key Authentication (ApiKey):

```python
import analysis_client
from analysis_client.models.request import Request
from analysis_client.models.response import Response
from analysis_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wordlift.io/analysis
# See configuration.py for a list of all supported configuration parameters.
configuration = analysis_client.Configuration(
    host = "https://api.wordlift.io/analysis"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
async with analysis_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analysis_client.AnalysisApi(api_client)
    request = analysis_client.Request() # Request | 

    try:
        # Analyse Web Page
        api_response = await api_instance.v2_analysis(request)
        print("The response of AnalysisApi->v2_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysisApi->v2_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**Request**](Request.md)|  | 

### Return type

[**Response**](Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server Error |  -  |
**401** | Authentication Failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

