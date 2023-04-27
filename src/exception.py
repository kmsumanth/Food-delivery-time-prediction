import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename

    error_message="Error occured in python script [{0}] lineno [{1}] error [{2}]".format(filename,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error,error_detail:sys):
        super().__init__(error)
        self.error_message=error_message_detail(error,error_detail)

    def __str(self):
        return self.error_message