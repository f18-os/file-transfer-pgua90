# File Transfer Assignment
Patricia Guajardo


The assignment required the student to be able to create a file transfer between the a Client and Server. In order to implement this, first I attempted to use the 'declaration.txt' file in order to send the message over, in which the file was read and as the file was read, the content within the file was encoded and I used the function 'frameSend', at which in order to prevent any special characters, and had it sent by 100 bytes at a time. In the fileServer, I attempted in the recieving the message, and with the use of the frameRecieve function I attempted to recieve this message, echo that it was recieved and the contents to be displayed within a temporary text file "rcv.txt", of which I was not able to find how to go about and recieve the content or message.



The following are the resources used as references to complete assignment:

* Dr. Freudenthal's Simple-Echo files and code in order to implement all necessary resources that include the socket and the server and client information.
* The following sites:
    * 
    * 
    * 
    * 
* I collaborated with Sebastian Nunez, in which he assisted me the understanding of the sample code that was provided to us as reference, as well as how to send the data at 100 bytes at a time which he helped understand this idea which can be seen in my code at lines 71-78, as well as assisting me in showing me how to replace special characters.



