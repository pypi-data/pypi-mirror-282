import requests


def get_data(api_key, data):
    """Fetch data from AuraFlow API."""
    url = 'https://unba.logixsy.com/api/open_api/'
    headers = {'Authorization': f'Bearer {api_key}'}

    response = requests.post(url, headers=headers, data=data)

    return response.json(), response.status_code
