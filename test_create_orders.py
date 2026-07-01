# Сатин Александр, 44-когорта - Финальный проект.Инженер по тестированию плюс.

import sender_stand_request
import data


# Эта функция создает заказ и возвращает track
def create_orders_and_get_track():
    # В переменную user_body берется тело запроса из data.py
    user_body = data.orders_body.copy()
    # В переменную response сохраняется ответ при создании нового заказа
    response = sender_stand_request.post_new_orders(user_body)
    # В переменную track сохраняется track, пришедший в ответе
    track = response.json()["track"]
    return track


def test_get_order_by_track():
    # Создаём заказ и получаем его трек — вызов происходит внутри теста
    track = create_orders_and_get_track()

    # Делаем GET по треку
    response = sender_stand_request.get_orders_track(track)

    # Проверяем, что код ответа = 200
    assert response.status_code == 200