from Hook import Hook
from HookCollection import HookCollection
from HookCollectionManager import HookCollectionManager
import time

#A main method for testing hook functionality.
def main():


    testHook = Hook("Test",True,"A test hook!",0,"C:/Users/octob/Documents/NTPSProject/Interceptor/testHook.py")

    print(testHook.Hook_Name)
    print(testHook.Hook_Description)

    hooks = []

    hc = HookCollection("testCollection",0,True,"A test hook collection.",hooks)

    hc.addHook(testHook)

    collections = [hc]

    manager = HookCollectionManager(collections,testHook)

    p = "Packet("

    #P.pName = "https Connection"

    print("Calling execute on hook manager...")

    #hc.executeHookSequence(p)
    manager.executeCollection(p)




if __name__ == "__main__": 
    main()