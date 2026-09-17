from abstract.iprocessor import IProcessor

class Processor(IProcessor):
    """! @brief Implementation class for IProcessor

    
    """
    def __init__(self, name):
        """! @brief This initializes Processor class

        @param name a unique name to identify processor
        """
        super().__init__(self)
        self.name = name

    def launch(self, mode) -> bool:
        """! @brief Need to call this to run it properly
        @param mode this is desired operation mode
        @return a boolean indicating if the launch was successfull
        """
        if self.name:
            return True
        else:
            return False