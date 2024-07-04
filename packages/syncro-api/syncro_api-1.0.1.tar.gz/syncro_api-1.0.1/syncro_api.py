import os
import requests

def get_syncro_customers():
    if syncro_api_key is None: syncro_api_key = os.environ.get('SYNCRO_API_KEY', None)
    if syncro_api_baseurl is None: syncro_api_baseurl = os.environ.get('SYNCRO_API_BASEURL', None)
    if syncro_api_key is None or syncro_api_baseurl is None:
        return "Missing API Key or Base URL"
    else:
        return "Syncro API Key: " + syncro_api_key + " Base
    syncro_api_url = syncro_api_baseurl + '/api/v1/customers'
    headers = {
        'Authorization': 'Bearer ' + syncro_api_key,
        'Content-Type': 'application/json'
    }
    try:
        response = requests.get(syncro_api_url, headers=headers)
        return response.json()
    except requests.exceptions.RequestException as e:
        return e
    
def get_syncro_customers_managed():
    #customers.properties["Managed Status"] 35984
    if syncro_api_key is None: syncro_api_key = os.environ.get('SYNCRO_API_KEY', None)
    if syncro_api_baseurl is None: syncro_api_baseurl = os.environ.get('SYNCRO_API_BASEURL', None)
    if syncro_api_key is None or syncro_api_baseurl is None:
        return "Missing API Key or Base URL"
    syncro_api_url = syncro_api_baseurl + '/api/v1/customers'
    headers = {
        'Authorization': 'Bearer ' + syncro_api_key,
        'Content-Type': 'application/json'
    }
    try:
        response = requests.get(syncro_api_url, headers=headers)
        all_customers = response.json()
        managed_customers = []
        for customer in all_customers:
            if customer.properties["Managed Status"] == 35984:
                managed_customers.append(customer)
        return managed_customers
    except requests.exceptions.RequestException as e:
        return e