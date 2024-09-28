import rpyc
from rpyc.utils.server import ThreadedServer
import hou

class HoudiniService(rpyc.Service):
    def exposed_get_hou(self):
        return hou

if __name__ == "__main__":
    server = ThreadedServer(HoudiniService, port=18812)
    print("Starting Houdini RPC server on port 18812...")
    server.start()