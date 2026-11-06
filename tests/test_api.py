import requests


def test_get_booking():
    response = requests.get('https://google.com')

    assert response.status_code == 200, (
        f"\nТЕСТ ПОВАЛЕН: Неверный статус-код ответа!\n"
        f"Ожидали: 200\n"
        f"Получили: {response.status_code}"
        )
