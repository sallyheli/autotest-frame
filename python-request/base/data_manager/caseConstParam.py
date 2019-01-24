#coding:utf-8
import sys
sys.path.append("../data_config")
from data_config.const_param import *


def getCaseNameColNum():
    '''获取caseName的列号'''
    return caseName

def getCaseIdColNum():
    return caseId

def getUrlColNum():
    return url

def getDataColNum():
    return data

def getMethodColNum():
    return method

def getExpectDataColNum():
    return expectData

def getNeedRunColNum():
    return needRun

def getTestResultColNum():
    return testResult
