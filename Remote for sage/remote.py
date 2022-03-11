import socket
# Since pwn repo can't be installed successfully in sage on Windows OS ,
# I implement a simple class : `remote` for nc interaction in CTF challenges
# By tl2cents

class remote():
    
    def __init__(self,addr,port):
        assert type(addr)==str
        self.io=socket.socket()
        self.io.connect((addr,int(port)))
        
    def recvline(self):
        # \n recived and not in data
        x = self.io.recv(1)  
        data = b''
        while x != b'\n':
            data += x
            x = self.io.recv(1)
        return data
    
    def sendline(self, data):
        if type(data)==str:
            data=data.encode()
        self.send(data+b'\n')
        
    def send(self,data):
        if type(data)==str:
            data=data.encode()
        self.io.send(data)
    
    def recv(self,nbyte):
        return self.io.recv(nbyte)
        
    def recvuntil(self,prefix=b""):
        # timeout not implemented !!!
        # Be careful
        if type(prefix)==str:
            prefix=prefix.encode()
        compare=b""
        L=len(prefix)
        counts=0
        while compare!=prefix:
            x=self.io.recv(1)
            if len(compare)<L:
                compare+=x
            else:
                compare=compare[1:]+x
            counts+=1
        
    def recvafter(self,prefix,nbyte):
        self.recvuntil(prefix)
        return self.recv(nbyte)
    
    def sendafter(self,prefix,data):
        self.recvuntil(prefix)
        self.send(data)
        
    def sendlineafter(self,prefix,data):
        self.recvuntil(prefix)
        self.sendline(data)
        
    def recvlineafter(self,prefix):
        self.recvuntil(prefix)
        return self.recvline()
            
    def time_out(self):
        raise TimeoutError("Time out error")
    

def test():
    addr="xxx.xxx.xxx.xxx"
    port=1234
    io=remote(addr,port)
    io.recvuntil("your prefix")