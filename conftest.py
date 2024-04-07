import pytest
from data import CourierData
from utils.CourierUtils import CourierUtils


@pytest.fixture()
def generation_courier_data_and_delete_courier():
    # Генерируем данные для создания курьера
    data = CourierData.generation_valid_data_for_create_courier()
    yield data
    # Удаляем ранее созданного курьера
    CourierUtils.delete_courier(data)
