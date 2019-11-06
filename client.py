import socket

def menu():
    print("**********Welcome to ATM********")
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
    print(s.recv(1024).decode())
    if userchoice == '1' or userchoice == '2':
        userchoice = input()
        msg = str.encode(str(userchoice), 'utf-8')
        s.send(msg)
        print(s.recv(1024).decode())
    elif userchoice == '4':
        exit()
s.close