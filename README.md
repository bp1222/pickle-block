Example
===========
SignalPickler is a block that will pickle the contents of a NIO Signal.  This will typically be used both before a publisher block, and after a subscriber block.  This is due to the fact that the communications system of NIO does not allow strictly pythonic data types for transmission.  It only allows JSON-able data types.  So sending tuples, bytestrings, and objects is not possible.

If your service is to communicate strictly to another NIO Binary running in python, this is a good shorthand to ensure you can submit your python data directly to the other side preserving the data types.

Properties
--------------
None

Dependencies
----------------
None

Commands
----------------
None

Input
-------
PickleBlock: Any set of signals.
UnpickleBlock: A pickled signal.

Output
---------
PickleBlock: A signal that contains one field, the pickled content of the signal.
UnpickleBlock: A signal with the original data.
