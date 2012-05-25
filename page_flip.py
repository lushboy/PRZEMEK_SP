#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path, sys, time, os

from obci_control.peer.configured_client import ConfiguredClient
from multiplexer.multiplexer_constants import peers, types
from configs import settings, variables_pb2

LOGGER = logger.get_logger("page_flip", "info")

class PageFlip(ConfiguredClient):
    """Turn pages."""
    def __init__(self, addresses, type=peers.PAGE_FLIP):
        super(PageFlip, self).__init__(addresses=addresses,
                                         type=type)
        self.ready()
        

