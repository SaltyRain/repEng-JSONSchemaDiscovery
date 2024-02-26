from user_auth import UserAuthentication

class RequestHeader:
    """Class for managing request headers."""

    @staticmethod
    def get_auth_header():
        """Generates and returns the authorization header."""
        token = UserAuthentication.get_auth_token()
        return {
            "content-type": "application/json",
            "Authorization": f"Bearer {token}"
        }