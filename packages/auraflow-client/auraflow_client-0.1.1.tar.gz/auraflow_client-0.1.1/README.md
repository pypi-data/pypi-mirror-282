# AuraFlow Client Library

The AuraFlow Client Library is a Python package for easy interaction with the AuraFlow API. It enables users to seamlessly retrieve data using their API key.

## Installation

Install the AuraFlow Client Library using pip:

```bash
pip install auraflow_client
```

## Configuration
Before using the library, you need to set up your AuraFlow API key. You can do this by setting an environment variable:

```bash
export AURAFLOW_API_KEY='your_api_key_here'
```

## Usage
Here is a simple example of how to use the library to post data and get a response:
```python
from auraflow_client.api import get_data
from auraflow_client.config import get_api_key

# Ensure your API key is configured as per the Configuration section
api_key = get_api_key()  # or use your own method to provide the API key

# Define your parameters to send in the POST request
body_params = {
    'ticker_list': ['^GSPC'],       # List of tickers to retrieve data for
    "start": '2020-01-01',          # Start date for data retrieval in any format
    "end": '2023-01-01',            # End date for data retrieval in any format
    "source": 'yahoo',              # String specifying the data source. This should match the data provider you have linked with your account on the AuraFlow web portal. Valid options depend on the providers you have configured and authorized.
    "data_format": 'json'           # Format of the data returned, options are 'json' and 'csv' only
}

# Get data
data = get_data(api_key, body_params)
print(data)
```