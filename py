Here's the equivalent Python code for the provided C# snippet:

```python
import urllib.parse
import requests

dataproviderAPIURL = "http://www.nsroot.net/api/api23/get/"
json_query = """{
    "db": "XXX",
    "collection": "XX_*_XXX_CONFIG",
    "queryFilterMap": {},
    "selectColumns": ["_id", "Name", "Url", "RefreshFrequency", "ConnectionTimeout", "ReadTin1"]
}"""

encoded_query = urllib.parse.quote(json_query)
url = dataproviderAPIURL + encoded_query

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an exception for 4XX/5XX errors
    result_content = response.text
    str_json = result_content  # In Python, you might parse this with json.loads() if needed
    print(str_json)
except requests.exceptions.RequestException as e:
    print(f"Error making request: {e}")
```

### Key Notes:
1. Used the `requests` library which is the most common way to make HTTP requests in Python
2. URL encoding is handled with `urllib.parse.quote`
3. Added basic error handling with try/except
4. The response content is available as text via `response.text`
5. If you need to parse the JSON response, you could use `import json` and then `json.loads(result_content)`

For async operations (like the original C#'s `await`), you could use `aiohttp` instead of `requests`:

```python
import aiohttp
import asyncio
import urllib.parse

async def fetch_data():
    dataproviderAPIURL = "http://www.nsroot.net/api/api23/get/"
    json_query = """{
        "db": "XXX",
        "collection": "XX_*_XXX_CONFIG",
        "queryFilterMap": {},
        "selectColumns": ["_id", "Name", "Url", "RefreshFrequency", "ConnectionTimeout", "ReadTin1"]
    }"""
    
    encoded_query = urllib.parse.quote(json_query)
    url = dataproviderAPIURL + encoded_query
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result_content = await response.text()
            print(result_content)

# Run the async function
asyncio.run(fetch_data())
```