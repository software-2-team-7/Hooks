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
        for h in self.collection:
            h.executeHookSequence(packet)

    def insertionSort_Hook_Collection_Sequence_Number(self):
        for index in range(1,len(self.collection)):
            currentHookCollection = self.collection[index]
            currentvalue = self.collection[index].Hook_Collection_Sequence_Number
            position = index
            while position>0 and self.collection[position-1].Hook_Collection_Sequence_Number > currentvalue:
                self.collection[position]=self.collection[position-1]
                position = position-1

            self.collection[position]=currentHookCollection
    

