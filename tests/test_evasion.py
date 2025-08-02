# Tests para los módulos de evasión (core/evasion.py y core/evasion_system.py) del framework TTBT1
# Ejecutar con: pytest tests/test_evasion.py

from core.evasion import Evasion
from core.evasion_system import EvasionSystem

class DummyBot:
    def __init__(self):
        self.proxy = None
        self.fingerprint = None

def test_evasion_rotate_fingerprint_and_proxy():
    fps = ["fpA", "fpB"]
    proxies = ["proxy1", "proxy2"]
    evasion = Evasion(fps, proxies)
    for _ in range(5):
        assert evasion.rotate_fingerprint() in fps
        assert evasion.rotate_proxy() in proxies

def test_evasion_empty_lists():
    evasion = Evasion([], [])
    assert evasion.rotate_fingerprint() is None
    assert evasion.rotate_proxy() is None

def test_evasion_system_initialization_and_run():
    """
    Tests that the EvasionSystem can be initialized with a driver
    and that its methods can be called without error.
    """
    class MockDriver:
        pass

    driver = MockDriver()
    system = EvasionSystem(driver)
    assert system.driver is driver

    # Test that the main method runs without error
    try:
        system.evade_detection()
    except Exception as e:
        assert False, f"'evade_detection' raised an exception {e}"