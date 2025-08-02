# Tests para los módulos principales en core/ del framework TTBT1
# Ejecutar con: pytest tests/test_core.py

import os
import json
import tempfile
from core.account_manager import CoreAccountManager
from core.bot import TikTokBot
from core.bot_engine import BotEngine
from core.config_loader import ConfigLoader

def test_core_account_manager_functionality():
    """
    Tests adding accounts and retrieving them with CoreAccountManager.
    """
    manager = CoreAccountManager()
    assert manager.get_next_account() is None  # Test empty manager

    manager.add_account("user1@test.com", "pass1")
    manager.add_account("user2@test.com", "pass2")

    account1 = manager.get_next_account()
    assert account1["email"] == "user1@test.com"
    # Note: The current get_next_account always returns the first one.
    # A more advanced implementation might rotate accounts.
    account2 = manager.get_next_account()
    assert account2["email"] == "user1@test.com"


def test_tiktok_bot_initialization(monkeypatch):
    """
    Tests the basic initialization of the TikTokBot.
    Mocks external dependencies like the webdriver.
    """
    # Mock selenium webdriver to avoid actual browser interaction
    class MockWebDriver:
        def __init__(self, options=None):
            pass
        def get(self, url):
            pass

    monkeypatch.setattr("core.bot.webdriver.Chrome", MockWebDriver)

    # Mock other managers to isolate the bot's own logic
    monkeypatch.setattr("core.bot.CoreAccountManager", CoreAccountManager)
    monkeypatch.setattr("core.bot.HumanBehaviorSimulator", lambda driver: None)

    bot = TikTokBot()
    assert bot.driver is not None
    assert isinstance(bot.account_manager, CoreAccountManager)
    assert bot.behavior is None # As it was mocked

def test_bot_engine_initialization():
    """
    Tests that the BotEngine can be initialized with a bot
    and its run method can be called.
    """
    class MockBot:
        def __init__(self):
            self.has_run = False
        def run_session(self):
            self.has_run = True

    bot = MockBot()
    engine = BotEngine(bot)
    engine.run()
    assert bot.has_run is True

def test_config_loader_json_and_yaml():
    data = {"hello": "world"}
    with tempfile.NamedTemporaryFile("w+", suffix=".json", delete=False) as jf:
        json.dump(data, jf)
        jf.seek(0)
        loaded = ConfigLoader.load(jf.name)
        assert loaded == data
    os.remove(jf.name)
    try:
        import yaml
        with tempfile.NamedTemporaryFile("w+", suffix=".yml", delete=False) as yf:
            yaml.safe_dump(data, yf)
            yf.seek(0)
            loaded = ConfigLoader.load(yf.name)
            assert loaded == data
        os.remove(yf.name)
    except ImportError:
        pass