#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation    https://github.com/cyborg-ai-git | 
#========================================================================================================================================

from evo_framework import *
from evo_package_admin.entity import *
from evo_framework.core.evo_core_api.entity.EApiConfig import EApiConfig

#<
#OTHER IMPORTS ...
#>
# ---------------------------------------------------------------------------------------------------------------------------------------
# UAdminApi
# ---------------------------------------------------------------------------------------------------------------------------------------
"""UAdminApi
"""
class UAdminApi():
    __instance = None
# ---------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):   
        if UAdminApi.__instance != None:
            raise Exception("ERROR:SINGLETON")
        else:
            super().__init__()
            UAdminApi.__instance = self
            self.currentPath = os.path.dirname(os.path.abspath(__file__))
            
# ---------------------------------------------------------------------------------------------------------------------------------------
    """getInstance Singleton

    Raises:
        Exception:  api exception

    Returns:
        _type_: UAdminApi instance
    """
    @staticmethod
    def getInstance():
        if UAdminApi.__instance is None:
            uObject = UAdminApi()  
            uObject.doInit()  
        return UAdminApi.__instance
# ---------------------------------------------------------------------------------------------------------------------------------------
    """doInit

    Raises:
        Exception: api exception

    Returns:

    """   
    def doInit(self):   
        try:
#<
            #INIT ...
            pass
#>   
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnSetEApiConfig(self, eAdminInput:EAdminInput) -> EApiConfig :
        try:
            if eAdminInput is None:
                raise Exception("ERROR_REQUIRED|eAdminInput|")

#<        
            #Add other check
            '''
            if eAdminInput. is None:
                raise Exception("ERROR_REQUIRED|eAdminInput.|")
            '''
   
            eApiConfig = EApiConfig()
            eApiConfig.doGenerateID()
            
            
            yield eApiConfig
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnGetEApiConfig(self, eAdminQuery:EAdminQuery) -> EApiConfig :
        try:
            if eAdminQuery is None:
                raise Exception("ERROR_REQUIRED|eAdminQuery|")

#<        
            #Add other check
            '''
            if eAdminQuery. is None:
                raise Exception("ERROR_REQUIRED|eAdminQuery.|")
            '''
   
            eApiConfig = CApiFlow.getInstance().eApiConfig
           
            
            
            yield eApiConfig
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnQueryAutomation(self, eAdminQuery:EAdminQuery) -> EApiFile :
        try:
            if eAdminQuery is None:
                raise Exception("ERROR_REQUIRED|eAdminQuery|")

#<        
            #Add other check
            '''
            if eAdminQuery. is None:
                raise Exception("ERROR_REQUIRED|eAdminQuery.|")
            '''
   
            eApiFile = EApiFile()
            eApiFile.doGenerateID()
            
            
            yield eApiFile
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------

#<
#OTHER METHODS ...
#>
# ---------------------------------------------------------------------------------------------------------------------------------------
