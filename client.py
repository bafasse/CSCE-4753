# Import socket module 
import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 12345                
  
# connect to the server on local computer 
temp =  0
while temp < 5:
    s.connect(('127.0.0.1', port)) 
    
    # receive data from the server 
    print (s.recv(1024) )
    # close the connection 
    temp = temp + 1
       
s.close()