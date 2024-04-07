# Тестовый набор для тестирования "Создание курьера"
import allure
import pytest

from utils.CourierUtils import CourierUtils
from data import (HttpStatuses, CourierData)


class TestCreateCourier:
    @allure.title('Тест успешного создания курьера')
    @allure.description('''Алгоритм тестирования: 
        1. Генерация синтетичесикх данных для создания курьера, 
        2. Создание курьера, 
        3. Проверка ответа
        4. Удаление ранее созданного курьера''')
    def test_create_courier_positive(self, generation_courier_data_and_delete_courier):
        data = generation_courier_data_and_delete_courier
        response = CourierUtils.create_courier(data)
        assert response.status_code == HttpStatuses.CREATED and '{"ok":true}' in response.text

    @allure.title('Тест успешного создания курьера без поля "firstName"')
    @allure.description('''Алгоритм тестирования: 
            1. Генерация синтетичесикх данных для создания курьера, 
            2. Удаление поля "firstName" из данных
            2. Создание курьера, 
            3. Проверка ответа
            4. Удаление ранее созданного курьера''')
    def test_create_courier_without_firstname_positive(self, generation_courier_data_and_delete_courier):
        data = generation_courier_data_and_delete_courier
        del data['firstName']
        response = CourierUtils.create_courier(data)
        assert response.status_code == HttpStatuses.CREATED and '{"ok":true}' in response.text

    @allure.title('Тест невозможности создания двух одинаковых курьеров')
    @allure.description('''Алгоритм тестирования: 
            1. Генерация синтетичесикх данных для создания курьера, 
            2. Создание курьера, 
            3. Повторное создание курьера с такими же данными
            4. Проверка ответа
            5. Удаление ранее созданного курьера''')
    def test_create_double_couriers_negative(self, generation_courier_data_and_delete_courier):
        data = generation_courier_data_and_delete_courier
        CourierUtils.create_courier(data)
        response = CourierUtils.create_courier(data)
        assert response.status_code == HttpStatuses.CONFLICT and 'Этот логин уже используется' in response.text

    @allure.title('Тест невозможности создания курьера без обязательных полей')
    @allure.description('''Алгоритм тестирования: 
                1. Генерация синтетичесикх данных для создания курьера, 
                2. Удаление обязательного поля из данных
                2. Попытка создания курьера,                 
                4. Проверка ответа''')
    @pytest.mark.parametrize('mandatory_field', ('login', 'password'))
    def test_create_couriers_negative(self, mandatory_field):
        data = CourierData.generation_valid_data_for_create_courier()
        del data[mandatory_field]
        CourierUtils.create_courier(data)
        response = CourierUtils.create_courier(data)
        assert response.status_code == HttpStatuses.BAD_REQUEST and 'Недостаточно данных для создания учетной записи' in response.text
