from Hook import Hook
from HookCollection import HookCollection
from Packet import Packet
import time

#A main method for testing hook functionality.
def main():
    testHook = Hook("Test",1,True,"A test hook!",2,"C:/Users/octob/Documents/NTPSProject/Hooks/testHook.py")

    print(testHook.Hook_Name)
    print(testHook.Hook_Description)

    hooks = {testHook}

    hc = HookCollection("testCollection",0,True,"A test hook collection.",hooks)

  

    hc.addHook(testHook)

    p = Packet("Test_Packet","Current Time")

    #P.pName = "https Connection"

    print("Calling execute on hook collection...")

    hc.executeHookSequence(p)




if __name__ == "__main__": 
    main()