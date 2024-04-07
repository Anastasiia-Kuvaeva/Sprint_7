# Тестовый набор для тестирования "Логин курьера"
import allure
import pytest

from utils.CourierUtils import CourierUtils
from data import HttpStatuses


class TestLoginCourier:
    @allure.title('Тест успешной авторизации курьера')
    @allure.description('''Алгоритм тестирования: 
        1. Генерация синтетичесикх данных для создания курьера, 
        2. Создание курьера, 
        3. Логин курьера
        4. Проверка ответа
        5. Удаление ранее созданного курьера''')
    def test_login_courier_positive(self, generation_courier_data_and_delete_courier):
        data = generation_courier_data_and_delete_courier
        CourierUtils.create_courier(data)
        response = CourierUtils.login_courier(data)
        assert response.status_code == HttpStatuses.OK and 'id' in response.text

    @allure.title('Тест невозможности авторизации курьера без обязательных полей')
    @allure.description('''Алгоритм тестирования: 
            1. Генерация синтетичесикх данных для создания курьера, 
            2. Создание курьера, 
            3. Удаление обязательного поля из данных
            4. Попытка логина курьера
            5. Проверка ответа
            6. Удаление ранее созданного курьера''')
    @pytest.mark.parametrize('mandatory_field', ('login', 'password'))
    def test_login_courier_negative(self, generation_courier_data_and_delete_courier, mandatory_field):
        data = generation_courier_data_and_delete_courier
        CourierUtils.create_courier(data)
        data[mandatory_field] = ""
        response = CourierUtils.login_courier(data)
        assert response.status_code == HttpStatuses.BAD_REQUEST and 'Недостаточно данных для входа' in response.text

    @allure.title('Тест невозможности авторизации курьера с некорректными логином/паролем')
    @allure.description('''Алгоритм тестирования: 
                1. Генерация синтетичесикх данных для создания курьера, 
                2. Создание курьера, 
                3. Замена значения поля на некорретное значение
                4. Попытка логина курьера
                5. Проверка ответа
                6. Удаление ранее созданного курьера''')
    @pytest.mark.parametrize('incorrect_field', ('login', 'password'))
    def test_login_courier_invalid_data_negative(self, generation_courier_data_and_delete_courier, incorrect_field):
        data = generation_courier_data_and_delete_courier
        CourierUtils.create_courier(data)
        data[incorrect_field] = incorrect_field
        response = CourierUtils.login_courier(data)
        assert response.status_code == HttpStatuses.NOT_FOUND and 'Учетная запись не найдена' in response.text
