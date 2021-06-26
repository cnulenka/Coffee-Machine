import logging

class Logger:
    _logger = None

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def get_logger():
        #Create and configure logger
        logging.basicConfig(filename="Coffee_Machine_Logs.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')
        
        #Creating an object
        Logger._logger=logging.getLogger()
        
        #Setting the threshold of logger to DEBUG
        Logger._logger.setLevel(logging.DEBUG)
        return Logger._logger