Context Managers
~~~~~~~~~~~~~~~~

*Context Managers* are python classes that are used in conjunction with
the python ``with`` statement.  They are used for managing resources
within a code block guaranteeing that if an ``__enter__()`` method is called,
an ``__exit__()`` method will be called at the exit of the code block, even
if an exception had occured during the code block.

**Example**  The following code shows how to use the threading.Lock() with
and without the ``with`` statement.

.. code-block:: python

    import threading
    lock = threading.Lock()

    #Without context handling:
    lock.acquire()
    do_something()  # <-- An unhandled exception here...
    lock.release()  # <-- ... prevents the release here.

    #Using Context Handler
    with lock:
        # Once in this block, the lock will
        # always be released even if do_something()
        # raises any exception
        do_something()  


Context managers are used to guarantee that state will always
be handled without the details being known by the particular
code block that uses it.  This allows for cleaner code and 
guarantees that an end state will occur once execution leaves
the code block.

**__enter__() method**  The ``__enter__()`` method of a class
is called upon the invocation of the ``with`` statement.  

**__exit__() method**  The ``__exit__()`` method of a class
is called at the end of the code block wrapped by the ``with``
statement.

