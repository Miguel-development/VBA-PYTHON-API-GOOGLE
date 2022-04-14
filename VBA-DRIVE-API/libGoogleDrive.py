# import our libraries
import pythoncom
import win32com.client
#C:\Users\Jorge\AppData\Roaming\Python\Python39\site-packages\pywin32_system32
#we have to copy pythoncom39.py and pythonwtypes.py to
#C:\Users\Jorge\AppData\Roaming\Python\Python39\site-packages\win32\lib
from urllib.request import Request, urlopen
from index import getUploadFile,getCLIENT__SECRET_FILE_BASE,getTOKEN_FILE_BASE
#pip install pywin32

class GoogleDriveObjectLibrary:

    # This will create a GUID to register it with Windows, it is unique.
    _reg_clsid_ = pythoncom.CreateGuid()
    # Register the object as an EXE file, the alternative is an DLL file (INPROC_SERVER)
    _reg_clsctx_ = pythoncom.CLSCTX_LOCAL_SERVER
    # the program ID, this is the name of the object library that users will use to create the object.
    _reg_progid_ = "GoogleDrive.APILibrary"
    # this is a description of our object library.
    _reg_desc_ = "This is our Google Sheets object library."
    # a list of strings that indicate the public methods for the object. If they aren't listed they are conisdered private.
    _public_methods_ = ['setUploadFile','setCLIENT__SECRET_FILE','setTOKEN_FILE']
    
    def setCLIENT__SECRET_FILE(self,pathClientSecret):
        getCLIENT__SECRET_FILE_BASE(pathClientSecret)

    def setTOKEN_FILE(self,pathToken):
        getTOKEN_FILE_BASE(pathToken)
        
    def setUploadFile(self):
        getUploadFile()



if __name__=='__main__':
    
    print ("Registering COM server...")
    import win32com.server.register
    win32com.server.register.UseCommandLine(GoogleDriveObjectLibrary)