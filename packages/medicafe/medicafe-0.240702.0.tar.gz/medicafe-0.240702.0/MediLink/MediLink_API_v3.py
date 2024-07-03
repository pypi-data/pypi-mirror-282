import time
import requests
import yaml
import json
import os

# Importing configuration loader
try:
    from MediLink import MediLink_ConfigLoader
except ImportError:
    import MediLink_ConfigLoader

# Utility to load configurations from JSON, YAML, or Swagger files
class ConfigLoader:
    @staticmethod
    def load_configuration(config_path=os.path.join(os.path.dirname(__file__), '..', 'json', 'config.json'), 
                           crosswalk_path=os.path.join(os.path.dirname(__file__), '..', 'json', 'crosswalk.json')):
        # Loads endpoint configuration, credentials, and other settings from JSON or YAML files.
        return MediLink_ConfigLoader.load_configuration(config_path, crosswalk_path)

    @staticmethod
    def load_swagger_file(swagger_path):
        # Loads Swagger API definitions from a JSON or YAML file.
        # Parameters: swagger_path (str): Path to the Swagger file.
        # Returns: dict: Parsed Swagger definitions.
        try:
            print("Attempting to load Swagger file: {}".format(swagger_path))
            with open(swagger_path, 'r') as swagger_file:
                if swagger_path.endswith('.yaml') or swagger_path.endswith('.yml'):
                    print("Parsing YAML file: {}".format(swagger_path))
                    swagger_data = yaml.safe_load(swagger_file)
                elif swagger_path.endswith('.json'):
                    print("Parsing JSON file: {}".format(swagger_path))
                    swagger_data = json.load(swagger_file)
                else:
                    raise ValueError("Unsupported Swagger file format.")
                
            print("Successfully loaded Swagger file: {}".format(swagger_path))
            return swagger_data
        except ValueError as e:
            print("Error parsing Swagger file {}: {}".format(swagger_path, e))
            MediLink_ConfigLoader.log("Error parsing Swagger file {}: {}".format(swagger_path, e), level="ERROR")
        except FileNotFoundError:
            print("Swagger file not found: {}".format(swagger_path))
            MediLink_ConfigLoader.log("Swagger file not found: {}".format(swagger_path), level="ERROR")
        except Exception as e:
            print("Unexpected error loading Swagger file {}: {}".format(swagger_path, e))
            MediLink_ConfigLoader.log("Unexpected error loading Swagger file {}: {}".format(swagger_path, e), level="ERROR")
        return None

# Class for caching tokens to manage token lifetimes efficiently
class TokenCache:
    def __init__(self):
        self.tokens = {}

    def get(self, endpoint_name, current_time):
        token_info = self.tokens.get(endpoint_name, {})
        if token_info and token_info['expires_at'] > current_time:
            return token_info['access_token']
        return None

    def set(self, endpoint_name, access_token, expires_in, current_time):
        self.tokens[endpoint_name] = {
            'access_token': access_token,
            'expires_at': current_time + expires_in - 120
        }

# Abstract base class for API clients to ensure a consistent interface
class BaseAPIClient:
    def __init__(self, config):
        self.config = config
        self.token_cache = TokenCache()

    def get_access_token(self, endpoint_name):
        raise NotImplementedError("Subclasses should implement this!")

    def make_api_call(self, endpoint_name, call_type, url_extension="", params=None, data=None):
        raise NotImplementedError("Subclasses should implement this!")

# Concrete implementation of APIClient inheriting from BaseAPIClient
class APIClient(BaseAPIClient):
    def __init__(self):
        config, _ = MediLink_ConfigLoader.load_configuration()
        super().__init__(config)

    def get_access_token(self, endpoint_name):
        current_time = time.time()
        cached_token = self.token_cache.get(endpoint_name, current_time)
        if cached_token:
            MediLink_ConfigLoader.log("Using cached token for endpoint: {}".format(endpoint_name), level="INFO")
            return cached_token

        # Load endpoint configuration
        endpoint_config = self.config['MediLink_Config']['endpoints'][endpoint_name]
        data = {
            'grant_type': 'client_credentials',
            'client_id': endpoint_config['client_id'],
            'client_secret': endpoint_config['client_secret'],
            'scope': 'hipaa'
        }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        # Request new token
        response = requests.post(endpoint_config['token_url'], headers=headers, data=data)
        response.raise_for_status()
        token_data = response.json()
        access_token = token_data['access_token']
        expires_in = token_data.get('expires_in', 3600)

        # Cache the new token
        self.token_cache.set(endpoint_name, access_token, expires_in, current_time)
        MediLink_ConfigLoader.log("Obtained new token for endpoint: {}".format(endpoint_name), level="INFO")
        return access_token

    def make_api_call(self, endpoint_name, call_type, url_extension="", params=None, data=None):
        # Obtain the access token
        token = self.get_access_token(endpoint_name)
        headers = {'Authorization': 'Bearer {}'.format(token), 'Accept': 'application/json'}
        url = self.config['MediLink_Config']['endpoints'][endpoint_name]['api_url'] + url_extension

        # Perform the appropriate API call based on call_type
        if call_type == 'GET':
            response = requests.get(url, headers=headers, params=params)
        elif call_type == 'POST':
            headers['Content-Type'] = 'application/json'
            response = requests.post(url, headers=headers, json=data)
        elif call_type == 'DELETE':
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError("Unsupported call type")

        # Log and raise error if the response is not successful
        if response.status_code >= 400:
            error_message = "Error {}: {}".format(response.status_code, response.text)
            MediLink_ConfigLoader.log(error_message, level="ERROR")
            response.raise_for_status()

        return response.json()

# Function to fetch payer name from the API, iterating through endpoints dynamically
def fetch_payer_name_from_api(payer_id, config, primary_endpoint='AVAILITY'):
    client = APIClient()
    config, _ = MediLink_ConfigLoader.load_configuration()
    endpoints = config['MediLink_Config']['endpoints']

    # Determine the order of endpoints to try
    if primary_endpoint and primary_endpoint in endpoints:
        endpoint_order = [primary_endpoint] + [endpoint for endpoint in endpoints if endpoint != primary_endpoint]
    else:
        endpoint_order = list(endpoints.keys())

    # Iterate through available endpoints in specified order
    for endpoint_name in endpoint_order:
        try:
            response = client.make_api_call(endpoint_name, 'GET', config['MediLink_Config']['endpoints'][endpoint_name].get('payer_list_endpoint', '/availity-payer-list'), {'payerId': payer_id})
            payers = response.get('payers', [])
            if payers:
                payer_name = payers[0].get('displayName', payers[0].get('name'))
                MediLink_ConfigLoader.log("Successfully found payer at {} for ID {}: {}".format(endpoint_name, payer_id, payer_name), level="INFO")
                return payer_name
            else:
                MediLink_ConfigLoader.log("No payer found at {} for ID: {}. Trying next available endpoint.".format(endpoint_name, payer_id), level="INFO")
        except Exception as e:
            MediLink_ConfigLoader.log("API call to {} failed: {}".format(endpoint_name, e), level="ERROR")

    error_message = "All endpoints exhausted for Payer ID {}.".format(payer_id)
    MediLink_ConfigLoader.log(error_message, level="CRITICAL")
    raise ValueError(error_message)

# Entry point for the script
if __name__ == "__main__":
    client = APIClient()
    try:
        # Fetch and print payer name
        payer_name = fetch_payer_name_from_api("87726", client.config)
        print("TEST API: Payer Name: {}".format(payer_name))
    except Exception as e:
        print("TEST API: Error: {}".format(e))