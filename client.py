import socket
from threading import Thread
from tkinter import *

# nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connected with the server...")

class gui:
    def __init__(self):
        self.window=Tk()
        self.window.withdraw()

        self.login=Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=300)

        self.title=Label(self.login,text="Please log in to continue!",justify="center",font="Helvetica 14 bold")
        self.title.place(relheight=0.15,relx=0.2,rely=0.07)

        self.labelName=Label(self.login,text="Name: ",font="arial 10")
        self.labelName.place(relheight=0.2,relx=0.1,rely=0.2)

        self.entry=Entry(self.login,font="Helvetica 14")
        self.entry.place(relheight=0.12,relx=0.25,rely=0.2,relwidth=0.4)
        self.entry.focus()

        self.button=Button(self.login,text="Continue:",font="Helvetica 14 bold",command=lambda:self.goAhead(self.entry.get()))
        self.button.place(relx=0.4,rely=0.5)

        self.window.mainloop()

    def goAhead(self,name):
        self.login.destroy()
        self.name=name
        rcv=Thread(target=self.receive)
        rcv.start()

    def receive(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                if message == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    print(message)
            except:
                print("An error occured!")
                client.close()
                break
g=gui()

# def write():
#     while True:
#         message = '{}: {}'.format(nickname, input(''))
#         client.send(message.encode('utf-8'))

# receive_thread = Thread(target=receive)
# receive_thread.start()
# write_thread = Thread(target=write)
# write_thread.start()