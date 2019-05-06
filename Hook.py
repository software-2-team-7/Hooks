import os
import subprocess

#Class definition for Hooks
class Hook:
    Hook_Name = "" #String
    Hook_Sequence_Number = 0 #Integer
    Boolean_Hook_Status = False #Boolean
    Hook_Description = "" #String
    Hook_Association_Number = 0 #Int
    hookPath = "" #String

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

    def decrement_sequence_number(self):
        print("Hello from a function")
        self.Hook_Sequence_Number =  self.Hook_Sequence_Number - 1

    def execute(self, packet):
        print("Executing hook " + self.hookPath + "...")
        if (self.Boolean_Hook_Status):
            os.system("python " + self.hookPath + " " + packet.toText())

            
        