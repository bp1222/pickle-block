from nio.block.base import Block
from nio.properties import VersionProperty
from nio.util.discovery import discoverable
from base64 import b64decode
import pickle


@discoverable
class UnpickleBlock(Block):
    version = VersionProperty('1.0.0')

    def process_signals(self, signals):
        if len(signals) > 1:
            raise RuntimeError("Should only have a single pickled signal")

        if 'pickled_data' not in signals[0]:
            raise RuntimeError(
                "Pickled signal should have the pickled_data field"
            )

        try:
            decoded_data = b64decode(signals[0].pickled_data)
        except TypeError:
            self.logger.exception("Unable to decode pickled_data")

        try:
            signals = pickle.loads(decoded_data)
        except pickle.UnpicklingError:
            self.logger.exception("Pickling based unpickle error")
        except:
            self.logger.exception("Error unpickling data")

        self.notify_signals(signals)
