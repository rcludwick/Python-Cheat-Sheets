ayncore
~~~~~~~

Python's asyncore provides an event loop that can handle
transactions from multiple non-blocking sockets.

**Import Syntax**
::
    import asyncore

**__init__ parameters**
::
    asyncore.dispatcher.__init__(self, sock, map)

*sock*: is the socket to be passed in if it exists
already.

*map*: is a dictionary for use when different asyncore
loops are running on different threads.  The same map is
passed into asyncore.loop()

**asyncore.dispatcher.**
Subclass asyncore.dispatcher :: 
    import asyncore
    import socket

    class SampleClass(asyncore.dispatcher):

        def __init__(self):
            self.asyncore.dispatcher.__init__(self)
            self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connect(("example.com",2222))
            self.out_buffer = ''
            self.in_buffer = ''

        def handle_read(self):
            # Do something with data
            data = self.recv(4096)
            self.in_buffer += data

        def handle_write(self):
            #Data must be placed in a buffer somewhere.
            #(In this case out_buffer)
            sent = self.send(self.out_buffer)
            self.out_buffer = self.out_buffer[sent:]

        def readable(self):
            #Test for select() and friends
            return True

        def writeable(self):
            #Test for select(). Must have data to write
            #otherwise select() will trigger
            if self.connected() and len(self.out_buffer) > 0:
                return True
            return False

        def handle_close(self):
            #Flush the buffer
            while self.writeable():
                self.handle_write()
            self.close()


**asyncore.dispatcher_with_send**
This is just like the normal dispatcher, except that the writable() and
handle_write() methods have been already provided.

