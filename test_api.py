import requests

BASE_URL = "http://pokeapi.co/api/v2"

def test_get_pokemon_returns_200(): 
    response = requests.get(f"{BASE_URL}/pokemon/pikachu")
    assert response.status_code == 200

def test_get_pokemon_return_correct_name():
    response = requests.get(f"{BASE_URL}/pokemon/pikachu")
    data = response.json()
    assert data["name"] == "pikachu"

def test_get_pokemon_has_expected_fields():
    response = requests.get(f"{BASE_URL}/pokemon/pikachu")
    data = response.json()
    assert "height" in data
    assert "weight" in data
    assert "types" in data

def test_get_pokemon_type_is_list():
    response = requests.get(f"{BASE_URL}/pokemon/pikachu")
    data = response.json()
    assert isinstance(data["types"], list)
    assert len(data["types"]) > 0

def test_get_nonexistent_pokemon_returns_404():
    response = requests.get(f"{BASE_URL}/pokemon/not-a-real-pokemon-12345")
    assert response.status_code == 404

def test_get_pokemon_list_return_200():
    response = requests.get(f"{BASE_URL}/pokemon?limit=10")
    assert response.status_code == 200

def test_get_pokemon__list_has_correct_count():	
    response = requests.get(f"{BASE_URL}/pokemon?limit=10")
    data =  response.json()
    assert len(data["results"]) == 10


