import Hook
from Packet import Packet
import time

#A main method for testing hook functionality.
def main():
    testHook = Hook.Hook("Test",1,True,"A test hook!",2,"testHook.py")

    print(testHook.Hook_Name)
    print(testHook.Hook_Description)

    p = Packet("Test_Packet","Current Time")

    #P.pName = "https Connection"

    testHook.execute(p)




if __name__ == "__main__": 
    main()