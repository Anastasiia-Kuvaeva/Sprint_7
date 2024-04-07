# Вспомогательные методы для работы с заказами
import allure
import requests

from config import Urls


class OrderUtils:
    @staticmethod
    @allure.step('Создание заказа')
    def create_order(data):
        return requests.post(Urls.CREATE_ORDER_URL, data=data)

    @staticmethod
    @allure.step('Получение списка заказов')
    def get_order_list():
        return requests.get(Urls.GET_ORDER_LIST_URL)
