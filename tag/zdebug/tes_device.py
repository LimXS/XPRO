import time

def test_device1(device):
    time.sleep(1)  # simulate long test time

    assert 0, device


def test_device2(device):
    time.sleep(1)  # simulate long test time

    assert 0, device

def test_device3(device):
    time.sleep(1)  # simulate long test time

    assert 0, device