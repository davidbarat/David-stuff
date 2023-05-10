import requests
from requests import Session
import unittest
from bs4 import BeautifulSoup

class TestSoapRequest(unittest.TestCase):
  def testsoap(self):
    self.maxDiff = None
    self.data = """ xml """
    self.soap_response = """ response xml """
    self.headers = {
      "Content-Type": "text/xml",
      "SOAPAction": "urn:getAllClientDat"
    }
    self.list_url = ['url','url/Cli?WSDL']
    
    for url in self.list_url:
      self.response = request.post(url, data=self.data, headers=self.headers, verify=False)
      print('response time: ' + str(self.response.elapsed.total_seconds()) + 's')
      xml = BeautifulSoup(self.response.text, 'xml')
      self.assertEqual(self.soap_response, str(xml.find('client')), msg='Not Equal')
      
if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)
