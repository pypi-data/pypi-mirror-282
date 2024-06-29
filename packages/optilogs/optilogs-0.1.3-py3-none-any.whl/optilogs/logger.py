import requests
from .config import OptilogsConfig

class Optilogs:
    def __init__(self, server_ip: str, server_port: int):
        self.config = OptilogsConfig(server_ip, server_port)

    def log(self, message: str):
        url = self.config.get_server_url()
        payload = {"log": message}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Failed to send log: {e}")

# Factory function for ease of use
def create_optilogs(server_ip: str, server_port: int):
    return Optilogs(server_ip, server_port)
