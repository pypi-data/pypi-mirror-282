# basic-rest-endpoint

For a REST API, use the BasicRestEndpoint class.

This class allows easily creating a task for an endpoint. For example, say we want to integrate with example.com's
indicator API. Here is a table of what their API looks like.

Endpoint	HTTP Method	URL Parameters
https://example.com/api/indicator	GET	indicator_id (int)
https://example.com/api/indicator	POST/PATCH	indicator_name, indicator_value
https://example.com/api/indicator/{id}	DELETE	(none)
So we have 3 endpoints, each with different HTTP Methods and parameters, but the same base URL.
We can create a superclass for this integration, let's call it ExampleIntegration

```python
from basic_rest_endpoint import BasicRestEndpoint


class ExampleIntegration(BasicRestEndpoint):
    def __init__(self, context):
        super(ExampleIntegration, self).__init__(context.asset["host"]
        # raise_for_status=False  # If we wanted to supress non-200 http codes being raised, set this to False
        )
```
## Basic Request
To make a request using this library, you just use `self.request(<method>, <endpoint>, **kwargs)`
Where `<method>` is an HTTP method, `<endpoint>` is the URL relative to the host, and `**kwargs`
are optional params to pass into the requests.request(...) call

## Basic GET Example
Now we create a task, say for the GET /api/indicator endpoint
```python
from sw_example import ExampleIntegration  # Import our superclass from above

class SwMain(ExampleIntegration):
    endpoint = "/api/indicator"
    method = "GET"

    def __init__(self, context):
        super(SwMain, self).__init__(context)
        self.kwargs['params'] = {"indicator_id": context.inputs["indicator_id"]}  # Get indicator from inputs
```
But we didn't actually make a request here! It is all handled by the BasicRestEndpoint superclass.
The params kwarg is passed into self.request which is used to create the full url with self.host that
ends up like https://example.com/api/indicator?indicator_id=<id>

## Basic POST Example
But what if the data required from the API isn't in the URL params? And what if the data returned from
wthe API isn't suitable for just returning, or needs some parsing?

Let's take a look at the second endpoint, the POST /api/indicator.
```python
from sw_example import ExampleIntegration  # Import our superclass from above


class SwMain(ExampleIntegration):
    endpoint = "/api/indicator"
    method = "POST"

    def parse_response(self, response):
        data = response.json()  # Basically json.loads(response.text)
        return data["data"]

    def __init__(self, context):
        super(SwMain, self).__init__(context)
        self.kwargs['json'] = {
            "indicator_name": context.inputs["indicator_name"],  # Get indicator from inputs
            "indicator_value": context.inputs["indicator_value"]
        }
}
```
This time, the data is passed in under the `json` parameter to requests which automatically formats our data for
us in the POST body. If the data were non-json, we would use `data` instead. We also parsed out the data returned,
only returning the JSON under the `data` key.

## Basic DELETE Example
Similarly to a variable request method, we can have a variable URL. This is quite trivial
```python
class SwMain(ExampleIntegration):
    method = "DELETE"

    def __init__(self, context):
        super(SwMain, self).__init__(context)
        self.endpoint = f"/api/indicator/{context.inputs['iid']}"
```

## Authentication
But what if example.com required authentication to make those calls?
There are options for these authentication methods, Basic Auth, Header Auth, Param Auth, and Custom Auth.

### Basic Auth
```python
from basic_rest_endpoint import BasicRestEndpoint

class ExampleIntegration(BasicRestEndpoint):
    def __init__(self, context):
        super(ExampleIntegration, self).__init__(
            host=context.asset["host"],
            auth=(context.asset["username"], context.asset["password"])
        )
```
This auth is handled by requests directly, and automatically parses it out and inserts it into the headers for us

### Header Auth
```python
from basic_rest_endpoint import BasicRestEndpoint, HeaderAuth

class ExampleIntegration(BasicRestEndpoint):
    def __init__(self, context):
        super(ExampleIntegration, self).__init__(
            host=context.asset["host"],
            auth=HeaderAuth({"X-api-key": context.asset["api_key"]})
        )
```
This auth is when an API requires a certain header to be sent in each request

### Param Auth
```python
from basic_rest_endpoint import BasicRestEndpoint, ParamAuth

class ExampleIntegration(BasicRestEndpoint):
    def __init__(self, context):
        super(ExampleIntegration, self).__init__(
            host=context.asset["host"],
            auth=ParamAuth({"username": context.asset["username"], "password" context.asset["password"]})
        )
``````
This auth is used when the URL contains the authenticating information, like 
https://example.com/api/indicator?indicator_id=<id>&username=<username>&password=<password>

## Polling Requests
Sometimes an API will return a status that indicates that they are still processing your request, 
and you will need to send requests until the processing is complete. We can use the polling request here.
```python
# def poll_request(self, method, endpoint, step=5, timeout=60, poll_func=None, **kwargs):

# By default the polling stops if you receive a 200
# Poll /my/endpoint with default settings
self.poll_request("GET", "/my/endpoint")

# Poll /my/endpoint every 5 seconds, giving up after 20 seconds
self.poll_request("GET", "/my/endpoint", step=5, timeout=60)

# Custom polling function to check if the json returned says it's finished
def my_poll_func(poll_method, poll_endpoint, poll_kwargs):
    result = self.request(poll_method, poll_endpoint, **poll_kwargs)
    if r.json()["status"].lower() == "done":
        return result  # Return the final response
    else:
        return False  # If what we return is falsey, then it will continue to poll

self.poll_request("GET" "/my/endpoint", poll_func=my_poll_func)
```

## Basic Pagination
An API may return a single page in a list of results of pages. To make this easy to process,
inherit from BasicPaginationEndpoint and implement the following functions
```python
from basic_rest_endpoint import BasicRestPaginationEndpoint

def MyIntegration(BasicRestPaginationEndpoint):
    def __init__(self, context):
        # Same init as BasicRestEndpoint, excluding in example

    def get_next_page(self, response):
        data = response.json()
        if "next" in data:
            return data["next"]  # Return the URL for the next call
        else:
            return None  # If this function returns None, all pages have been seen

    def parse_response(self, response):
        data = response.json()
        data.pop("next", None)  # Remove useless keys/clean data of each response here
        return data

    def combine_responses(self, results):
        # Results is a list of parsed responses, from self.parse_response
        all_data = []
        for result in results:
            all_data.extend(result)  # Use .extend to take [1,2,3] + [4,5] -> [1,2,3,4,5]

        return all_data
```

## Link Headers Pagination
Some (very few) APIs implement a standard called "Link Headers" which makes pagination very easy.
This implementation is completely done so all you have to do is implement combine_responses
```python
from basic_rest_endpoint import LinkHeadersPaginationEndpoint

def MyIntegration(LinkHeadersPaginationEndpoint):
    def __init__(self, context):
        # Same init as BasicRestEndpoint, excluding in example

    def combine_responses(self, results):
        # do parsing here
```

## Asset Parser
The `asset_parser` function is used to split the incoming Context object into a super() call for BasicRestEndpoint

In the following example, the Context object is parsed, and with auth set to "basic" the username and password are automatically set up for Basic HTTP auth.
```python
from basic_rest_endpoint import BasicRestEndpoint, asset_parser


class MyIntegration(BasicRestEndpoint):
    def __init__(self, context):
        super(MyIntegration, self).__init__(**asset_parser(context, auth="basic"))


class Context(object):
    asset = {
        "host": "abc.com",
        "username": "bb",
        "password": "cc",
        "verify_ssl": False,
        "http_proxy": None
    }
```