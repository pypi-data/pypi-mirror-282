class OptilogsConfig:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port

    def get_server_url(self):
        return f"http://{self.server_ip}:{self.server_port}/log"
