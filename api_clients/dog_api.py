import requests

from api_clients.base_api import BaseApi


class DogApiClient(BaseApi):
    ENDPOINT = 'breeds/image/random'

    def get_random_image_dog(self):
        return self.get_response(self.ENDPOINT)



    def get_breed_random_image(self, breed):
        return self.get_response(f'breed/{breed}/images/random')


