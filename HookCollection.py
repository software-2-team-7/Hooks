class HookCollection(object):
    Hook_Collection_Name = ""
    Hook_Collection_Sequence_Number = 0
    Hook_Collection_Status = False
    Hook_Collection_Description = ""
    Hooks = [] #Hooks: List<Hook> 

    def __init__(self,name,seqNum,status,desc,h):
        self.Hook_Collection_Name = name
        self.Hook_Collection_Sequence_Number = seqNum
        self.Hook_Collection_Status = status
        self.Hook_Collection_Description = desc
        self.Hooks = h


    def knowIfHookSequenceIsUnique(self):
        print("A function")

    def knowIfHookCollectionSequenceIsUnique(self):
        print("A function")

    def searchHooks(self):
        print("A function")

    def executeHookSequence(self,packet):
        if (self.Hook_Collection_Status):
            newPacket = ""
            for h in self.Hooks:
                newPacket = h.execute(packet)
        return newPacket



        
            

    def addHook(self,h): #private
        self.Hooks.append(h)

    def updateHookSequencing(self): #private
        print("Hello")

    def updateCollectionSequencing(self): #private
        print("Hello")

    def removeHook(self): #private
        print("Hello")
