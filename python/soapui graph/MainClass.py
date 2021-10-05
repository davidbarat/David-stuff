import os
import sys
import HTMLTestRunner
import yaml
import pycron

__author__ = 'Cb1en'

while True:
    path_log = 'C:\\David\\soapui\\'
    liste_fic = [
        path_log + 'logs\\getAllClientData.csv',
        path_log + 'logs\\Perso.csv',
        path_log + 'logs\\getListofCusto.csv',
        path_log + 'logs\\ConnectedParties.csv',
        path_log + 'soapui-errors.log',
        path_log + 'soapui.log'
    ]
    if pycron.is_now('*/45 09 * * 1-5'):
        time.sleep(60)
        for fic in list_fic:
            with open(fic, "w"):
                pass
                print('suppression fic -> ' + fic)
    
    if pycron.is_now('*/10 8-19 * * 1-5'):
        if __name__ == "__main__":
            list_ws = [
                'getAll',
                'Perso',
                'getList',
                'Connected']
            myTestCase = testcase()
            myTestCase.soapui('PROD')
            myTestCase.getlog_soapui('PROD', list_ws)