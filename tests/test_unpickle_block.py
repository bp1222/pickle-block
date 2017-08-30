from base64 import b64encode
import pickle

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..unpickle_block import UnpickleBlock


class TestExample(NIOBlockTestCase):

    def test_process_signals(self):
        """Signals pass through block unmodified."""
        blk = UnpickleBlock()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal({
                'pickled_data': b64encode(
                    pickle.dumps([Signal({"hello": "n.io"})])
                )
        })])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
            {"hello": "n.io"}
        )
