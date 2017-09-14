Pickle
======
Pickle is a block that will pickle the contents of a nio Signal.  This block will typically be used both before a publisher block, and the Unpickle block after a subscriber block.  This is due to the fact that the communications system of nio does not allow strictly pythonic data types for transmission.  It only allows JSON-able data types.  So sending tuples, bytestrings, and objects is not possible. If your service is to communicate strictly to another nio Binary running in python, this is a good shorthand to ensure you can submit your python data directly to the other side preserving the data types.

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

Dependencies
------------
None

Unpickle
========
The un-pickle version of the Pickle block.

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

Dependencies
------------
None
