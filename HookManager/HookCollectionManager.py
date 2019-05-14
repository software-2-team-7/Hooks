class HookCollectionManager(object):
    collection = []
    hooks = []

    def __init__(self,collect,hook):
        self.collection = collect 
        self.hooks = hook
    
    def executeHook(self,name,packet):

        for h in self.hooks:
                h.execute(packet)
    
    def executeCollection(self,packet):
        newPacket = packet
        for h in self.collection:
            newPacket = h.executeHookSequence(newPacket)
        return newPacket
        
    def deleteCollection(self):
        print("Collection deleted.")
    
    def deleteHook(self):
        print("Hello!")
    
    def addHookCollection(self,c):
        self.collection.append(c)
    
    def addHook(self,h):
        self.hooks.append(h)
    
    def getCollections(self):
        return self.collection
    
    def getHooks(self):
        return self.hooks


