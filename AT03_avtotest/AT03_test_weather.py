import pytest
from AT03_code_weather import get_weather
import config

# Проверка функци просмотра погоды
def test_get_weather(mocker):
    mock_get = mocker.patch('AT03_code_weather.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clear sky'}],
        'main': [{'temp': 273.15}],
    }

    api_key = config.weather_key
    citi = 'Tambov'

    weather_data = get_weather(api_key, citi)
    assert weather_data == {
        'weather': [{'description': 'clear sky'}],
        'main': [{'temp': 273.15}],
    }

def test_get_weather_erro(mocker):
    mock_get = mocker.patch('AT03_code_weather.requests.get')
    mock_get.return_value.status_code = 404

    api_key = config.weather_key
    citi = 'Tambov'

    weather_data = get_weather(api_key, citi)
    assert weather_data == None

