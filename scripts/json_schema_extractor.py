"""Extract JSON schemas"""
import csv
import requests
from request_header import RequestHeader

class JSONSchemaExtractor:
    AUTHENTICATION = {
        'authMechanism': 'SCRAM-SHA-1',
        'userName': 'mongoadmin',
        'password': 'secret',
        'authDatabase': 'admin'
    }
    HEADER = RequestHeader().get_auth_header()

    def __init__(self, base_url):
        self.base_url = base_url

    def send_request_to_server(self, collection_name):
        """Send a POST request to the server to extract raw schema for a given collection."""
        POST_URL = f'{self.base_url}/api/batch/rawschema/steps/all'
        payload = {
            'authentication': self.AUTHENTICATION,
            'port': '27017',
            'address': 'mongodb',
            'databaseName': 'jsonschemadiscovery',
            'collectionName': collection_name
        }

        try:
            response = requests.post(POST_URL, json=payload, headers=self.HEADER)
            if response.status_code == 200:
                return 'ok'
            else:
                print(f'Error Code: {response.status_code}\n{response.text}')
                return 'error'
        except requests.exceptions.RequestException as e:
            print(f'Request failed: {e}')
            return 'error'

    def save_analysis_to_csv(self, results, csv_file='/home/repro/JSONSchemaDiscovery/csv/experiment_results.csv'):
        """Save analysis results to a CSV file."""
        fieldnames = ['Collection', 'N_JSON', 'RS', 'ROrd']
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for result in results:
                writer.writerow({
                    'Collection': result['collectionName'],
                    'N_JSON': result['collectionCount'],
                    'RS': result['uniqueUnorderedCount'],
                    'ROrd': result['uniqueOrderedCount']
                })

    def get_analysis(self):
        """Retrieve and analyze batch data from the server."""
        schema_results = []
        GET_URL = f'{self.base_url}/api/batches'
        
        try:
            response = requests.get(GET_URL, headers=self.HEADER)
            if response.status_code == 200:
                data = response.json()
                for result in data:
                    # Extract relevant information from the server response
                    schema_results.append({
                        '_id': result.get('_id', 'N/A'),
                        'collectionName': result.get('collectionName', 'N/A'),
                        'collectionCount': result.get('collectionCount', 'N/A'),
                        'uniqueUnorderedCount': result.get('uniqueUnorderedCount', 'N/A'),
                        'uniqueOrderedCount': result.get('uniqueOrderedCount', 'N/A')
                    })
                return schema_results
            else:
                return f'Failed to retrieve data. Status Code: {response.status_code}'
        except requests.exceptions.RequestException as e:
            print(f'Request failed: {e}')
            return None