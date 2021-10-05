
import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pandas import read_csv
import subprocess
import os
import time

class testcase():

    def __init__(self):

        self.path_soapui = 'C:\\Program Files\\SmartBear\\SoapUI-5.4.0\\bin\\'
        self.path_param_log = '-fC:\\David\\soapui\\logs\\'
        self.path_path_project_soapui = 'c:\\David\\soapui\\logs\\'
        self.path_js = 'c:\\David\\soapui\\js\\'

    def soapui(self, env):

    	param_testsuite = '-s"TestSuite Prod"'
    	subprocess.call(
                [self.path_soapui + 'testrunner.bat',
                param_testsuite,
                '-a',
                self.path_param_log,
                self.path_path_project_soapui
                ])
    
    def getlog_soapui(self, env, ws):

        for self.webservice in ws:
            self.log = 'TestSuite_' + env + '-TestCase_' + self.webservice + '-SOAP_Request-0-OK.txt'
            self.mylines = []
            with open(self.path_log_df + self.log, 'r') as file:
                for self.myline in file: # For each line, stored as myline,
                    self.mylines.append(self.mylines)
                
                self.execution_time = (self.mylines[1].split(':'))
                self.date = datetime.datetime.now()
                self.date_string = self.date.strftime("%H:%M")

                with open(self.path_log_df + self.webservice + '.csv') as self.file:
                    self.file.write(self.date_string)
                    self.file.write(";")
                    self.file.write(self.execution_time[1])
                    self.file.write("\n")

                self.df = pd.read_csv(
                    self.path_log_df + self.webservice + '.csv',
                    sep=';',
                    names = ['Time', 'Execution Time'])
                
                #js structure construction
                self.labels = [] # response_time list y axis
                self.list_response_time = self.df.values.tolist()
                for i in self.list_response_time:
                    line4 = "\"" + str(i[0]) + "\""
                    self.labels.append(line4)

                self.data = [] # time list x axis
                self.list_response_time = self.df.values.tolist()
                for i in self.list_response_time:
                    line7 = "\"" + str(i[1]) + "\""
                    self.data.append(line7)
                
                self.mylines_works = []
                with open(self.path_js + self.webservice + '.js','w') as self.file:
                    line1 = "var ctxL = document.getElementById(\"lineChart" + self.webservice + "\").getContext('2d');"
                    line2 = "var myLineChart = new Chart(ctxL, {"
                    line3 = "type: 'line'," + "\n" + "data: {" + "\n" + "labels: ["
                    self.file.write("%s \n%s\%s \n" % (
                       line1, line2, line3))
                    for self.item in self.labels:
                        if self.labels.index(self.item) == len(self.labels)-1:
                            self.file.write("%s ]" % (
                                self.item))
                        else:
                            self.file.write("%s ," %(
                                self.item))
                        line4 = ", datasets: [{"
                        self.file.write(" \n %s \n" % (line4))
                        line5 = "label: " + '"' + self.webservice + "(ms)" '"' + ","
                        self.file.write("%s \n" % (line5))
                        line6 = "data: ["
                        self.file.write("%s" % (line6))

                        # last element case (, or ] )
                        for self.item in self.data:
                            if self.data.index(self.item) == len(self.data)-1:
                                self.file.write("%s ], \n %" % (
                                    self.item))
                            else:
                                self.file.write("%s ," % (
                                    self.item))
                        
                        line8 = " backgroundColor: [ \n 'rgba(54, 162, 235, 0.3)', \n ], \n borderColor: [ \n 'rgba(54, 162, 235, 0.7)', /n ], \n borderWidth: 2 \n },"
                        self.file.write("%s" % (line8))
                        line9 = "{ \n label: \"Timeout Mulesoft\", \n data: "
                        self.file.write("%s" % (line9))
                        # Mulesoft threshold 20 ms
                        self.threshold = ['20000' for i in range(len(self.data))]
                        line10 = self.threshold
                        self.file.write("%s" % (line10))
                        line11 = ", \n backgroundColor: [ \n 'rgba(255, 0,0 )', \n ], \n borderColor: [ \n 'rgba(255, 0, 0, 0.7)',"
                        self.file.write("%s" % (line11))
                        line12 = "\n borderWidth :2  \n } \n [ \n }, \n options:{ \n responsive: true, \n } \n });"
                        self.file.write("%s" % (line12))

                time.sleep(40) # to avoid multi launch cron
