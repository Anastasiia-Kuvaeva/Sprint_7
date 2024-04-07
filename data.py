# Данные для тестов
from faker import Faker


class HttpStatuses:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409


class CourierData:

    # Генерация валидных данных для регистрации курьера
    @staticmethod
    def generation_valid_data_for_create_courier():
        fake = Faker("ru_RU")
        data = {
            "login": fake.user_name(),
            "password": fake.password(),
            "firstName": fake.first_name()
        }
        return data


class OrderData:

    # Получение данных для создания заказа
    @staticmethod
    def get_data_for_create_order():
        data = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "г. Смоленск, ул. Ленина, д. 7",
            "metroStation": "м. Красноармеская",
            "phone": "+70000000000",
            "rentTime": 2,
            "deliveryDate": "2020-06-06",
            "comment": "Домофон не работает",
            "color": []
        }
        return data
