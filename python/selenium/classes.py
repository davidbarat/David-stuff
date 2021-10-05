
import selenium
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import HTMLTestRunner
import socket
import requests
import yaml
from selenium.webdriver.chrome.options import Options
import sys
import os
import pycron
import logging
import logging.config
from selenium.common.exception import NoSuchElementException
from logger import logger

import selenium.webdriver.chrome.service as service
from selenium import webdriver

class SabSDE(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Ie(
            "C:\\ProgramData\\Anaconda3\\Library\\bin\\IEDriverServer.exe")

    def test_sde(self):
        print("")
        try:
            for url in self.cfg[self.env]['url_SDE']:
                logger.info("SDE | Test OK WS sayHello " + url)
                self.driver.get(url)
                self.driver.get("javascript:document.getElementById('overridelink').click()")
                time.sleep(2)
        except:
            print("Test KO " + url)
            logger.error("SDE | Test KO WS sayHello " + url)
     
    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()

class SabProcessCenter(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.cap = webdriver.DesiredCapabilities().INTERNETEXPLORER
        inst.cap['requireWindowFocus'] = True
        inst.driver = webdriver.Ie(capabilities=inst.cap)
        inst.driver = webdriver.Ie(
            "C:\\ProgramData\\Anaconda3\\Library\\bin\\IEDriverServer.exe")

    def test_process_center(self):
        self.driver.maximize_window()
        self.driver.get(self.cfg[self.env]['url_generic'])
        self.elem = self.driver.find_element_by_id("_login")
        self.driver.execute_script(
            "arguments[0].value = 'login'",
            self.elem)

        self.driver.execute_script(
            "arguments[0].value = 'paswword'",
            self.elem)
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        logger.info("BPM | Test ouverture du Process Center ")
        try:
            self.elem = self.driver.find_element_by_id("_26287")
            self.elem.click()
        except:
            logger.error("BPM | Test ouverture du Process Center KO")

        time.sleep(5)
        self.wait = WebDriverWait(self.driver, 120)
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(
            (By.ID, 'TargetFrame')))
        task = [
            'Tâches terminées', 'Processus en erreur',
            'Instance de processus', 'Tâches en retard']

        for tasks in task:
            self.wait = WebDriverWait(self.driver, 120)
            logger.info("BPM | Taches testees :" + tasks)
            print('Taches testees ' + tasks)
            self.wait.until(EC.element_to_be_clickable((
                By.XPATH, "//span[text()='" + tasks "']"))).click()
     
    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()
        # os.system("taskkill /F /IM chrome.exe")

class SabX3S(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Ie(
            "C:\\ProgramData\\Anaconda3\\Library\\bin\\IEDriverServer.exe")

    def test_x3s(self):
        print("")
        self.driver.get(self.cfg[self.env]['url_generic'])
        self.elem = self.driver.find_element_by_id("_login")
        self.driver.execute_script(
            "arguments[0].value = 'login'",
            self.elem)    
        self.driver.execute_script(
            "arguments[0].value = 'paswword'",
            self.elem)
        self.elem = self.driver.find_element_by_id("send")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)

        self.elem = self.driver.find_element_by_id("_21113")
        self.elem.click()
        time.sleep(5)
        try:
            logger.info("X3S | Test Ouverture VGC OK")
            self.wait = WebDriverWait(self.driver, 120)
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(
                (By.NAME, 'TargetFrame')))
        except:
            logger.error("X3S | Ouverture VGC KO ")

        time.sleep(5)
        self.elems = self.driver.find_element_by_xpath("//input[@class='x3Text' and @type='text']")
        logger.info("X3S | Test id client ")
        self.elems[0].send_keys(self.cfg[self.env]['VGC_idclient'])
        time.sleep(2)
        try:
            self.elems[0].send_keys(Keys.RETURN)
            time.sleep(20)
        except:
            logger.error("X3S | Test id client KO ")
            print('Error in opening VGC')

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()

class SabVerification(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Ie(
            "C:\\ProgramData\\Anaconda3\\Library\\bin\\IEDriverServer.exe")

    def test_x3installation(self):
        print("")
        self.driver.get(self.cfg[self.env]['url_generic'])
        self.elem = self.driver.find_element_by_id("_login")
        self.driver.execute_script(
            "arguments[0].value = 'login'",
            self.elem)    
        self.driver.execute_script(
            "arguments[0].value = 'paswword'",
            self.elem)
        self.elem = self.driver.find_element_by_id("send")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)

        self.elem = self.driver.find_element_by_id("_26693")
        self.elem.click()
        time.sleep(5)
        try:
            logger.info("X3S | Ouverture Verification OK ")
            time.sleep(2)
            self.wait = WebDriverWait(self.driver, 120)
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(
                (By.NAME, 'TargetFrame')))
        except:
            print('Error in opening Vérification Installation, swith to default frame')
            logger.error("X3S | Ouverture Vérification KO ")

            self.driver.switch_to.default_content()
        logger.info("X3S | Ouverture Verification Installation depuis Service X3S ")
        self.processus = self.driver.find_element_by_xpath('//a[text()="Démarrer Processus"]')
        self.processus[2].click()
        time.sleep(2)
        
    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()
