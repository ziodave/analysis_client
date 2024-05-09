# analysis_client.AnalysesApi

All URIs are relative to *https://api.wordlift.io/analysis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](AnalysesApi.md#create) | **POST** /analysis/analyses | Create


# **create**
> AnalysesResponse create(analyses_request)

Create

Create an analysis request

### Example

* Api Key Authentication (ApiKey):

```python
import analysis_client
from analysis_client.models.analyses_request import AnalysesRequest
from analysis_client.models.analyses_response import AnalysesResponse
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
    api_instance = analysis_client.AnalysesApi(api_client)
    analyses_request = analysis_client.AnalysesRequest() # AnalysesRequest | 

    try:
        # Create
        api_response = await api_instance.create(analyses_request)
        print("The response of AnalysesApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalysesApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analyses_request** | [**AnalysesRequest**](AnalysesRequest.md)|  | 

### Return type

[**AnalysesResponse**](AnalysesResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/x.wordlift.analysis+json;version=3

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**500** | Uh oh, something went wrong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

