from fastapi.testclient import TestClient
from .main import app


MOCKED_DATA = {
    "address": "ул. Валерия Гассия, 4, корпус 4\nКонтейнер ООО \"РТС\""
               " (Чистый город) \nПринимают:\n- макулатуру;\n- "
               "пластиковые бутылки из-под напитков с маркировкой PET "
               "(01);\n- пластиковые флаконы из-под бытовой "
               "химии с маркировкой HDPE/PEHD (02);\n- пакеты (HDPE/PEHD"
               " (02));\n- плёнку,  пупырчатую плёнку,  "
               "пакеты из-под молочных продуктов, мягкие почтовые конверты"
               " (LPDE (04));\n- стрейч-плёнку,"
               "\n- вёдра;\n- ПП ящики;\n- пенопласт\nvyvozmusora23.ru\n"
               "vtormusor.ru",
    "coords": "44.9890618,39.0698255"
}

MOCKED_NULL_DATA = {
    'trashers': []
}


client = TestClient(app)


def test_get_null_trashers():
    response = client.get("/id/", params={'id': 200})
    assert response.status_code == 200
    assert response.json() == MOCKED_NULL_DATA


def test_get_trashers():
    response = client.get("/id/", params={'id': 1})
    assert response.status_code == 200
    assert MOCKED_DATA in response.json()["trashers"]
