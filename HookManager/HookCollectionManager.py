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


