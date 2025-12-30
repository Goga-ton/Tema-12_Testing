import pytest
from DZ_AT03_code import get_catapi_pic

def test_get_catapi_pic(mocker):
    mock_get = mocker.patch('DZ_AT03_code.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'id' : '2nb',
        'url' : 'https://cdn2.thecatapi.com/images/2nb.jpg',
        'width': 500,
        'height': 334
    }

    url_pic = get_catapi_pic()
    assert url_pic == {
        'id' : '2nb',
        'url' : 'https://cdn2.thecatapi.com/images/2nb.jpg',
        'width': 500,
        'height': 334
    }

def test_get_catapi_pic_error(mocker):
    mock_get = mocker.patch('DZ_AT03_code.requests.get')
    mock_get.return_value.status_code = 500


    user_data = get_catapi_pic()
    assert user_data == None

