import sys
from os import path
import unittest

sys.path.append("./")

from src.auto_switch_providers.auto_switch_providers import AutoSwitchProviders

TEMPLATE_CONFIG = {
    "googleapi": {"http_service": {"params": {"key": ""}}},
    "proxiesapi": {"http_service": {"params": {"auth_key": ""}}},
}

CACHE_CONFIG = {"host": "127.0.0.1", "password": "", "port": 6379}


class TestSample(unittest.TestCase):
    def test_process(self):
        response = AutoSwitchProviders(
            template_dir=f"{path.dirname(__file__)}/templates",
            config=TEMPLATE_CONFIG,
        ).process({})
        self.assertEqual(response, {})


if __name__ == "__main__":
    unittest.main()
