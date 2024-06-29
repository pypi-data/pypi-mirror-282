# Optilogs

Optilogs is a simple logging library that sends logs to a server via HTTP requests.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install optilogs.

```bash
pip install optilogs
```

Example

```bash
from optilogs.logger import Optilogs

# Create an instance of Optilog with the IP and port of your log server
optilogs = Optilogs(server_ip="0.0.0.0", server_port=5050)

# Send a log
optilogs.log("Ceci est un log de test")
```
