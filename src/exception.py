import sys
import logging

def error_msg_details(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    fileName = exc_tb.tb_frame.f_code.co_filename
    error_msg_details = "Error occurred in Python script name [{0}] in line number [{1}]. [{2}]".format(fileName,
                                                                                                        exc_tb.tb_lineno,
                                                                                                        str(error))
    return error_msg_details

class CustomException (Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_msg_details(error_message, error_detail = error_detail)



if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e, sys)