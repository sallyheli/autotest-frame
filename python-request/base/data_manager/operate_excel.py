#coding:utf-8
import xlrd
from xlutils.copy import copy

class operateExcel():
    '''解析Excel测试用例'''
    def __init__(self,fName = None,sheetId = 0):
        if fName == None:
            self.filename="../data_config/caseList.xls"
        else:
            self.filename = fName
        self.data = self._openExcel()
        self.table = self.getSheetById(sheetId)
        self.row = self.table.nrows
        self.col = self.table.ncols

    def _openExcel(self):
        try:
           data = xlrd.open_workbook(self.filename)
           return data
        except Exception,e:
            raise e

    def getSheetByName(self,sheetName = None):
        sheet = self.data.sheet_by_name(sheetName)
        self.row = sheet.nrows
        self.col = sheet.ncols
        return sheet

    def getSheetById(self,sheetId=0):
        try:
            table = self.data.sheets()[sheetId]
            return table
        except Exception,e:
            raise e

    def writeData(self,row,col,info):
        readData = xlrd.open_workbook(self.filename)
        writeData = copy(self.data)
        writeTable = writeData.get_sheet(0)
        writeTable.write(row,col,info)
        writeData.save(self.filename)


    def getSheetTable(self):
        return self.table

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col


if __name__ == "__main__":
    fname = "../data_config/caseList.xlsx"
    excelData = operateExcel(fname,0)
    table = excelData.getSheetTable()
    print(str(table.row_values(1)))

