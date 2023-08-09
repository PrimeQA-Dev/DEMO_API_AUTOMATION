import logging
from main_test.Report_Mail import TestReport_Generation, Summary_Table_Formation, Send_Mail


def pytest_unconfigure(config):
    TestReport_Generation()
    Summary_Table_Formation()
    Send_Mail()
    logging.info("finally")




