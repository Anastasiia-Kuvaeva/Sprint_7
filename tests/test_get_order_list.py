# Тестовый набор для тестирования "Список заказов"
import allure

from utils.OrderUtils import OrderUtils
from data import (HttpStatuses)


class TestGetOrderList:
    @allure.title('Тест успешного получения списка заказов')
    @allure.description('''Алгоритм тестирования: 
        1. Получение списка заказов,        
        2. Проверка ответа''')
    def test_get_order_list_positive(self):
        response = OrderUtils.get_order_list()
        assert response.status_code == HttpStatuses.OK and 'orders' in response.text
