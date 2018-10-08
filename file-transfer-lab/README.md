# File Transfer Assignment

The assignment required the student to be able to create a file transfer between the a Client and Server. In order to implement this, first I attempted to use the 'declaration.txt' file in order to send the message over, in which the file was read and as the file was read, the content within the file was encoded and I used the function 'frameSend', and had it sent by 100 bytes at a time, by through a while loop have it read 100 bytes at a time of the file. In order to turn the file into a binary file, I had the file read with 'rb' of which this allowed me to not necessarily use the 'encode' function and immediately just use the file to send to the Server. In the fileServer, I attempted in the recieving the message, and with the use of the frameRecieve function I attempted to recieve this message, of which I attempted using the "forkframedServer" file that was provided to us, as a means to fork and attempt to create a way to be able to handle multiple clients at a time, yet wasn't able to figure out how to implement this idea.

The following are the resources used as references to complete assignment:

* Dr. Freudenthal's Simple-Echo files and code in order to implement all necessary resources that include the socket and the server and client information.
* The following sites:
    * https://docs.python.org/3/tutorial/errors.html - Attempted to use as a reference to know how to implement exceptions for if the connection was lost, if the file was not found, etc.
    * https://docs.python.org/3.4/howto/sockets.html - Site was used as guide, in which I used to understand how to attempt to implement socket programming with python.
    * https://www.bogotobogo.com/python/python_network_programming_server_client.php - Site was used as reference to understand visually how to transfer a file from client to server with python.
    



