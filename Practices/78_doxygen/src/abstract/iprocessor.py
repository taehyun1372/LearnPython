from abc import abstractmethod

class IProcessor:
    """! @brief a abstract class for processor
    
    This provides abstract functions that all sub classes need 
    to implement
    """
    def __init__(self, name):
        """! @brief Initialize class
        """
    
    @abstractmethod
    def launch(self, mode) -> bool:
        """! @brief Need to call this to run it properly
        @param mode this is desired operation mode
        @return a boolean indicating if the launch was successfull
        """
        
    