import socket

def Main():
        host = '127.0.0.1' #client will search for this address
        port = 5000 #client connects to this port to receive/send data

        s = socket.socket()#(socket.AF_INET, socket.SOCK_STREAM) #create a new CLIENT socket object
        s.connect((host, port)) #connect to server and port which server is on

        # 'socket 123345nfjkw345 SECRET'
        message = raw_input(">>") #have user input some message to be sent to server as bytes of data
        while message != 'q': #while loop to have user continuosly enter data if necessary
                s.send(message) #sent out the message to server
                data = s.recv(2048) #receive any data sent back from server
                print ("Received from server: " + data)
                message = raw_input(">>")
        print("Connection closing...")
        s.close() #close the connection

if __name__ == '__main__':
        Main()
