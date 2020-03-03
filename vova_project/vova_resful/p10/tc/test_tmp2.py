import pytest

def get_data():
    with open('p10\数据表\data.csv',encoding='utf8') as f:
        lines=f.read().splitlines()
        inputData = []
        for line in lines:
            params=line.split(',')
            inputData.append((params[0].strip(),int(params[1].strip())))
    print(inputData)
    return inputData

@pytest.mark.parametrize(
    "test_input,expected",
    get_data())
def test_eval21(test_input, expected):
    assert eval(test_input) == expected
