import pickle
from base64 import b64encode

from nio.block.base import Block
from nio.properties import VersionProperty
from nio.signal.base import Signal


class Pickle(Block):
    version = VersionProperty("1.0.1")

    def process_signals(self, signals):
        try:
            pickled = pickle.dumps(signals)
        except pickle.PicklingError:
            self.logger.exception("Pickling based pickle error")
        except:
            self.logger.exception("Error pickling signals")

        signal = Signal()

        try:
            signal.pickled_data = b64encode(pickled)
        except TypeError:
            self.logger.exception("Unable to encode pickled signals")

        self.notify_signals([signal])
