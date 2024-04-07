# Адреса endpoints
class Urls:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    CREATE_COURIER_URL = BASE_URL + "/api/v1/courier"
    LOGIN_COURIER_URL = BASE_URL + "/api/v1/courier/login"
    DELETE_COURIER_URL = BASE_URL + "/api/v1/courier/"
    CREATE_ORDER_URL = BASE_URL + "/api/v1/orders"
    GET_ORDER_BY_ID_URL = BASE_URL + "/api/v1/orders/track?t="
    GET_ORDER_LIST_URL = BASE_URL + "/api/v1/orders"