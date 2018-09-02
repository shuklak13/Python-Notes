https://docs.python.org/3/reference/datamodel.html

* number.Number
    * numbers.Integral
        * Integers (`int`)
            * Python 2: 32-bit or 64-bit, dependening on the Python build
            * Python 3: unlimited size, subject only the the available memory
        * Boolean (`bool`)
            * True or False
    * numbers.Real (`float`)
        * dependent on underlying machine architecture
* Sequences
    * `len()`, indexing, splicing (`a[i:j]`), iterating
    * Immutable
        * String
        * Tuple
        * Bytes
            * Construct from ints with `bytes(10)` or from ASCII chracters with `b"abc"` (Python 3 only)
            * each item in the sequence is a byte (an int between 0 and 256)
    * Mutable
        * Lists
        * Byte Array
            * Construct with `bytearray(10)`
            * same as Bytes except mutable
* Sets
    * Mutable `set()`
    * Immutable `frozenset()`
* Dictionaries `dict()`
* Callables
    * User-Defined Functions
    * Built-In Functions
        * wrappers around C functions
    * Classes
        * act as factories for themselves
    * Instance Method
        * combines a class, class instance, and a callable (usually a user-defined function)
    * Generator Function
        * a function that uses `yield()`
        * returns an iterator object; get the next value via `iterator.__next__()`
* Modules
* Classes
* Class Instances
* I/O
    * File Objects
        * `sys.stdin`, `sys.stdout`, and `sys.stderr` are initialized by default