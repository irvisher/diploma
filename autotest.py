import sender_stand_request
import requests


def test_track_order():
    track = sender_stand_request.new_order_track_number()
    result = sender_stand_request.get_track_number(track)
    assert result.status_code == 200

# Шеремет Ирина, 6 когорта — Финальный проект. Инженер по тестированию плюс
