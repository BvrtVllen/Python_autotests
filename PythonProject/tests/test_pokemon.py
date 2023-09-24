import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id':2326})
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(f'{host}/trainers', params={'trainer_id':2326})
    assert response.json()["trainer_name"] == "Zubenko Mikhail"

@pytest.mark.parametrize('key, value', [("trainer_name", "Zubenko Mikhail")])

def test_response_json(key, value):
    response = requests.get(f'{host}/trainers', params={'trainer_id':2326})
    assert response.json()[key] == value