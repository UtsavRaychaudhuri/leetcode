class FileSystem:

    def __init__(self):
        self.path={}
        self.root=self.path
        

    def ls(self, path) :
        path=path.split("/")[1:]
        mempath=self.root
        res=[]
        if path==[""]:
            return sorted(list(mempath))
        for i in path:
            mempath=mempath[i]
        if "content" in mempath:
            return path[-1]
        res=sorted(list(mempath))
        return res
    
    def mkdir(self, path: str) -> None:
        path=path.split("/")[1:]
        mem_path=self.root
        for i in path:
            if i in mem_path:
                mem_path=mem_path[i]
            else:
                mem_path[i]={}
                mem_path=mem_path[i]

    def addContentToFile(self, filePath: str, content: str) -> None:
        mempath=self.root
        fp=filePath.split("/")[1:]
        for i in fp:
            if i in mempath:
                mempath=mempath[i]
            else:
                mempath[i]={}
                mempath=mempath[i]
        if "content" in mempath:
            mempath["content"]+=content
        else:
            mempath["content"]=content
            

    def readContentFromFile(self, filePath: str) -> str:
        mempath=self.root
        fp=filePath.split("/")[1:]
        for i in fp:
            mempath=mempath[i]
        return mempath["content"]


fs=FileSystem()
print(fs.mkdir("/m"))
print(fs.ls("/m"))
print(fs.mkdir("/w"))
print(fs.ls("/"))
print(fs.ls("/w"))
print(fs.ls("/"))
print(fs.addContentToFile("/dycete","emer"))
print(fs.ls("/w"))
print(fs.ls("/"))
print(fs.ls("/dycete"))