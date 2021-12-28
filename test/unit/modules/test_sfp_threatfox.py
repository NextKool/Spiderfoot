# test_sfp_threatfox.py
import pytest
import unittest

from modules.sfp_threatfox import sfp_threatfox
from sflib import SpiderFoot


@pytest.mark.usefixtures
class TestModuleThreatFox(unittest.TestCase):
    """
    Test modules.sfp_threatfox
    """

    def test_opts(self):
        module = sfp_threatfox()
        self.assertEqual(len(module.opts), len(module.optdescs))

    def test_setup(self):
        """
        Test setup(self, sfc, userOpts=dict())
        """
        sf = SpiderFoot(self.default_options)

        module = sfp_threatfox()
        module.setup(sf, dict())

    def test_watchedEvents_should_return_list(self):
        module = sfp_threatfox()
        self.assertIsInstance(module.watchedEvents(), list)

    def test_producedEvents_should_return_list(self):
        module = sfp_threatfox()
        self.assertIsInstance(module.producedEvents(), list)
