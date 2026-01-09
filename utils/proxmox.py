from proxmoxer import ProxmoxAPI

class Proxmox(ProxmoxAPI):
    def __init__(self, host=None, backend="https:", service="PVE", **kwargs):
        super().__init__(host, user, password, verify_ssl=True, **kwargs) 