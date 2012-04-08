.. header::

    .. class:: heading

        ..class:: centered

            Threading


**Import Syntax**

.. code-block:: python

    import threading

**Wrapping a Function.**
The option *target* points the thread to run the function when started.

.. code-block:: python

    def myfunc(*args, **kwargs):
        pass

    t = threading.Thread(target = myfunc, \
            args = (), kwargs = {} )

    #Invoke the thread
    t.start()

    #Join when finished
    t.join()


**Subclassing threading.Thread**:
Subclassing a thread involves overloading the *run* method which
will then be called by the *start* method.

.. code-block:: python

    class MyThreadClass(threading.Thread):
         
        def run(self):
            pass

    my_thread = MyThreadClass()
    
    #Invoke
    my_thread.start()

    #Join when finished
    my_thread.join()
             
**Daemon Mode**:
Setting daemon mode on a thread will prevent the thread from keeping
the program from exiting.  Any thread in daemon mode that has not exited will
hang preventing the main thread from exiting.

.. code-block:: python

    my_thread = MyThreadClass()

    #set daemon mode
    my_thread.daemon = True

    #Thread now started in daemon mode
    my_thread.start()


