#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:
#     Mateusz Kruszyński <mateusz.kruszynski@gmail.com>
#

from multiplexer.multiplexer_constants import peers, types
from logic import logic_helper
from logic.logic_decision_peer import LogicDecision
from bliss_engine import BlissEngine


from configs import settings, variables_pb2
from logic import logic_logging as logger
LOGGER = logger.get_logger("logic_multiple", "info")

class LogicBliss(LogicDecision, BlissEngine):
    """A class for creating a manifest file with metadata."""
    def __init__(self, addresses):
        LogicDecision.__init__(self, addresses=addresses)
        BlissEngine.__init__(self, self.config.param_values())
        self.ready()
        self._update_letters()
        self._update_images()

    def _run_post_actions(self, p_decision):
        self._update_letters()

if __name__ == "__main__":
    LogicBliss(settings.MULTIPLEXER_ADDRESSES).loop()

