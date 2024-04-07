# Вспомогательные методы для работы с курьерами
import allure
import requests

from config import Urls


class CourierUtils:
    @staticmethod
    @allure.step('Создание курьера')
    def create_courier(data):
        return requests.post(Urls.CREATE_COURIER_URL, data=data)

    @staticmethod
    @allure.step('Логин курьера')
    def login_courier(data):
        return requests.post(Urls.LOGIN_COURIER_URL, data=data)

    @staticmethod
    @allure.step('Удаление курьера')
    def delete_courier(data):
        payload = {"login": data.get("login"), "password": data.get("password")}
        response = requests.post(Urls.LOGIN_COURIER_URL, data=payload)
        courier_id = response.json().get("id")
        requests.delete(Urls.DELETE_COURIER_URL + f'/{courier_id}')
