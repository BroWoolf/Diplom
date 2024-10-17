import sender_stand_request
import requests

# Виктор Павлов, 22-я когорта - Финальный проект. Инженер по тестированию плюс.

def positive():
    assert requests.get(sender_stand_request.get_url()).status_code == 200

def test_can_get_body():
    return positive()