import requests

class UserAuthentication:
    """Class to manage user authentication."""
    
    LOGIN_URL = "http://localhost:4200/api/login"  # Class variable for the login URL
    REGISTER_URL = "http://localhost:4200/api/register"  # Class variable for the register URL
    
    @staticmethod
    def get_auth_token(email="repro@gmail.com", password="repro123"):
        """Logs in a user and returns an authentication token."""
        payload = {"email": email, "password": password}
        try:
            response = requests.post(UserAuthentication.LOGIN_URL, json=payload)
            if response.status_code == 200:
                return response.json().get('token', 'N/A')
            else:
                print(f'Error Code: {response.status_code}\n{response.text}')
                return 'error'
        except requests.exceptions.RequestException as e:
            print(f'Request failed: {e}')
            return 'error'
        
    @staticmethod
    def create_user(email="repro@gmail.com", username="repro", password="repro123"):
        """Registers a new user."""
        payload = {"email": email, "username": username, "password": password}
        try:
            response = requests.post(UserAuthentication.REGISTER_URL, json=payload)
            if response.status_code == 200:
                print(" User registration successful.")
                return 'ok'
            else:
                print(f'Error Code: {response.status_code}\n{response.text}')
                return 'error'
        except requests.exceptions.RequestException as e:
            print(f'Request failed: {e}')
            return 'error'