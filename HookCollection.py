class HookCollection:
    Hook_Collection_Name = ""
    Hook_Collection_Sequence_Number = 0
    Hook_Collection_Status = False
    Hook_Collection_Description = ""
    Hooks = [] #Hooks: List<Hook> 

    def __init__(self,name,seqNum,status,desc):
        self.Hook_Collection_Name = name
        self.Hook_Collection_Sequence_Number = seqNum
        self.Hook_Collection_Status = status
        self.Hook_Collection_Description = desc


        def knowIfHookSequenceIsUnique(self):
            print("A functio")
        def knowIfHookCollectionSequenceIsUnique(self):
            print("A function")
        def searchHooks(self):
            print("A function")
        def deleteHook(self):
            print("A function")

        def execute_hook_sequence(self):
            print("Hello from a function")

        def __add_hook(self): #private
            print("Hello") 

        def __update_hook_sequencing(self): #private
            print("Hello")

        def __update_hook_collection_sequencing(self): #private
            print("Hello")

        def __remove_hook(self): #private
            print("Hello")
