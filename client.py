import socket

def menu():
    print("**********Welcome to XYZ ATM********")
    print("Press 1 for Deposit.")
    print("Press 2 for Withdrawal")
    print("Press 3 for Account Balance")
    print("Press 4 to Quit")
host = socket.gethostname()
port = 64000
s = socket.socket()

s.connect((host, port))

while True:
    menu()
    print("What would you like to do: ")
    userchoice = input()
    msg = str.encode(str(userchoice), 'utf-8')
    s.send(msg)
    print(s.recv(1024))
    userchoice = input()
    msg = str.encode(str(userchoice), 'utf-8')
    s.send(msg)
    print(s.recv(1024))
s.close

# s = socket.socket()          
  
# port = 12345                
  
# temp =  0
# while temp < 5:
#     s.connect(('127.0.0.1', port)) 
#     print (s.recv(1024) )
#     temp = temp + 1
       
# s.close()