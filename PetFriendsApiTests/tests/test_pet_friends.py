from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Ириска', animal_type='британка',
                                     age='4', pet_photo='images/koshka.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/koshka.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")

def test_get_my_pets_with_valid_key(filter='my_pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    if len(result['pets']) > 0:
        assert status == 200
    else:
        raise Exception("There is no my pets")

def test_add_new_pet_without_photo_with_valid_data(name='Sauron', animal_type='собачка', age='10'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name

def test_get_api_key_invalid_email(email='shery@gmail.ru', password=valid_password):
    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result

def test_get_api_key_invalid_password(email=valid_email, password='7777'):
    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result

def test_get_api_key_for_empty_password(email=valid_email, password=''):
    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result

def test_get_api_key_for_empty_email(email='', password='0987'):
    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result

def test_add_new_pet_without_data(name='', animal_type='', age=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
    # Сверяем полученный ответ с ожидаемым результатом, в данном случае тест падает,
    # питомец с путыми параметрами добавлен - баг.
    assert status != 200

def test_add_new_pet_with_negativ_age(name='Roxi', animal_type='пантера', age='-9', pet_photo='images/bigl_004.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    #Сверяем полученный ответ с ожидаемым результатом, в данном случае тест падает,
    #питомец с отрицательным значением возраста добавлен  - баг.
    assert status != 200



















