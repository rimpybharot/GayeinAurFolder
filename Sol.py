from builtins import set
class Folder:
    id=-1;
    confidential = False;
    children = []
    cows = set()
    
    def __init__(self, id1, confidential):
        self.cows = set()
        self.confidential = confidential
        self.children = []
        self.id = id1;
        
    def addCow(self, cow):
        self.cows.add(cow)
    
    def setFolder(self, ID, conf):
        self.id=ID
        self.confidential = conf;
        
        
    def addChild(self, f):
        self.children.append(f)
    


class Sol():

    """this method takes the input and creates the required structure for finding the solution"""    
    def sol(self):
        
        # All folders with ID and Object of Folder class
        folderID = {}
        
        # Read input
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break

        # total cows, complete set
        cows = int(lines[0])
        setOfCows = set()
        for i in range(cows):
            setOfCows.add(i)
            

        m = int((lines[1]).split()[0]) # Line from where info about shared folder starts
        n = int((lines[1]).split()[1]) # Line from where info about conf folder starts
       
        i=2
        shared = m+2 # Line till where info about shared folder is
        conf =   shared + n # Line till where info about conf folder is

        # Get all info about shared folders
        while(i<shared):
            sharedFolder = lines[i].split()
            id = int(sharedFolder[0])
            folderID[id] = Folder(id, False)
            k = 2
            while(k<2+int(sharedFolder[1])):
                cow = int(sharedFolder[k])
                k=k+1
                folderID[id].addCow(cow)
            i = i+1

        # Get all info about conf folders
        while(i<conf):
            sharedFolder = lines[i].split()
            id = int(sharedFolder[0])
            folderID[id] = Folder(id, True)
            k = 2
            while(k<2+int(sharedFolder[1])):
                cow = int(sharedFolder[k])
                k=k+1
                folderID[id].addCow(cow)
            i = i+1

        # Add children
        tree = i+int((lines[i])) # Line till where info about children is
        i=i+1
        while(i<=tree):
            parent = int((lines[i]).split()[0])
            child = int((lines[i]).split()[1])
            folderID[parent].addChild(folderID[child])
            i=i+1
        
        # uncool cow empty set
        uncoolCows = set()
        for folder in folderID.values():
            # check if a folder has children
            if(folder.children!=[]):
                # if yes, then for each check shared or confidential
                for child in folder.children:
                    # if shared , then cows able to access parent folder
                    # should be able to access child folder
                    if(child.confidential==False):
                        child.cows = child.cows | folder.cows

        # for each folder , check if it is leaf, i.e. ha no children
        for folder in folderID.values():
            # if leaf, then compare with cows set
            if(folder.children==[]):
                # if cows not equal to full set cows, then remaining cows are uncool
                uncoolCows = uncoolCows | setOfCows - folder.cows
      
        for uncoolCow in uncoolCows:
            print(uncoolCow)
            


if __name__ == "__main__":
    s = Sol();
    s.sol()
        
        
    
    
