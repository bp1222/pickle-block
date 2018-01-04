Pickle
======
The Pickle block will [pickle](https://docs.python.org/3/library/pickle.html) the contents of a nio Signal.  This block will typically be used before a publisher block, combined with the Unpickle block after a subscriber block.  This is due to the fact that the communications system of nio does not allow strictly pythonic data types for transmission.  It only allows JSON-able data types.  So sending tuples, bytestrings, and objects is not possible. If your service is to communicate strictly to another nio Binary running in python, this is a good shorthand to ensure you can submit your python data directly to the other side while preserving the data types.

Properties
----------
None

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: A pickled signal.

Commands
--------
None

Unpickle
========
The un-pickle version of the [Pickle](https://blocks.n.io/Pickle) block.

Properties
----------
None

Inputs
------
- **default**: A pickled signal.

Outputs
-------
- **default**: An un-pickled signal of the input signal.

Commands
--------
None

