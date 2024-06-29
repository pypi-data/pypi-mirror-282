import requests
from .config import OptilogConfig

class Optilog:
    def __init__(self, server_ip: str, server_port: int):
        self.config = OptilogConfig(server_ip, server_port)

    def log(self, message: str):
        url = self.config.get_server_url()
        payload = {"log": message}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Failed to send log: {e}")

# Factory function for ease of use
def create_optilog(server_ip: str, server_port: int):
    return Optilog(server_ip, server_port)
