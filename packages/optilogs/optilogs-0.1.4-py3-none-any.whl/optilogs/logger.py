import requests
import inspect
from .config import OptilogsConfig

class Optilogs:
    def __init__(self, server_ip: str, server_port: int):
        self.config = OptilogsConfig(server_ip, server_port)

    def log(self, *args):
        message = self._format_message(*args)
        self._send_log(message)

    def logf(self, variable):
        var_name = self._get_variable_name(variable)
        message = f"{var_name} -> {type(variable).__name__} : {repr(variable)}"
        self._send_log(message)

    def _format_message(self, *args):
        try:
            message = " ".join(str(arg) for arg in args)
        except Exception as e:
            message = f"Failed to format log message: {e}"
        return message

    def _get_variable_name(self, var):
        # Inspect the previous frame to find the name of the variable passed to logf
        frame = inspect.currentframe().f_back
        for name, value in frame.f_locals.items():
            if value is var:
                return name
        return "unknown"

    def _send_log(self, message: str):
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

# Exemple d'utilisation
if __name__ == "__main__":
    logs = create_optilogs("127.0.0.1", 5000)
    logs.log("Message de log simple")
    logs.log("Log avec plusieurs arguments:", 123, {"clé": "valeur"})

    mavariable = 'test'
    logs.logf(mavariable)
