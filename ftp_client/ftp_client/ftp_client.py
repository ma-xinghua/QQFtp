import ftplib 
import os,socket 
import threading



class FTPClient: 
    def __init__(self): 
        self.curDir = "/" 
        self.cursize = 0  

    def ListFile(self): 
        self.ftp.dir(self.curDir) 
        pass  

    def Connect(self,host): 
        try: 
            self.ftp = ftplib.FTP(host) 
            self.ftp.encoding = 'utf-8'
        except (socket.error, socket.gaierror) as e: 
            print("Er#ror:cannot reach%s" % (host)) 
            return  
        print("Conneted host:", host)  

    def Login(self,user,password): 
        try: 
            self.ftp.login(user, password) 
            
        except ftplib.error_perm: 
            print("Error: cannot login anonymously") 
            self.ftp.quit() 
            return 
        print("logined as ", user) 
        self.ListFile()  

    def EnterDir(self,dirname): 
        try: 
            #change dir 
            self.curDir = self.curDir+dirname 
            self.ftp.cwd(self.curDir) 
        except ftplib.error_perm: 
            print("Error: cannot CD into %s" % (self.curDir)) 
            self.ftp.quit() 
            return 
        print("Changed into %s folder" % (self.curDir))  

    def DownloadFile(self, filename): 
        try: 
            #local file 
            self.cursize = 0 
            filehandle = open(filename, "wb") 
            #remote file 
            print ("1")
            self.totalsize = os.path.getsize(filename)  
            print ("2")
            #define callback 
            chunkwrite = lambda chunk: self.ChunkWrite(chunk, filehandle)  
            print ("3")
            self.ftp.retrbinary("RETR %s" % (filename), filehandle.write)  
        except ftplib.error_perm:  
            print("Error: cannot read file %s" % (filename)) 
              
        filehandle.close() 
        print("….Download “%s” to Local" % (filename))  

    def UPLoadFile(self, filename): 
        try: 
            #local 
            self.cursize = 0 
            filehandle = open(filename, "rb") 
            self.totalsize = os.path.getsize(filename)  
            #remote 
            pathFormat = filename.split("\\") 
            remotefile = pathFormat[len(pathFormat) - 1]  
            self.ftp.storbinary("STOR %s" % (remotefile),filehandle, 1024,self.ChunkRead)  
        except ftplib.error_perm:  
            print("Error: cannot read file %s" % (remotefile)) 
            os.unlink(remotefile)  
        filehandle.close() 
        print("….UpLoad “%s” to FTP" % (filename))  

    def ChunkWrite(self,chunk, filehandle):  
        # calc process 
        self.cursize = self.cursize + len(chunk) 
        process = self.cursize*100 / self.totalsize 
        print(str(round(process, 3))+"%",end = "\r")  
        #save data to local 
        filehandle.write(chunk)  

    def ChunkRead(self, chunk):  
        #calc process 
        self.cursize = self.cursize + len(chunk) 
        process = self.cursize * 100 / self.totalsize 
        print(str(round(process, 3)) + "%",end="\r")  
        

    def Disconnect(self): 
        try: 
            self.ftp.quit() 
        except (socket.error, socket.gaierror) as e: 
            print(e)

class CustomConsole(threading.Thread): 
    def __init__(self): 
        self.cmd = "" 
        threading.Thread.__init__(self)  

   

    def run(self):  
        print("*********Command Usaged************") 
        print("***conn :Connect to ftp server*****") 
        print("***login:Login ftp server**********") 
        print("***ls:List files and directories***") 
        print("***cd:Change directory*************") 
        print("***put:Upload File to ftp server***") 
        print("***get:Download from ftp server****") 
        print("***quit:disconnect with ftp server*")  

        while(True): 
            cmd = input("Please input command:") 
            if(cmd == "quit"): 
                self.ftp.Disconnect() 
                break  

            if (cmd == "conn"): 
                serverip = input("Please input server ip:") 
                self.ftp = FTPClient() 
                self.ftp.Connect(serverip)  

            if (cmd == "login"): 
                username = input("Please input username:") 
                password = input("Please input password:") 
                self.ftp.Login(username,password)  

            if(cmd == "ls"): 
                files = self.ftp.ListFile()  

            if (cmd == "cd"): 
                files = self.ftp.ListFile() 
                subdir = input("Please input subdir:") 
                self.ftp.EnterDir(subdir)  

            if (cmd == "get"): 
                filename = input("Please input filename:") 
                self.ftp.DownloadFile(filename)  

            if (cmd == "put"): 
                filename = input("Please input filename:") 
                self.ftp.UPLoadFile(filename)




if __name__ == '__main__': 

    c = CustomConsole() 
    c.start()
    c.join()
    