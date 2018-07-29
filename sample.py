import unittest
import pytest

class BrowserGoogle(unittest.TestCase):
    def browser(self):
        browser_type = pytest.config.option.type
        print(browser_type)
