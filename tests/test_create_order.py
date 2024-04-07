# Тестовый набор для тестирования "Создание заказа"
import allure
import pytest

from utils.OrderUtils import OrderUtils
from data import (HttpStatuses, OrderData)


class TestCreateOrder:
    @allure.title('Тест успешного создания заказа')
    @allure.description('''Алгоритм тестирования: 
        1. Получение дпнных для создания заказа, 
        2. Добавление цвета в данные
        3. Создание заказа, 
        3. Проверка ответа''')
    @pytest.mark.parametrize('color', ('BLACK', 'GREY', ['BLACK', 'GREY'], []))
    def test_create_order_positive(self, color):
        data = OrderData.get_data_for_create_order()
        data['color'] = list(color)
        response = OrderUtils.create_order(data)
        assert response.status_code == HttpStatuses.CREATED and 'track' in response.text
