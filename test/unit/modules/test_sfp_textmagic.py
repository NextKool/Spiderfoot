# test_sfp_textmagic.py
import pytest
import unittest

from modules.sfp_textmagic import sfp_textmagic
from sflib import SpiderFoot
from spiderfoot import SpiderFootEvent, SpiderFootTarget


@pytest.mark.usefixtures
class TestModuletextmagic(unittest.TestCase):
    """
    Test modules.sfp_textmagic
    """

    def test_opts(self):
        module = sfp_textmagic()
        self.assertEqual(len(module.opts), len(module.optdescs))

    def test_setup(self):
        """
        Test setup(self, sfc, userOpts=dict())
        """
        sf = SpiderFoot(self.default_options)

        module = sfp_textmagic()
        module.setup(sf, dict())

    def test_watchedEvents_should_return_list(self):
        module = sfp_textmagic()
        self.assertIsInstance(module.watchedEvents(), list)

    def test_producedEvents_should_return_list(self):
        module = sfp_textmagic()
        self.assertIsInstance(module.producedEvents(), list)

    def test_handleEvent_no_api_key_should_set_errorState(self):
        """
        Test handleEvent(self, event)
        """
        sf = SpiderFoot(self.default_options)

        module = sfp_textmagic()
        module.setup(sf, dict())

        target_value = 'example target value'
        target_type = 'PHONE_NUMBER'
        target = SpiderFootTarget(target_value, target_type)
        module.setTarget(target)

        event_type = 'ROOT'
        event_data = 'example data'
        event_module = ''
        source_event = ''
        evt = SpiderFootEvent(event_type, event_data, event_module, source_event)

        result = module.handleEvent(evt)

        self.assertIsNone(result)
        self.assertTrue(module.errorState)
