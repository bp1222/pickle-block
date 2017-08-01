from nio.block.base import Block
from nio.properties import VersionProperty
from nio.util.discovery import discoverable
import pickle


@discoverable
class UnpickleBlock(Block):
    version = VersionProperty('1.0.0')

    def process_signals(self, signals):
        if len(signals) > 1:
            raise RuntimeError("Should only have a single pickled signal")

        signals = pickle.loads(signals[0].pickled_data)

        self.notify_signals(signals)
