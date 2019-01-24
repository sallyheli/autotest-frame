from caseConstParam import *
from operate_excel import *
from parse_json import *

class dataAccess:
    def __init__(self, casePath=None):
        self.casepath = "../data_config/caseList.xlsx"
        self.excel_obj = operateExcel(self.casepath, 0)
        self.case_table = self.excel_obj.getSheetTable()
        self.case_count = self.excel_obj.getRow()

        self.nameCol = getCaseNameColNum()
        self.IDCol = getCaseIdColNum()
        self.urlCol = getUrlColNum()
        self.dataCol = getDataColNum()
        self.expectCol = getExpectDataColNum()
        self.testResultCol = getTestResultColNum()
        self.needRunCol = getNeedRunColNum()
        self.methodCol = getMethodColNum()

    def get_case_name(self, row):
        return self.case_table.cell(row, self.dataCol).value

    def get_case_id(self, row):
        return self.case_table.cell(row, self.IDCol).value

    def get_case_url(self,row):
        return self.case_table.cell(row, self.urlCol).value

    def get_case_data(self, row):
        name = self.get_case_name(row)
        return parseJsonData().getData(name)

    def get_is_run(self,row):
        return self.case_table.row(row)[self.needRunCol].value

    def get_expect_data(self, row):
        return self.case_table.cell(row, self.expectCol).value

    def get_run_method(self,row):
        return self.case_table.cell(row, self.methodCol).value

    def get_row(self):
        return self.case_table.nrows


