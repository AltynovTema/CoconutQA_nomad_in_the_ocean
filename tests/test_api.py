import requests

def test_get_booking():
    response = requests.get('https://google.com')
    assert response.status_code == 999, f"Ожидаемый статус-код 999, получен {response.status_code}"
