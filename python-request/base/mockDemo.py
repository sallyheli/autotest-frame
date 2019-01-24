from mock import mock

def mockTest(url,data,response_data):
    mockMethod = mock.Mock(return_value=response_data)
    res = mockMethod(url,data)
    return res