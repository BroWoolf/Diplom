import sender_stand_request

# Виктор Павлов, 22-я когорта - Финальный проект. Инженер по тестированию плюс.

def test_get_order_by_track_success():
    assert sender_stand_request.get_order_by_track(sender_stand_request.create_order()).status_code == 200
