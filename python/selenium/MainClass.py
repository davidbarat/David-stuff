import unittest
from basic_test_SAB import SabProcessCenter
from basic_test_SAB import SabMireTest
from basic_test_SAB import SabSDE
from basic_test_SAB import SabX3S
from basic_test_SAB import SabVerification
import os
import sys
import HTMLTestRunner
import yaml
import pycron

__author__ = 'Cb1en'

SabProcessCenter.env = sys.argv.pop()

while True:
    if pycron.is_now('*/15 8-19 * * 1-5'):
        if __name__ == "__main__":

            SabX3S.env = SabProcessCenter.env
            SabMireTest.env = SabProcessCenter.env
            SabVerification.env = SabProcessCenter.env
            SabSDE.env = SabProcessCenter.env

            with open("c:\David\selenium\config.yml", 'r') as ymlfile:
                SabSDE.cfg = yaml.load(ymlfile)

            with open("c:\David\selenium\config.yml", 'r') as ymlfile:
                SabProcessCenter.cfg = yaml.load(ymlfile)

            with open("c:\David\selenium\config.yml", 'r') as ymlfile:
                SabX3S.cfg = yaml.load(ymlfile)

            with open("c:\David\selenium\config.yml", 'r') as ymlfile:
                SabMireTest.cfg = yaml.load(ymlfile)

            with open("c:\David\selenium\config.yml", 'r') as ymlfile:
                SabVerification.cfg = yaml.load(ymlfile)

            dir = os.getcwd()

            sabprocesscenter = unittest.TestLoader().\
                loadTestsFromTestCase(SabProcessCenter)

            sabx3s = unittest.TestLoader().loadTestsFromTestCase(SabX3S)
            sabsde = unittest.TestLoader().loadTestsFromTestCase(SabSDE)

            sabverification = unittest.TestLoader().\
                loadTestsFromTestCase(SabVerification)
            sabmiretest = unittest.TestLoader().\
                loadTestsFromTestCase(SabMireTest)

            test_suite = unittest.TestSuite(
                [sabprocesscenter,
                 sabx3s,
                 sabsde,
                 sabverification])

            outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")

            title_html = 'SAB Test Report ' + SabProcessCenter.env

            runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title=title_html,
                description='Basic SAB Tests')

            # run the suite using HTMLTestRunner html output
            # runner.run(test_suite)
            # run TestRunner direct cmd output
            unittest.TextTestRunner(verbosity=2).run(test_suite)
