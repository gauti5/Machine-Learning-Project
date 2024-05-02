import os
import sys

class HousingException(Exception):
    def __init__(self, error_message:Exception, error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message #passing error message to the Exception Class....


    @staticmethod
    def get_detailed_error_message(self, error_message:Exception, error_details:sys)->str:
        return error_message
