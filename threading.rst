Threading
~~~~~~~~~

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
             
            

