# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         sfp_ethereum
# Purpose:      SpiderFoot plug-in for scanning retrieved content by other
#               modules (such as sfp_spider) and identifying ethereum addresses.
#
# Author:      Steve Micallef <steve@binarypool.com>
#
# Created:     03/09/2018
# Copyright:   (c) Steve Micallef 2018
# Licence:     GPL
# -------------------------------------------------------------------------------

import re

from spiderfoot import SpiderFootEvent, SpiderFootPlugin


class sfp_ethereum(SpiderFootPlugin):

    meta = {
        'name': "Ethereum Address Extractor",
        'summary': "Identify ethereum addresses in scraped webpages.",
        'flags': [],
        'useCases': ["Footprint", "Investigate", "Passive"],
        'categories': ["Content Analysis"]
    }

    # Default options
    opts = {}
    optdescs = {}

    results = None

    def setup(self, sfc, userOpts=dict()):
        self.sf = sfc
        self.results = self.tempStorage()

        for opt in list(userOpts.keys()):
            self.opts[opt] = userOpts[opt]

    # What events is this module interested in for input
    def watchedEvents(self):
        return ["TARGET_WEB_CONTENT"]

    # What events this module produces
    # This is to support the end user in selecting modules based on events
    # produced.
    def producedEvents(self):
        return ["ETHEREUM_ADDRESS"]

    # Handle events sent to this module
    def handleEvent(self, event):
        eventName = event.eventType
        srcModuleName = event.module
        eventData = event.data
        sourceData = self.sf.hashstring(eventData)

        if sourceData in self.results:
            return

        self.results[sourceData] = True

        self.debug(f"Received event, {eventName}, from {srcModuleName}")

        # thanks to https://stackoverflow.com/questions/21683680/regex-to-match-ethereum-addresses
        matches = re.findall(r"[\s:=\>](0x[a-fA-F0-9]{40})", eventData)
        for m in matches:
            self.debug("Ethereum address match: " + m)
            evt = SpiderFootEvent("ETHEREUM_ADDRESS", m, self.__name__, event)
            self.notifyListeners(evt)

# End of sfp_ethereum class
