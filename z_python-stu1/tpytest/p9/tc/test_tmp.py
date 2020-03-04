import pytest
import xlrd

def get_data():

    xls = xlrd.open_workbook('p9/数据表/data.xlsx')
    sheet = xls.sheet_by_name('Sheet1')

    inputData = []

    for x in range(sheet.nrows):
        row = sheet.row_values(x)
        print(row)
        inputData.append((row[0].strip(),int(row[1])))
    print(inputData)
    return inputData

@pytest.mark.parametrize(
    "test_input,expected",
    get_data())
def test_eval(test_input, expected):
    assert eval(test_input) == expected
