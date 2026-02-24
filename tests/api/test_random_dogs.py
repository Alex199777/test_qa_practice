import pytest


from api_clients.dog_api import DogApiClient

def test_random_dogs_image(base_url):
    dog = DogApiClient(base_url)
    response = dog.get_random_image_dog()
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data['status'] == 'success'
    assert 'https://images' in data['message']
    # response = requests.get(base_url('breeds/image/random'))
    # assert response.status_code == 200
    # data = response.json()
    # print(data)
    # assert data['status'] == 'success'
    # assert 'https://images' in data['message']


@pytest.mark.parametrize('breed', ["corgi", "dalmatian", "labrador"])
def test_random_dogs_by_breed(base_url, breed):
    dog = DogApiClient(base_url)
    response = dog.get_breed_random_image(breed)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert breed in data['message']
    assert data['status'] == 'success'


    # assert data.status_code == 200
    # response = requests.get(base_url(f'breed/{breed}/images/random'))
    # assert response.status_code == 200
