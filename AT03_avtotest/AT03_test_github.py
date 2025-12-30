import pytest
from AT03_code_github import get_github_user
import config

def test_get_github_user(mocker):
    mock_get = mocker.patch('AT03_code_github.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login' : 'nizavr',
        'id' : 1325497,
        'name' : 'Gora'
    }

    user_data = get_github_user('VseChtoYgodno')
    assert user_data == {
        'login': 'nizavr',
        'id' : 1325497,
        'name' : 'Gora'
    }

def test_get_github_user_error(mocker):
    mock_get = mocker.patch('AT03_code_github.requests.get')
    mock_get.return_value.status_code = 500


    user_data = get_github_user('VseChtoYgodno')
    assert user_data == None