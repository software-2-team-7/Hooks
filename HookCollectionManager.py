class HookCollectionManager:
    collection = []
    hooks = []
    def __init__(self,collect,hook):
        self.collection = collect 
        self.hooks = hook
    
    def executeHook(self,name):

        for h in self.hooks:
            if h.Hook_Name == name:
                h.execute()
    

