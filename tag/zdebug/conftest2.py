
import pytest

def read_device_list():
    #return ["172.16.0.144", "172.16.0.248"]
    return ["172.16.0.144","172.16.0.248"]

def pytest_configure(config):
     # read device list if we are on the master
     if not hasattr(config, "slaveinput"):
        config.iplist = read_device_list()

def pytest_configure_node(node):
    # the master for each node fills slaveinput dictionary
    # which pytest-xdist will transfer to the subprocess
    node.slaveinput["ipadr"] = node.config.iplist.pop()

@pytest.fixture(scope="session")
def device(request):
    slaveinput = getattr(request.config, "slaveinput", None)
    if slaveinput is None: # single-process execution
        ipadr = read_device_list()[0]
    else: # running in a subprocess here
        ipadr = slaveinput["ipadr"]
    return Device(ipadr)

class Device:
    def __init__(self, ipadr):
        self.ipadr = ipadr

    def __repr__(self):
        return "<Device ip=%s>" % (self.ipadr)
