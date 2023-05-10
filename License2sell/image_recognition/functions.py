import requests
import csv
import pandas as pd
import json, urllib3
from bs4 import BeautifulSoup
import ast
import sqllite3 as sql
from PyPDF2 import PdfReader


def createListPattern(source):
  con = sql.connect("database.db")
  cur.execute("select InstituteName, CertificationCode from Institute")
  rows = cur.fetchall()
  print(rows)
  return(rows)

def searchPatternDocumentAI(list_pattern, filename, UPLOAD_FOLDER):
  list_result = []
  reader = PdfReader(UPLOAD_FOLDER + "/" + filename)
  page = reader.page[0]
  textExtract = page.extract_text()
  extractedText = re.split('\n)\t', textExtract)
  print("extractedText: " + str(extractedText) + "\n ")
  extractedString = ' '.join(map(str, extractedText))
  
