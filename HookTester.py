from Hook import Hook
from HookCollection import HookCollection
from HookCollectionManager import HookCollectionManager
import time

#A main method for testing hook functionality.
def main():

    #create a hook called 'testHook'with the name 'Test'. Its sequence is not set automatically.
    testHook = Hook("Test",True,"A test hook!",0,"C:/Users/octob/Documents/NTPSProject/Interceptor/testHook.py")

    #Printing the name and description of the hook.
    print(testHook.Hook_Name)
    print(testHook.Hook_Description)

    #create an empty list of hooks to add to the collection
    hooks = []

    #create a hook collection and put the hooks list in it
    hc = HookCollection("testCollection",0,True,"A test hook collection.",hooks)

    #add the testHook to the hc hook list
    hc.addHook(testHook)

    #create a list of HookCollections; right now, there's only one hook collection in it
    collections = [hc]

    #create HookCollectionManager called 'manager' and add 'collections' to it.
    #remember that managers also store hooks without assigning them to collections; 
    #we add a copy of the testHook to illustrate this.
    manager = HookCollectionManager(collections,testHook)

    #A test packet. Right now, it's just a string; expect it to be a raw packet later.
    p = "Packet("

    print("Calling execute on hook manager...")

    #hc.executeHookSequence(p)
    manager.executeCollection(p) #executes a hook collection


if __name__ == "__main__": 
    main()