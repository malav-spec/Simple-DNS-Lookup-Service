README 

Project 1

Name: Malav Doshi (md1378) | Abhay Saxena ()

1. Flow of the program

The flow of the program starts with the client connecting to the root server. After connecting to the root server, it sends the hostname 
line by line from the PROJI-HNS.txt file. The root server receives the data from the client. It first converts the data to lower case since
the lookup is case-insensitive. Then it sends the data to 'checkHostInDict' function in order to check if the data is present in the DNS 
table or not. If present, data is sent to 'toString()' method to convert the data to [Hostname IP A] form. If not present, Top server host
name is looked up and returned to the client in the format [TShostname - NS]. 

Now back in client, if the data was present it simply writes the data to the 'RESOLVED.txt' file and moves onto the next line. If the data is 
not present in the root server the client connects to the Top-Server. Connection to the top-server is only done once. Once client is connected 
to Top-server it sends the query to it. In top-server data is received and converted to lower-case. Then again it is checked in the DNS table. If
the data is present it returnsin format [Hostname IP A], else in the format [Hostname - Error:HOST NOT FOUND] 

Data storage in ts.py and rs.py: 
	Data is stored in similar manner in both the servers. It is stored by calling 'fileToDict()' function. This function converts the text line by line 
into a dict. The key in the dict is the hostname and the value is a list of IP address and the flag.

Dict = {key = hostname : value = [IP, Flag]} 

2. There are no known problems in the program. Everythin is working fine. 

3. The main problem we faced for this project was connecting two sockets from the client. The connection to root server was easy. But connection to the top-server
was tricky because the conenction got closed after 1 lookup in ts.py and couldn't connect again. But this was rectified. 

4. We learned exactly how the DNS lookup service works. Also we learned how to use dicts and lists efficiently in python. 