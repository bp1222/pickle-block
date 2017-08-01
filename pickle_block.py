from nio.block.base import Block
from nio.properties import VersionProperty
from nio.signal.base import Signal
from nio.util.discovery import discoverable
import pickle


@discoverable
class PickleBlock(Block):
    version = VersionProperty('1.0.0')

    def process_signals(self, signals):
        pickled = pickle.dumps(signals)

        signal = Signal()
        signal.pickled_data = pickled

        self.notify_signals([signal])
