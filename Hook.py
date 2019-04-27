class Hook:
    Hook_Name = ""
    Hook_Sequence_Number = 0
    Boolean_Hook_Status = False
    Hook_Description = ""
    Hook_Association_Number = 0
    hookPath = ""
    def __init__(self,hName,seqNum, status,desc,assocNum,path):
        self.Hook_Name = hName
        self.Hook_Sequence_Number = seqNum
        self.Boolean_Hook_Status = status
        self.Hook_Description = desc
        self.Hook_Association_Number = assocNum
        self.hookPath = path
    

    def increment_association_number(self):
        print("Hello from a function")
        self.Hook_Association_Number = self.Hook_Association_Number + 1
        
    def decrement_association_number(self):
        print("Hello from a function")
        self.Hook_Association_Number =  self.Hook_Association_Number - 1

    def execute(self, packet):
        print("Hello from a function")
        if (self.Boolean_Hook_Status):
            exec(self.hookPath,packet)
            
        